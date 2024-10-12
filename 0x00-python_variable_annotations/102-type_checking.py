#!/usr/bin/env python3
'''
This module provides a function `zoom_array` to create a list where each
element of a given tuple is repeated multiple times based on a specified
zoom factor.
'''

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Generates a list with elements of the input tuple repeated based on
    a given zoom factor.

    Args:
        lst (Tuple): A tuple containing the elements to be zoomed (repeated).
        factor (int, optional): The number of times each element in the tuple
                                is repeated. Defaults to 2.

    Returns:
        List: A list with the elements from the tuple, each repeated
        `factor` times.

    Example:
        >>> zoom_array((1, 2, 3), 3)
        [1, 1, 1, 2, 2, 2, 3, 3, 3]
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
