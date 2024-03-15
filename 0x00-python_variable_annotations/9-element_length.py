#!/usr/bin/env python3
"""A module that gets the length of elements in an iterable.

This module provides a function that returns a list of tuples where each
tuple contains an element of the input iterable and its length.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the length of elements in an iterable.

    Parameters:
    lst (Iterable[Sequence]): The input iterable.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples each containing an element
    from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
