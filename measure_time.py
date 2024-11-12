from functools import wraps
import time


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__} function took {elapsed_time} seconds to run\n")
        return result

    return wrapper
