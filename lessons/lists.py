# Creating Lists
# list_name: list[data_type]
# each list will only contain one data type
grocery_list: list[str] = []
# write a literal for a string
numbers: list[float] = []  # creates an empty string using a constructor
numbers: list[float] = list()  # creates an empty list using a literal

# Adding objects to a list
# <list name>.append(<item>)
grocery_list.append("bananas")
numbers.append(1.5)
numbers.append(2.3)

# creating an already populated list
game_points: list[int] = [102, 86, 94]
# accessing a specific index withen a list using subscription notation
game_points[2]

# modifying something withen a string by index (because lists are mutable)
grocery_list: list[str] = ["bananas", "eggs", "bread"]
grocery_list[1] = "eggs"
grocery_list.append("bananas")

# removing an item from a list
grocery_list.pop(2)
game_points.pop(1)


# Write a function called display
def display(print_list: list[int]) -> None:
    index: int = 0
    while index < len(print_list):
        print(print_list[index])
        index += 1
