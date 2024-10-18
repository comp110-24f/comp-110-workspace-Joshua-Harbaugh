from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first_return_value() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) == None


def test_remove_first_behavior() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


# Use Cases: testing properties for how we expect our program to be used
# Edge Cases: testing inputs outside of the typical or expected usage
# Command line: python -m pytest path/to/testfile.py
# python -m pytest lessons/unit_tests/list_fns_test.py
