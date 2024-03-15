#!/usr/bin/env python3
"""A module for summing a mixed list of integers and floats.

This module provides a function to sum a list containing both integers and
floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum the elements of a mixed list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): The mixed list of integers and floats.

    Returns:
    float: The sum of the elements of the list.
    """
    return float(sum(mxd_lst))
