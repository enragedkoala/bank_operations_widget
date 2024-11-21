import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "raw, formatted",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card_correct(raw, formatted):
    assert mask_account_card(raw) == formatted


def test_mask_account_card_wrong_input():
    with pytest.raises(ValueError):
        mask_account_card("abcde")
        mask_account_card("a124455533")
        mask_account_card("Visa Classic 683198247673765833")
        mask_account_card("6644554345")
        mask_account_card("Счет 1231231231231231231231231231")
    with pytest.raises(TypeError):
        mask_account_card([1, 2, 3])
        mask_account_card({1: 5})
        mask_account_card(123123123)
        mask_account_card((1, 2, 3))


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-10-19T13:45:30") == "19.10.2023"
    assert get_date("2023-10-19") == "19.10.2023"
    assert get_date("2023-10-19 13:45:30") == "19.10.2023"


def test_get_date_invalid_input():
    with pytest.raises(ValueError):
        get_date("")
        get_date("2023.10.19")
        get_date("fff")
        get_date("2323232323")
    with pytest.raises(TypeError):
        get_date(20240311)
        get_date((1, 2, 3))
        get_date({1: 5})
        get_date([1, 2, 3])
