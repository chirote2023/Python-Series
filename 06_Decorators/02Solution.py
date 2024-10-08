# Debugging function calls

def debug(fun):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args )
        kwargs_value = ', '.join(f"{k}={v}" for k , v in kwargs.items())
        print(f"Calling: {fun.__name__} with {args_value} and {kwargs_value}")
        return fun(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting = "Piyush"):
    print(f"{greeting}  {name} ")

hello()
greet("Nitu", greeting="Kumari")