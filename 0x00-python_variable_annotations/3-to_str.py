#!/usr/bin/env python3
'''
This module provides a function to convert a floating-point number to a string.
'''


def to_str(n: float) -> str:
    '''
    Converts a floating-point number to its string representation.

    Args:
        n (float): The floating-point number to convert.

    Returns:
        str: The string representation of the given floating-point number.

    Example:
        >>> to_str(3.14)
        '3.14'
        >>> to_str(-0.001)
        '-0.001'
    '''
    return str(n)
