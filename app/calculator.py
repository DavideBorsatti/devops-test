def add(a: int, b: int) -> int:
    return a

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b

