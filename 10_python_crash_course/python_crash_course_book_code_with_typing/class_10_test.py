# Generator Example with Generator static type
from typing import Generator, Tuple, Dict, Union, Any, Callable, List
import time
from datetime import timedelta
from collections.abc import Iterator
# generator function
def my_range(start:int, end:int, step:int = 1)-> Generator[int, None, None]:
    for i in range(start, end, step):
        yield i
a:Generator[int, None, None] = my_range(1, 11)
print(a)
print(type(a))
# print(list(a)) # it will generate all items at same time
print(next(a))
print(next(a))

# =================================================================================
# Generator Example with Iterator static type
# generator function
def my_range1(start:int, end:int, step:int = 1)-> Iterator[int]:
    for i in range(start, end, step):
        yield i
b:Iterator[int] = my_range1(1, 11)
print(b)
print(type(b))
# print(list(b)) # it will generate all items at same time
print(next(b))
print(next(b))

# =================================================================================
# complicated func
def complicated_func(a:int, b:int, *args: int, **attrs: str)->Dict[str, Union[int, str, Tuple, Dict]]:
    return {
        'a': a,
        'b': b,
        'args': args,
        'attrs': attrs
    }
# print(complicated_func(1)) missing 1 required positional argument
print(complicated_func(1, 2))
print(complicated_func(1, 2, 3, 4, 5))
print(complicated_func(1, 2, 3, 4, 5, name='Muhammad Ali', education='Computer Engineering'))

# =================================================================================
# Decorator no args no return
def decorator(func: Callable[[], None])->None:
    def wrapper()->None:
        print('Something before the function is called')
        func()
        print('Something after the function is called')
    wrapper()
@decorator
def print_hello()->None:
    print('Between before and after')

# =================================================================================
# Decorator 2 args 1 return
def add_logger(func: Callable[[int, int], int]) -> Callable[[int, int], int]:
    def wrapper(a: int, b: int) -> int:
        print(f"Adding {a} and {b}")
        result = func(a, b)
        print(f"Result: {result}")
        return result
    return wrapper
    
@add_logger
def add(a: int, b: int) -> int:
    return a + b
# Example usage:
add(3, 5)
# =================================================================================
# Decorator any num of args return anythong
def timing_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        print(f"Calling {func.__name__} ") #  with args: {args} and kwargs: {kwargs}
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        # Convert execution time to HH:MM:SS format using timedelta
        execution_time_delta = timedelta(seconds=execution_time)
        execution_time_str = str(execution_time_delta).split('.')[0]
        
        print(f"{func.__name__} returned {execution_time_str} (hh:mm:ss)")
        
        return result
    return wrapper

@timing_logger
def add2(lst: List[int])->int :
    total = 0
    for i in lst:
        total += i 
    return total

# Example usage:
# result = add2(lst = list(range(1, 100_000_001)))

# =================================================================================
def factorial(n: int) -> int:
    """
    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input integer.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> factorial(5)
    120

    >>> factorial(0)
    1

    >>> factorial(1)
    1
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

result:int = factorial(5)
print(result)