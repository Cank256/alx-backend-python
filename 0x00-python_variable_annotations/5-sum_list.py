#!/usr/bin/env python3
"""A module for summing a list of floats.

This module provides a function to sum a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum the elements of a list of floats.

    Parameters:
    input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the elements of the list.
    """
    return sum(input_list)
