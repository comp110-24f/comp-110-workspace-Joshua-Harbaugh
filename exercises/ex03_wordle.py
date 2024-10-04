"""EX02 - Wordle - Creating a wordle game."""

__author__ = "730796549"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user for a guess"""
    guess = input(
        f"Enter a {secret_word_len} character word: "
    )  # using an f string allows your string to change based on the variable value
    while (
        len(guess) != secret_word_len
    ):  # This loop checks to make sure that the guess is the correct number of letters
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searches through all of letters in a word to find matches to another character"""
    assert len(char_guess) == 1  # This makes sure that the character is always 1
    index = 0
    while index < len(secret_word):
        # Searches through all of the letters and identifies if it appears at least once
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compare the secret word and guess for overlapping letters"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    output_string: str = ""
    while index < len(secret):
        # This loops over all letters in the secret word
        if secret[index] == guess[index]:  # writes a green box for each exact letter
            output_string = output_string + GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]) == bool(True):
            # calls contains_char to check if the letter is anywhere in the word
            output_string = output_string + YELLOW_BOX
        else:
            output_string = output_string + WHITE_BOX
        index += 1
    return output_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1  # keeps track of how many turns a user has played
    win = 0  # keeps track of if the player has won
    while turn <= 6 and win == 0:  # Only plays the game if a person has turns left
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(len(secret))  # gets the users guess
        print(
            emojified(secret=secret, guess=user_guess)
        )  # checks the users guess for correctness
        if secret == user_guess:  # This checks if the person has won or not
            win = 1
        else:
            turn += 1
    if win == 1:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
