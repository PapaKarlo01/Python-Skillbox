import functools
from typing import Callable, Any


def validate_args(func: Callable) -> Callable:
    def wrapped_func(*args) -> Any:
        value = func(*args)
        if len(args) < 1: print("Not enough arguments")
        elif len(args) > 1: print("Too many arguments")
        else:
            if type(*args) != int: print("Wrong types")
            else:
                if args[0] < 0: print("Negative argument")
        return value
    return wrapped_func


# @validate_args
# def function(*args):
#     print("Передано аргументов: {length}".format(length=len(args)))
#     return None
#
# function(1)
