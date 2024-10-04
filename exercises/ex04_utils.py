"""Completing EX04_utils"""

__author__ = "730796549"


def all(list: list[int], num: int) -> bool:
    index: int = 0
    while index < len(list):
        if list[index] != num:
            return False
        elif len(list) == 0:
            return False
        index += 1
    return True


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max: int = 0
    while index < len(list):
        if list[index] > max:
            max = list[index]
        index += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    if len(list_1) != len(list_2):
        return False
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    index: int = 0
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1


a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)
print(a)
c: list[int] = [7, 8]
extend(c, b)
print(c)
