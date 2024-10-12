#!/usr/bin/env python3
'''
This module provides a function to create a multiplier function.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Creates a multiplier function that multiplies a given number by a specified
    multiplier.

    This function returns a new function that, when called with a number,
    will return the product of that number and the multiplier.

    Args:
        multiplier (float): The value by which numbers will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the product of the input and the multiplier.

    Example:
        >>> double = make_multiplier(2)
        >>> double(5)
        10.0
        >>> triple = make_multiplier(3)
        >>> triple(4)
        12.0
    '''
    return lambda x: x * multiplier
