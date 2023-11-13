from typing import Callable, Any
import functools
import time


def timer(func: Callable) -> Callable:
    """Декоратор таймера"""
    work_time = 0
    @functools.wraps(func)
    def wrapped_func(*args) -> Any:
        started_time = time.time()
        value = func(*args)
        end_time = time.time()
        work = end_time - started_time
        nonlocal work_time
        work_time += work
        print(f'Функция {func.__name__} выполнялась {work: 0.05f} секунд')
        return value
    return wrapped_func


arg_dict = dict()
def memoize(func: Callable) -> Callable:
    """Декоратор мемоизации"""
    @functools.wraps(func)
    def wrapped_func(*args) -> Any:
        if args[0] not in arg_dict: arg_dict[args[0]] = func(args[0])
        return arg_dict[args[0]]
    return wrapped_func


def validate_args(func: Callable) -> Callable:
    @functools.wraps(func)
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


@timer
@memoize
def fibonacci(n: int) -> int:
    """Рекурсивный алгоритм поиска числа Фибоначчи"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

