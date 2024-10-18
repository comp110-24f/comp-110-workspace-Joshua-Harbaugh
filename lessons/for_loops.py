xs: list[str] = ["w", "x", "y", "z"]

# looping over this list using a while loop
index = 0
while index < len(xs):
    print(xs[index])
    index += 1

# looping over the list using a for loop
# The element can really be named anything, but it represents each element in the list
for element in xs:
    print(element)


# example use case
my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for element in my_list:
    new_list.append(element)
print(new_list)

# practice problem
pets: list[str] = ["Louie", "Bo", "Bear"]
for element in pets:
    print(f"Good boy, {element}!")

# Range is a type of sequence you can loop over.
# Includes the start point but does not include the end point
# step defaults to one, but it just counts how many numbers you skip over each time
# range(start, end, [step=1])

# accessing both range and element
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
