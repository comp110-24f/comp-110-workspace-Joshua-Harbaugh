"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730796549"


def input_word() -> str:
    """prompt the user for a five letter word"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:  # this checks to make sure the word is a valid 5 letter word
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # this quits the program because it was not a valid input


def input_letter() -> str:
    """prompt the user for a single letter"""
    letter: str = input("Enter a single character: ")  # prompt the user for a letter
    if len(letter) == 1:  # this checks to make sure the word is a valid single letter
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()  # this quits the program because it was not a valid input


def contains_char(word: str, letter: str) -> None:
    count = 0  # set the count equal to zero
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:  # these lines check if the letter is equal to each index
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if (
        count == 0
    ):  # thiswill print different things based on the number of letters matching
        print(" No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    elif count >= 2:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # the arguments are set equal to the return value of the other functions


if __name__ == "__main__":
    main()
