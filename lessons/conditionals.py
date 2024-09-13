"""practicing conditionals"""


def less_than_10(num: int) -> None:
    """tell us if a num < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
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


def get_weather_report() -> str:
    weather: str = input("What is the weather? ")
    if weather == "rainy" or weather == "cold":
        print("Bring a Jacket")
    elif weather == "hot":
        print("keep cool out there")
    else:
        print("I don't recongnize this weather.")
    return weather


x: int = 1
x = x + 1
print(x)
