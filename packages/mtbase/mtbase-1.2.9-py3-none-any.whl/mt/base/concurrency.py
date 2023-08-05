'''Concurrency in dask way. Needed for streaming workloads.'''

import queue as _q
import threading as _t
import multiprocessing as _mp
from . import home_dirpath
from .path import join, make_dirs
from .deprecated import deprecated_func
from time import sleep


__all__ = ['max_num_threads', 'Counter', 'ProcessParalleliser', 'WorkIterator']


@deprecated_func("1.2.3", suggested_func="mt.base.WorkIterator", removed_version="1.5.0", docstring_prefix="    ")
def max_num_threads(client=None, use_dask=True):
    '''Retrieves the maximum number of threads the client can handle concurrently. 

    Parameters
    ----------
    client : dask.distributed.Client, optional
        If 'use_dask' is True, this argument specifies the dask distributed client. It uses the default dask.distributed client if None is given.
    use_dask : bool
        whether or not we use dask distributed to count the number of threads. If not, we use :func:`multiprocessing.cpu_count`.
    '''
    return _mp.cpu_count()

class Counter(object):

    '''Counter class without the race-condition bug'''

    def __init__(self):
        self.val = _mp.Value('i', 0)

    def increment(self, n=1):
        with self.val.get_lock():
            self.val.value += n

    @property
    def value(self):
        return self.val.value


# ----------------------------------------------------------------------


def _worker_process(func, queue_in, queue_out, queue_ctl, logger=None):
    queues = [queue_in, queue_out, queue_ctl]
    def cleanup():
        for q in queues: # to prevent join_thread() from blocking
            q.cancel_join_thread()

    interval = 1 # 1 second interval
            
    while True:
        # get a work id
        work_id = None
        for i in range(24*60*60//interval):
            if not queue_ctl.empty():
                cleanup()
                return # stop the process
            try:
                work_id = queue_in.get(block=True, timeout=interval)
                break
            except _q.Empty:
                continue

        if work_id is None:
            if logger:
                logger.error("Waited a for a day without receiving a work id.")
                logger.error("Shutting down the background process.")        
        if not isinstance(work_id, int) or work_id < 0:
            cleanup()
            return # stop the process

        # work
        try:
            res = func(work_id)
        except:
            with logger.scoped_warn("Returning None since background worker has caught an exception", curly=False):
                logger.warn_last_exception()
            res = None

        # put the result
        ok = False
        for i in range(30//interval):
            if not queue_ctl.empty():
                cleanup()
                return # stop the process

            try:
                queue_out.put((work_id, res), block=True, timeout=interval)
                ok = True
                break
            except _q.Full:
                continue
            
        if not ok:
            if logger:
                logger.error("Unable to send the result of work id {} to the main process.".format(work_id))
                logger.error("Shutting down the background process.")
            cleanup()
            return
            


class ProcessParalleliser(object):
    '''Run a function with different inputs in parallel using multiprocessing.

    Parameters
    ----------
    func : function
        a function to be run in parallel. The function takes as input a non-negative integer 'work_id' and returns some result.
    logger : IndentedLoggerAdapter, optional
        for logging messages
    '''

    def __init__(self, func, logger=None):
        self.func = func
        self.queue_in = _mp.Queue()
        self.queue_out = _mp.Queue()
        self.queue_ctl = _mp.Queue() # control queue, to terminate things
        self.process_list = [_mp.Process(target=_worker_process, args=(func, self.queue_in, self.queue_out, self.queue_ctl), kwargs={'logger': logger}) for i in range(_mp.cpu_count())]

        # start all background processes
        for p in self.process_list:
            p.start()

        self.alive = True


    def __del__(self):
        self.close()

        
    def close(self):
        '''Closes the instance properly.'''

        if not self.alive:
            return

        is_alive = True
        self.queue_ctl.put(1) # anything here to make the queue non-empty
        while is_alive:
            # check if any process is alive
            is_alive = False
            for p in self.process_list:
                if p.is_alive():
                    is_alive = True
                    break

            if is_alive and self.queue_in.empty():
                # send a command to terminate one process
                self.queue_in.put(-1)

            sleep(0.01) # sleep a bit to give other threads/processes some time to work

        # wait for them to be terminated and joined back
        for p in self.process_list:
            p.join()
        self.alive = False


    def push(self, work_id, timeout=30):
        '''Pushes a work id to the background to run the provided function in parallel.

        Parameters
        ----------
        work_id : int
            non-negative integer to be provided to the function
        timeout : float
            number of seconds to wait to push the id to the queue before bailing out

        Returns
        -------
        bool
            whether or not the work id has been pushed

        Notes
        -----
        You should use :func:`pop` or :func:`empty` to check for the output of each work.
        '''
        if not self.alive:
            raise RuntimeError("The process paralleliser has been closed. Please reinstantiate.")
        if not isinstance(work_id, int):
            raise ValueError("Work id is not an integer. Got {}.".format(work_id))
        if work_id < 0:
            raise ValueError("Work id is negative. Got {}.".format(work_id))
        try:
            self.queue_in.put(work_id, block=True, timeout=timeout)
            return True
        except _q.Full:
            return False

    def empty(self):
        '''Returns whether the output queue is empty.'''
        return self.queue_out.empty()

    def pop(self, timeout=60*60):
        '''Returns a pair (work_id, result) when at least one such pair is available.

        Parameters
        ----------
        timeout : float
            number of seconds to wait to pop a work result from the queue before bailing output
        
        Returns
        -------
        int
            non-negative integer representing the work id
        object
            work result

        Raises
        ------
        queue.Empty
            if there is no work result after the timeout
        '''
        if not self.alive:
            raise RuntimeError("The process paralleliser has been closed. Please reinstantiate.")
        return self.queue_out.get(block=True, timeout=timeout)


# ----------------------------------------------------------------------


def worker_process_v2(func, queue_in, queue_out, queue_ctl, logger=None):

    '''
    The worker process.

    The worker process operates in the following way. There are 2 queues to communicate with the
    worker process, `queue_in` and `queue_out`.
    
    '''
    queues = [queue_in, queue_out, queue_ctl]
    def cleanup():
        for q in queues: # to prevent join_thread() from blocking
            q.cancel_join_thread()

    interval = 1 # 1 second interval
            
    while True:
        # get a work id
        work_id = None
        for i in range(24*60*60//interval):
            if not queue_ctl.empty():
                cleanup()
                return # stop the process
            try:
                work_id = queue_in.get(block=True, timeout=interval)
                break
            except _q.Empty:
                continue

        if work_id is None:
            if logger:
                logger.error("Waited a for a day without receiving a work id.")
                logger.error("Shutting down the background process.")        
        if not isinstance(work_id, int) or work_id < 0:
            cleanup()
            return # stop the process

        # work
        try:
            res = func(work_id)
        except:
            with logger.scoped_warn("Returning None since background worker has caught an exception", curly=False):
                logger.warn_last_exception()
            res = None

        # put the result
        ok = False
        for i in range(30//interval):
            if not queue_ctl.empty():
                cleanup()
                return # stop the process

            try:
                queue_out.put((work_id, res), block=True, timeout=interval)
                ok = True
                break
            except _q.Full:
                continue
            
        if not ok:
            if logger:
                logger.error("Unable to send the result of work id {} to the main process.".format(work_id))
                logger.error("Shutting down the background process.")
            cleanup()
            return


# ----------------------------------------------------------------------


class WorkIterator(object):
    '''Iterates work from id 0 to infinity, returning the work result in each iteration, but using ProcessParalleliser to do a few works ahead of time.

    Parameters
    ----------
    func : function
        a function representing the work process. The function takes as input a non-negative integer 'work_id' and returns some result in the form of `(work_id, ...)` if successful else None.
    buffer_size : int, optional
        maximum number of work resultant items to be buffered ahead of time. If not specified, default to be twice the number of processes.
    push_timeout : float, optional
        timeout in second for each push to input queue. See :func:`ProcessParalleliser.push`.
    pop_timeout : float, optional
        timeout in second for each pop from output queue. See :func:`ProcessParalleliser.pop`.
    skip_null : bool, optional
        whether or not to skip the iteration that contains None as the work result.
    logger : IndentedLoggerAdapter, optional
        for logging messages

    Notes
    -----
    Instances of the class qualify as a thread-safe Python iterator. Each iteration returns a (work_id, result) pair. To avoid a possible deadlock during garbage collection, it is recommended to explicitly invoke :func:`close` to clean up background processes.

    As of 2021/2/17, instances of WorkIterator can be used in a with statement. Upon exiting, :func:`close` is invoked.
    '''

    def __init__(self, func, buffer_size=None, skip_null=True, push_timeout=30, pop_timeout=60*60, logger=None):
        self.paralleliser = ProcessParalleliser(func, logger=logger)
        self.push_timeout = push_timeout
        self.pop_timeout = pop_timeout
        self.skip_null = skip_null
        self.push_timeout = push_timeout
        self.pop_timeout = pop_timeout
        self.send_counter = 0
        self.recv_counter = 0
        self.retr_counter = 0
        self.work_id = 0
        self.buffer_size = len(self.paralleliser.process_list)*2 if buffer_size is None else buffer_size
        self.lock = _t.Lock()
        self.alive = True

    # ----- cleaning up resources -----

    def close(self):
        '''Closes the iterator for further use.'''
        with self.lock:
            if not self.alive:
                return

            self.paralleliser.close()
            self.alive = False

    def __del__(self):
        self.close()

    # ----- with-compatibility -----

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.close()

    # ----- next ------

    def __next__(self):
        with self.lock:
            if not self.alive:
                raise RuntimeError("The instance has been closed. Please reinstantiate.")

            while True:
                max_items = max(self.recv_counter + self.buffer_size - self.send_counter, 0)
                for i in range(max_items):
                    if not self.paralleliser.push(self.send_counter, timeout=self.push_timeout):
                        break # can't push, maybe timeout?
                    self.send_counter += 1

                if self.send_counter <= self.recv_counter:
                    raise RuntimeError("Unable to push some work to background processes.")

                work_id, result = self.paralleliser.pop(timeout=self.pop_timeout)
                self.recv_counter += 1

                if self.skip_null and result is None:
                    continue
                
                self.retr_counter += 1
                return result
                

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self
