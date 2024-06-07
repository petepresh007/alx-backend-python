#!/usr/bin/env python3
'''a module with a multiplier function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function
    """
    def multiplier_function(value: float) -> float:
        """calls the multiplier function"""
        return value * multiplier

    return multiplier_function
