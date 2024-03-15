#!/usr/bin/env python3
"""A module for zooming in on elements of a tuple.

This module provides a function that repeats each element in a tuple a given
number of times.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on elements of a tuple.

    Parameters:
    lst (Tuple): The input tuple.
    factor (int, optional): The number of times to repeat each element.
    Defaults to 2.

    Returns:
    List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
