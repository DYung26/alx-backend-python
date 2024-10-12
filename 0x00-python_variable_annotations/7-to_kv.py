#!/usr/bin/env python3
'''
This module provides a function to convert a key-value pair into a tuple,
where the value is squared.
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Converts a key and its value into a tuple containing the key
    and the square of its value.

    The function takes a string key and a numerical value (either an integer
    or a float), calculates the square of the value, and returns a tuple
    consisting of the key and the squared value.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value to be squared, which can be an int or
        a float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.

    Example:
        >>> to_kv("age", 5)
        ('age', 25.0)
        >>> to_kv("length", 2.5)
        ('length', 6.25)
    '''
    return (k, float(v**2))
