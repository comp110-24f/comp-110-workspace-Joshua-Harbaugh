"""Plan a tea party based on the number of people that are coming"""

__author__ = "730796549"


def main_planner(guests: int) -> None:
    """Display a summary of data about a tea party based on the number of guests"""
    print(
        "A cozy tea party for " + str(guests) + " people!"
    )  # print the number of guests in a sentence
    print("Tea Bags: " + str(tea_bags(people=guests)))  # print the number of tea bads
    print("Treats: " + str(treats(people=guests)))  # print the number of treats
    print(
        "Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests)))
    )  # call tea and treats to calculate the total number of each item needed based on the number of guests


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of people coming"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the amount of tea people dring"""
    return int(
        1.5 * tea_bags(people)
    )  # call the tea_bags function to find the number of tea bags based on the number of people


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost based on the amount of tea and treats consumed"""
    return (0.50 * tea_count) + (
        0.75 * treat_count
    )  # multiply the number of each item by its unit cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
