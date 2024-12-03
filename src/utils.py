from functools import wraps
from time import time
import os
import sys

called_from_directory = os.path.dirname(sys.modules["__main__"].__file__)

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw.keys(), te-ts))
        return result
    return wrap

@timing
def get_input(file_name) -> list: 
    input_path = os.path.join(called_from_directory, file_name)
    print("Reading file at:", input_path)
    with open(input_path) as input:
        i =  input.read().splitlines()

    return i