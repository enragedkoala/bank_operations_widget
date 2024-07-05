from masks import get_mask_account, get_mask_card_number


def mask_account_card(crd_or_accnt: str) -> str:
    """Returns reformated card or accnt number"""
    unformatted_list = crd_or_accnt.split(" ")
    number = "".join([i for i in unformatted_list if i.isdigit()])
    if not number.isdigit():
        return "Ошибка ввода"
    if len(number) == 16:
        num_masked = get_mask_card_number(number)
    elif len(number) == 20:
        num_masked = get_mask_account(number)
    else:
        return "Ошибка длины номера счета"
    formatted = " ".join([i for i in unformatted_list if i.isalpha()]) + " " + num_masked
    return formatted


def get_date(date_unform: str) -> str:
    """Returns date in dd.mm.yyyy format"""
    date_formated = f"{date_unform[8:10]}.{date_unform[5:7]}.{date_unform[0:4]}"
    return date_formated
