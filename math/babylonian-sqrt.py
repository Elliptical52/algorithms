"""
Babylonian Square Root Implementation - 2/25/2026
Iteratively improves a guess for the square root of a number
Time Complexity: O(n)
"""

def babylonian_square_root(number: float, iterations: int):
    guess = number / 2
    for i in range(iterations):
        guess = (guess + (number / guess)) / 2

    return guess
