from typing import Union


def get_mask(number: Union[int, str]) -> str:
    """Func returns masked number based on its length(16 for card, 20 for account)"""
    if isinstance(number, str) and number.isdigit() or isinstance(number, int):
        num_str = str(number)
    else:
        return "Ошибка ввода(data type)"
    num_list = []
    if len(num_str) == 16:
        num_stars = num_str[0:6] + "*" * 6 + num_str[-4:]
        for i in range(0, 13, 4):
            num_list.append(num_stars[i: i + 4])
        num_masked = " ".join(num_list)
    elif len(num_str) == 20:
        num_masked = "**" + num_str[-4:]
    else:
        return "Ошибка ввода(number length)"
    return num_masked


def get_mask_card_number(number: Union[int, str]) -> str:
    """Func returns masked card number"""
    if isinstance(number, str) and number.isdigit() or isinstance(number, int):
        num_str = str(number)
    else:
        return "Ошибка ввода(data type)"
    num_list = []
    if len(num_str) == 16:
        num_stars = num_str[0:6] + "*" * 6 + num_str[-4:]
        for i in range(0, 13, 4):
            num_list.append(num_stars[i: i + 4])
        num_masked = " ".join(num_list)
    else:
        return "Ошибка ввода(number length)"
    return num_masked


def get_mask_account(number: Union[int, str]) -> str:
    """Func returns masked account number"""
    if isinstance(number, str) and number.isdigit() or isinstance(number, int):
        num_str = str(number)
    else:
        return "Ошибка ввода(data type)"
    if len(num_str) == 20:
        num_masked = "**" + num_str[-4:]
    else:
        return "Ошибка ввода(number length)"
    return num_masked
