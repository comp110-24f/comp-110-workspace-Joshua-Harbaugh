"""practicing conditionals"""


def less_than_10(num: int) -> None:
    """tell us if a num < 10."""
    if num < 10:
        print("less than 10")
    else:
        print("greater than or equal to 10")
    print("end of function")


less_than_10(num=554)
