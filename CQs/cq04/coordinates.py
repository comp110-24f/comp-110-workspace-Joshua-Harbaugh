"""Challenge Question 04 - Coordinates"""

__author__ = "730796549"


def get_coords(xs: str, ys: str) -> None:

    x_index = 0
    y_index = 0
    while x_index < len(xs):
        while y_index < len(ys):
            print(f"({xs[x_index]},{ys[y_index]})")
            y_index += 1
        y_index = 0
        x_index += 1


get_coords(xs="hi", ys="bye")
