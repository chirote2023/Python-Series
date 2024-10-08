# Chache a return value

import time

def chache(func):
    chache_value = {}
    print(chache_value)
    def wrapper(*args):
        if args in chache_value:
            return chache_value[args]
        result  = func(*args)
        chache_value[args] = result
        return result
    return wrapper


@chache
def long_function(a,b):
    time.sleep(3)
    return a + b

print(long_function(2,3))
print(long_function(4,4))