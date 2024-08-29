"""Plan a tea party based on the number of people that are coming"""

__author__ = "730796549"


def main_planner(guests: int) -> None:
    """Display a summary of data about a tea party based on the number of guests"""
    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of people coming"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the amount of tea people dring"""
    return int(1.5 * tea_bags(people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost based on the amount of tea and treats consumed"""
    return (0.50 * tea_count) + (0.75 * treat_count)


if __name__ == "__name__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
