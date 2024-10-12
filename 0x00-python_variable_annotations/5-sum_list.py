#!/usr/bin/env python3
'''
This module provides a function to compute the sum of a list of floating-point
numbers.
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Computes the sum of a list of floating-point numbers.

    This function takes a list of floating-point numbers as input and
    returns their total sum as a floating-point number.

    Args:
        input_list (List[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of the numbers in `input_list`.

    Example:
        >>> sum_list([1.5, 2.5, 3.0])
        7.0
        >>> sum_list([])
        0.0
    '''
    return float(sum(input_list))
