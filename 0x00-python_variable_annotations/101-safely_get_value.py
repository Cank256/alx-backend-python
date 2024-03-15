#!/usr/bin/env python3
"""A module for safely getting a value from a dictionary.

This module provides a function that returns a specified key's value from a
dictionary
or a default value if the key is not found.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
            dct: Mapping, key: Any,
            default: Union[T, None]=None
        ) -> Union[Any, T]:
    """Safely get a value from a dictionary.

    Parameters:
    dct (Mapping): The dictionary.
    key (Any): The key to look for.
    default (Union[T, None], optional): The default value. Defaults to None.

    Returns:
    Union[Any, T]: The value corresponding to the key, or the default value
    if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
