def get_first(input_list: list[str]) -> str:
    return input_list[0]


def remove_first(input_list: list[str]) -> None:
    input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    first_str = input_list[0]
    input_list.pop(0)
    return first_str
