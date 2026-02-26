def factorial(n):
    # Check integer
    if not isinstance(n, int):
        raise ValueError("Input must be integer")

    # Check negative
    if n < 0:
        raise ValueError("Negative numbers not allowed")

    # Base cases
    if n == 0 or n == 1:
        return 1

    # Compute factorial
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result
