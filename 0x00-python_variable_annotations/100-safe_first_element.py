#!/usr/bin/env python3
'''
This module provides a utility function to safely retrieve the first element
from a sequence, returning None if the sequence is empty.
'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Safely retrieves the first element from a given sequence.

    If the sequence is not empty, the first element is returned.
    If the sequence is empty, None is returned.

    Args:
        lst (Sequence[Any]): The sequence from which the first element is
        retrieved.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the
        sequence is empty.

    Example:
        >>> safe_first_element([1, 2, 3])
        1
        >>> safe_first_element([])
        None
    '''
    if lst:
        return lst[0]
    else:
        return None
