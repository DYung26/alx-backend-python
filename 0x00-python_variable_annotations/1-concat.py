#!/usr/bin/env python3
'''
This module provides a function to concatenate two strings.
'''


def concat(str1: str, str2: str) -> str:
    '''
    Concatenates two strings and returns the resulting string.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string of `str1` and `str2`.

    Example:
        >>> concat("Hello, ", "world!")
        'Hello, world!'
    '''
    return str1 + str2
