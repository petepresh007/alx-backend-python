#!/usr/bin/env python3
'''module for a list with mixed values'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function to sum mixed list'''
    return sum(mxd_lst)
