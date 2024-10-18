"""testing find max"""

__author__ = "730796549"

from CQs.cq07.find_max import find_and_remove_max


def test_returns_correct_value() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    assert find_and_remove_max(b) == int(10)


def test_edits_list() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(b)
    assert b == [9, 8, 7]


def test_empty_list() -> None:
    assert find_and_remove_max([]) == int(-1)
