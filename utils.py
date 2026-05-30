def format_currency(amount):
    """Formats a raw number into a currency string."""
    return f"${amount:,.2f}"

def greet_user(name):
    """Generates a simple greeting message."""
    return f"Hello, {name}! Welcome to the app."

def fibonacci(n):
    """Returns the first n numbers of the Fibonacci sequence.

    Args:
        n: A non-negative integer indicating how many Fibonacci numbers to generate.

    Returns:
        A list containing the first n Fibonacci numbers.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# Future helper functions can be added below
