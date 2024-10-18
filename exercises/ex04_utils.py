"""Completing EX04_utils."""

__author__ = "730796549"


def all(list: list[int], num: int) -> bool:
    """This function will check if all the numbers in a list are equal to a number."""
    index: int = 0
    if len(list) == 0:  # makes sure that there are values in the list
        return False
    while index < len(list):  # Loops over all numbers in list
        if list[index] != num:  # Checks if each index is equal to the number
            return False
        elif len(list) == 0:  # checks if the list is empty
            return False
        index += 1
    return True


def max(list: list[int]) -> int:
    """This function will return the maximum number in a list of numbers."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max: int = list[0]  # This sets the value of max to the first number in a list
    while index < len(list):
        if (
            list[index] > max
        ):  # This checks if each number is greater than the previous max number
            max = list[index]
        index += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """This function will check if two functions are exactly equal."""
    index: int = 0
    if len(list_1) != len(list_2):  # This makes sure the lists are the same length
        return False
    while index < len(list_1):  # Loops over all indexes in the lists
        if list_1[index] != list_2[index]:  # Checks to see if each index is different
            return False
        index += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """This function will append one list of numbers to another list of numbers."""
    index: int = 0
    while index < len(list_2):
        list_1.append(list_2[index])  # appends the current index of list_2 to list_1
        index += 1
