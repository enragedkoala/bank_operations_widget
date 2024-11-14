from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("raw, formatted", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                ("Счет 64686473678894779589", "Счет **9589"),
                                            ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")])
def test_mask_account_card_correct(raw, formatted):
    assert mask_account_card(raw) == formatted


def test_mask_account_card_wrong_input():
    assert mask_account_card("abcde") == "Invalid input(not a number)"
    assert mask_account_card([1,2,3]) == "Invalid input(data type)"
    assert mask_account_card({1: 5}) == "Invalid input(data type)"
    assert mask_account_card(123123123) == "Invalid input(data type)"
    assert mask_account_card("a124455533") == "Invalid input(not a number)"
    assert mask_account_card("Visa Classic 683198247673765833") == "Invalid input(number length)"
    assert mask_account_card("6644554345") == "Invalid input(number length)"
    assert mask_account_card("Счет 1231231231231231231231231231") == "Invalid input(number length)"
    assert mask_account_card((1,2,3)) == "Invalid input(data type)"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-10-19T13:45:30") == "19.10.2023"
    assert get_date("2023-10-19") == "19.10.2023"
    assert get_date("2023-10-19 13:45:30") == "19.10.2023"
    assert get_date("") == "Not an ISO format date"
    assert get_date("2023.10.19") == "Not an ISO format date"
    assert get_date("fff") == "Not an ISO format date"
    assert get_date("2323232323") == "Not an ISO format date"
    assert get_date(20240311) == "Invalid input(data type)"
    assert get_date((1,2,3)) == "Invalid input(data type)"
    assert get_date({1: 5}) == "Invalid input(data type)"
    assert get_date([1,2,3]) == "Invalid input(data type)"
