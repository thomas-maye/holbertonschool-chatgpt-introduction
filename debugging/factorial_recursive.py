#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which the factorial is to be calculated. 
             Must be a non-negative integer.

    Returns:
    int: The factorial of the input number. If n is 0, returns 1.
         Otherwise, returns n * factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the first command-line argument, convert it to an integer, and calculate its factorial.
f = factorial(int(sys.argv[1]))

# Print the result to the console.
print(f)
