import functools
from typing import Callable, Any


arg_dict = dict()
def memoize(func: Callable) -> Callable:
    """Декоратор мемоизации"""
    @functools.wraps(func)
    def wrapped_func(*args) -> Any:
        if args[0] not in arg_dict: arg_dict[args[0]] = func(args[0])
        return arg_dict[args[0]]
    return wrapped_func


@memoize
def fibonacci(n: int) -> int:
    """Рекурсивный алгоритм поиска числа Фибоначчи"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))