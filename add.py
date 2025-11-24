def add(x: int, y: int) -> int:
    if not isinstance(x,int) or not is instance(y,int):
        raise TypeError("Both arguements must be integers")
    """Returns the sum of two integers."""
    return x + y
