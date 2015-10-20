from functools import wraps
from threading import Thread
from multiprocessing import Process


def asyncThread(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


def asyncProcess(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        process = Process(target=func, args=args, kwargs=kwargs)
        process.start()
    return wrapper


def async(method='thread'):
    def asyncInner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if method == 'thread':
                multi = Thread(target=func, args=args, kwargs=kwargs)
            elif method == 'process':
                multi = Process(target=func, args=args, kwargs=kwargs)
            multi.start()
        return wrapper
    return asyncInner

# @async()
# # @asyncThread
# # @asyncProcess
# def test(a,b):
#     for x in xrange(a,b):
#         print x


# if __name__ == '__main__':
#     test(1,3)
#     test(4,6)
