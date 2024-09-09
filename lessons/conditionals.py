"""practicing conditionals"""


def less_than_10(num: int) -> None:
    """tell us if a num < 10."""
    if num < 10:
        print("less than 10")
    else:
        print("greater than or equal to 10")
    print("end of function")


def wakeup(alarm: bool) -> str:
    """return a message based on whether or not the alarm is going off"""
    if alarm is True:
        return "Wake up"
    else:
        return "keep sleeping buster"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if a letter is the first character of a word"""
    if letter == word[0]:
        return "Match"
    else:
        return "No Match"


print(check_first_letter(word="beef", letter="d"))
