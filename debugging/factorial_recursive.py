#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input integer `n`.

    Example:
        factorial(4) returns 24, since 4! = 4 * 3 * 2 * 1 = 24.

    Note:
        The factorial of 0 is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Parse the input from command line argument
    f = factorial(int(sys.argv[1]))
    # Print the result of the factorial calculation
    print(f)
