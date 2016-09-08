from functools import wraps
from math import sin, pi

def squared(func):
    """
    Decorator that returns func * func
    """
    print("Executing squared")
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * func(*args, **kwargs)
    return wrapper

def minus(func):
    """
    Decorator that returns -func
    """
    print("Executing minus")
    @wraps(func)
    def wrapper(*args, **kwargs):
        return -func(*args, **kwargs)
    return wrapper

@minus
@squared
def minus_squared_sin(x):
    """
    Minus square of the sin
    """
    return sin(x)

if __name__ == "__main__":
    points = [x * pi/12 for x in range(0, 13)]
    print(list(map(minus_squared_sin, points)))
