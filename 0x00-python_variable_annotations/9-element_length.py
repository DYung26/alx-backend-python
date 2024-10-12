#!/usr/bin/env python3
'''
This module provides a function to compute the lengths of sequences in a list.
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes the lengths of sequences within an iterable and returns a list of
    tuples.

    Each tuple contains a sequence from the input iterable and its
    corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g.,
        lists, strings, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        a sequence
        and its length.

    Example:
        >>> element_length(["hello", [1, 2, 3], (4, 5)])
        [('hello', 5), ([1, 2, 3], 3), ((4, 5), 2)]
        >>> element_length([])
        []
    '''
    return [(i, len(i)) for i in lst]
