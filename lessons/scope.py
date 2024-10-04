"""some examples of using scope"""


def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with all instances of char removed"""
    copy: str = ""
    index: int = 0
    while index < len(msg):  # loop through all characters in message
        if not (index == char):
            copy += msg[index]  # copy over message at a specific index
        index += 1
    return copy
