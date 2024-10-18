"""Summing the elements of a list using different loops"""

__author__ = "730796549"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for value in vals:
        sum = sum + value
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum = sum + vals[index]
    return sum
