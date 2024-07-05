def mask_account_card(crd_or_accnt: str) -> str:
    """Returns reformated card or accnt number"""
    number = crd_or_accnt.split(" ")[-1]
    if not number.isdigit():
        return "Ошибка ввода"
    num_list = []
    if len(number) == 16:
        num_stars = number[0:6] + "*" * 6 + number[-4:]
        for i in range(0, 13, 4):
            num_list.append(num_stars[i : i + 4])
        num_masked = " ".join(num_list)
    elif len(number) == 20:
        num_masked = "**" + number[-4:]
    else:
        return "Ошибка длины номера счета"
    formated = " ".join(crd_or_accnt.split(" ")[:-1]) + " " + num_masked
    return formated


def get_date(date_unform: str) -> str:
    """Returns date in dd.mm.yyyy format"""
    date_formated = f"{date_unform[8:10]}.{date_unform[5:7]}.{date_unform[0:4]}"
    return date_formated

