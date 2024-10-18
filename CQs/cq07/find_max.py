"""writing a find max function"""

__author__ = "730796549"


def find_and_remove_max(input_list: list[int]) -> int:
    if len(input_list) == 0:
        return -1
    else:
        max = input_list[0]
        for number in input_list:
            if number > max:
                max = number
        index = 0
        while index < len(input_list):
            if max == input_list[index]:
                input_list.pop(index)
                index = index - 1
            index += 1
        return max


b: list[int] = [10, 9, 8, 7, 10]
print(find_and_remove_max(b))
print(b)
