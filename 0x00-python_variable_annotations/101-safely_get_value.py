#!/usr/bin/env python3
'''
This module provides a utility function to safely retrieve values
from a dictionary, returning a default value if the key is not found.
'''

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    Safely retrieves a value from a dictionary using a specified key.

    If the key exists in the dictionary, its associated value is returned.
    If the key is not present, the provided default value is returned instead.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key whose value should be retrieved.
        default (Union[T, None], optional): The default value to return if
                                            the key is not found.
                                            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or the default value
        if the key is missing.

    Example:
        >>> safely_get_value({'a': 1, 'b': 2}, 'a')
        1
        >>> safely_get_value({'a': 1, 'b': 2}, 'c', 0)
        0
    '''
    if key in dct:
        return dct[key]
    else:
        return default
