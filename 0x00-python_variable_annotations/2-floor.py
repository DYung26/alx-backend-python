#!/usr/bin/env python3
'''
This module provides a function to compute the floor of a floating-point
number.
'''


def floor(a: float) -> int:
    '''
    Computes the largest integer less than or equal to the given
    floating-point number.

    This function effectively truncates the decimal part of the number,
    returning the integer portion.

    Args:
        a (float): The floating-point number to be floored.

    Returns:
        int: The largest integer less than or equal to `a`.

    Example:
        >>> floor(3.7)
        3
        >>> floor(-1.2)
        -2
    '''
    return int(a)
