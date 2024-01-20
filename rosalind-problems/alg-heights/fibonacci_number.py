def fibonacci_loop(number):
    """Fibonacci Loop"""
    old, new = 1, 1
    for _ in range(number - 1):
        new, old = old, old + new
    return new


print(fibonacci_loop(22))
