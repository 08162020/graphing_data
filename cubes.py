# Brittani Chandler
# math for cubes
# 4/22/2025

"""
cubes.py

This file includes one function: generate_cubes().

It creates a list of numbers raised to the third power (called cubes),
starting from 1 up to the number you give it. For example, if you give it 5,
it will return: [1, 8, 27, 64, 125].

"""

def generate_cubes(limit):
    """
    Creates a list of cube values from 1 to the given number.

    Parameters:
        limit (int): The last number to cube.

    Returns:
        list: A list of numbers raised to the third power.

    Example:
        If limit = 3, it returns [1, 8, 27]
    """
    return [x**3 for x in range(1, limit + 1)]

