#!/usr/bin/env python3
from typing import List
"""type-annotated function sum_mixed_list which takes a list mxd_lst
 of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxt_lst: List[int, float]) -> float:
    """Returns sum as a float"""
    return float(sum(mxt_lst))
