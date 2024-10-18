"""Test functions for ex05."""

__author__ = "730796549"

# Allows us to use the functions in our other program
from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return() -> None:
    """Tests that the function returns the correct even numbers from a test list."""
    input_list: list[int] = [4, 5, 6]  # Creating a test list
    assert only_evens(input_list) == [4, 6]  # Checks the return value is correct


def test_only_evens_mutation() -> None:
    """Tests that the function does not change the original list."""
    input_list: list[int] = [4, 5, 6]  # Creating a test list
    only_evens(input_list)  # Calls the function
    assert input_list == [4, 5, 6]  # Checks the function has not been changed


def test_only_evens_empty_list() -> None:
    """Tests that the function works correctly with an empty original list."""
    input_list: list[int] = []  # Creating a test list
    assert only_evens(input_list) == []  # Checks the return value is correct


def test_sub_return() -> None:
    """Tests that the function returns the correct smaller list."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6]  # Creating a test list
    assert sub(input_list, 1, 4) == [2, 3, 4]  # Checks the return value is correct


def test_sub_mutation() -> None:
    """Tests that the function does not change the original list."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6]  # Creating a test list
    sub(input_list, 1, 4)  # Calls the function
    assert (input_list) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]  # Checks the function has not been changed


def test_sub_greater_start() -> None:
    """Returns the correct value when the start index is greater than the end index."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6]  # Creating a test list
    assert sub(input_list, 4, 1) == []  # Checks the return value is correct


def test_add_at_index_return() -> None:
    """Tests that the function has no return value."""
    input_list: list[int] = [10, 20, 30, 40, 50]  # Creating a test list
    assert add_at_index(input_list, 4, 1) == None  # Checks the return value is correct


def test_add_at_index_mutable() -> None:
    """Tests that the function changes the list is the correct way."""
    input_list: list[int] = [10, 20, 30, 40, 50]  # Creating a test list
    add_at_index(input_list, 4, 1)  # Calls the function
    assert input_list == [10, 4, 20, 30, 40, 50]  # Checks the function has been changed


def test_add_at_index_out_of_range() -> None:
    """Tests that the function raises an error when it is supposed to."""
    input_list: list[int] = [10, 20, 30, 40, 50]  # Creating a test list
    with pytest.raises(IndexError):  # Checks that calling the function raises an error
        add_at_index(input_list, 4, 15)
