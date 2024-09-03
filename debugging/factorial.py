#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Args:
        n (int): The non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the input integer n.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 factorial.py <number>")
        sys.exit(1)  # Exit with a non-zero status to indicate an error
    
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("The number must be a non-negative integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    f = factorial(number)
    print(f)
