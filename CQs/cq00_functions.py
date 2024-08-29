"""Challenge Question 00"""

__author__ = "730796549"


def mimic(message: str) -> str:
    """Print your message back to you"""
    return message


def main() -> None:
    """Call the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
