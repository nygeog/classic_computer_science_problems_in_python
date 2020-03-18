"""
Fibonacci sequence, a sequence of numbers such that any number except for the
first and second, is the sum of the previous two.

fib(n) = fib(n - 1) + fib(n - 2)

This can trivially be translated into a recursive Python function
A recursive function is a function that calls itself.
"""


def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(5))

# THIS WILL NOT RUN!!! RecursionError: maximum recursion depth exceeded.
