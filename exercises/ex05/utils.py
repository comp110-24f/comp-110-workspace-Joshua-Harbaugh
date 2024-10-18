"""Implement functions for ex05."""

__author__ = "730796549"


def only_evens(input_list: list[int]) -> list[int]:
    """Creates a new list with only the even numbers from a list."""
    even_list: list[int] = []
    for number in input_list:  # Loops over ever element in the list
        if number % 2 == 0:  # Checks to see if the number is even
            even_list.append(number)  # appends the even numbers to the new list
    return even_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Creates a subset of a currently existing list as a new list."""
    subset_list: list[int] = []  # creates a new empty list
    if (
        len(input_list) == 0 or start_index >= len(input_list) or end_index <= 0
    ):  # Checks for conditions in which there will be nothing in the new list
        return subset_list
    if (
        start_index < 0
    ):  # makes sure that the start index only counts real indices withen the list
        start_index = 0
    if end_index > len(
        input_list
    ):  # Checks to make sure that it is not using indices greater than those that exist
        end_index = len(input_list)
    index = start_index
    while (
        index < end_index
    ):  # appends each selected element in the old list to the new list
        subset_list.append(input_list[index])
        index += 1
    return subset_list


def add_at_index(input_list: list[int], input_int: int, input_index: int) -> None:
    """Adds a new element at a specific index withen an existing list."""
    if (
        input_index > (len(input_list)) or input_index < 0
    ):  # This will raise an error if the index is not valid.
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(1)  # Adds a new element to the list
    index: int = (
        len(input_list) - 1
    )  # Sets the index equal to the last element in the list
    while index > input_index:  # Moves each element in the list one index up
        input_list[index] = input_list[index - 1]
        index = index - 1
    if index == input_index:  # Inserts the new element at the selected index
        input_list[index] = input_int
