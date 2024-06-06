#!/usr/bin/env python3
"""a module for complex annotation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple where the first element is the string k
    """
    return (k, float(v ** 2))
