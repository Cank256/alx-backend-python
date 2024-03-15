#!/usr/bin/env python3
"""A module that converts a string and a number into a tuple.

This module provides a function that takes a string and a number (int or float)
and returns a tuple with the string and the square of the number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a string and a number into a tuple.

    Parameters:
    k (str): The string.
    v (Union[int, float]): The number (integer or float).

    Returns:
    Tuple[str, float]: A tuple containing the string and the square of the
    number.
    """
    return (k, v * v)
