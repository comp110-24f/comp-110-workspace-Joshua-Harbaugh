"""Challenge Question 02"""

__author__ = "730796549"


def guess_a_number() -> None:
    """set a secret number and then guess the number. then give feedback on the guess"""
    secret: int = 7
    guess: int = int(input("Guess a number."))
    print("Your guess was " + str(guess))
    if secret == guess:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
