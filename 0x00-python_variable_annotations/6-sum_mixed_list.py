#!/usr/bin/env python3
'''
This module provides a function to compute the sum of a mixed list of integers
and floating-point numbers.
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Computes the sum of a list containing both integers and floating-point
    numbers.

    This function takes a list that may include both integer and float values,
    sums them up, and returns the total as a floating-point number.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or
        floats to sum.

    Returns:
        float: The sum of the numbers in `mxd_lst`.

    Example:
        >>> sum_mixed_list([1, 2.5, 3, 4.0])
        10.5
        >>> sum_mixed_list([])
        0.0
    '''
    return float(sum(mxd_lst))
