from src.masks import get_mask, get_mask_card_number, get_mask_account


def test_get_mask():
    # Test for a 16-digit card number
    assert get_mask("1234123412341234") == "1234 12** **** 1234"
    assert get_mask(1234123412341234) == "1234 12** **** 1234"

    # Test for a 20-digit account number
    assert get_mask("12341234123412341234") == "**1234"
    assert get_mask(12341234123412341234) == "**1234"

    # Test for an invalid number length
    assert get_mask("123") == "Ошибка ввода(number length)"
    assert get_mask(123) == "Ошибка ввода(number length)"

    # Test for invalid data type
    assert get_mask("number") == "Ошибка ввода(data type)"
    assert get_mask(["123"]) == "Ошибка ввода(data type)"
    assert get_mask({1: 5, 6: 8}) == "Ошибка ввода(data type)"


def test_get_mask_card_number():
    # Test for a 16-digit card number
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"
    assert get_mask_card_number(1234123412341234) == "1234 12** **** 1234"

    # Test for an invalid number length
    assert get_mask_card_number("123") == "Ошибка ввода(number length)"
    assert get_mask_card_number(123) == "Ошибка ввода(number length)"

    # Test for invalid data type
    assert get_mask_card_number("number") == "Ошибка ввода(data type)"
    assert get_mask_card_number(["123"]) == "Ошибка ввода(data type)"
    assert get_mask_card_number({1: 5, 6: 8}) == "Ошибка ввода(data type)"


def test_get_mask_account():
    # Test for a 20-digit account number
    assert get_mask_account("12341234123412341234") == "**1234"
    assert get_mask_account(12341234123412341234) == "**1234"

    # Test for an invalid number length
    assert get_mask_account("123") == "Ошибка ввода(number length)"
    assert get_mask_account(123) == "Ошибка ввода(number length)"

    # Test for invalid data type
    assert get_mask_account("number") == "Ошибка ввода(data type)"
    assert get_mask_account(["123"]) == "Ошибка ввода(data type)"
    assert get_mask_account({1: 5, 6: 8}) == "Ошибка ввода(data type)"
