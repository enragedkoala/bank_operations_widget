from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Returns reformated card or account number"""
    if not isinstance(card_or_account, str):
        raise TypeError("Invalid input(data type)")
    unformatted_list = card_or_account.split(" ")
    number = "".join([i for i in unformatted_list if i.isdigit()])
    if not number.isdigit():
        raise ValueError("Invalid input(not a number)")
    if len(number) == 16:
        num_masked = get_mask_card_number(number)
    elif len(number) == 20:
        num_masked = get_mask_account(number)
    else:
        raise ValueError("Invalid input(number length)")
    formatted = " ".join([i for i in unformatted_list if i.isalpha()]) + " " + num_masked
    return formatted


def get_date(date_unformatted: str) -> str:
    """Returns date in dd.mm.yyyy format"""
    if not isinstance(date_unformatted, str):
        raise TypeError("Invalid input(data type)")
    try:
        datetime.fromisoformat(date_unformatted)
    except ValueError:
        raise ValueError("Not an ISO format date")
    date_formatted = f"{date_unformatted[8:10]}.{date_unformatted[5:7]}.{date_unformatted[0:4]}"
    return date_formatted
