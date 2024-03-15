#!/usr/bin/env python3
"""A module that creates a multiplier function.

This module provides a function that takes a float multiplier and returns
another function that multiplies any float by this multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function.

    Parameters:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies any float by the
    multiplier.
    """
    return lambda x: x * multiplier
