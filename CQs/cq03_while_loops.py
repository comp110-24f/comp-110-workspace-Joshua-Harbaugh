"""Challenge Question 03"""

__author__ = "730796549"


def num_instances(phrase: str, search_char: str) -> int:
    """Count how many times a letter appears in a phrase"""
    count = 0
    index = 0
    while index < len(phrase):  # loop over every letter in the phrase
        if phrase[index] == search_char:
            count = count + 1  # add one to the number of times the letter appears
        index = index + 1  # increase the index by one
    return count


if __name__ == "__main__":
    print(num_instances(phrase="pizza", search_char="p"))
