from typing import overload, Union

class Calculator:
    
    @overload
    def add(self, a: int, b: int) -> int:
        ...

    @overload
    def add(self, a: float, b: float) -> float:
        ...

    @overload
    def add(self, a: str, b: str) -> str:
        ...

    def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        elif isinstance(x, float) and isinstance(y, float):
            return x + y
        elif isinstance(x, str) and isinstance(y, str):
            return x + y
        else:
            raise TypeError('Invalid argument types: Expected (int, int), (float, float), or (str, str).')

# Usage Example
calculator: Calculator = Calculator()

# Valid operations
result_int = calculator.add(5, 10)            # Returns 15 (int)
result_float = calculator.add(5.5, 10.2)      # Returns 15.7 (float)
result_str = calculator.add("Hello, ", "World!") # Returns 'Hello, World!' (str)

print(f"Integer Addition: {result_int}")       # Output: 15
print(f"Float Addition: {result_float}")       # Output: 15.7
print(f"String Concatenation: {result_str}")   # Output: 'Hello, World!'