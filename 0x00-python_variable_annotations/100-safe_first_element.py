#!/usr/bin/env python3
"""A module for safely getting the first element of a sequence.

This module provides a function that returns the first element of a sequence
or None if the sequence is empty.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Safely get the first element of a sequence.

    Parameters:
    lst (Sequence[Any]): The input sequence.

    Returns:
    Optional[Any]: The first element of the sequence, or None if the sequence
    is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
