import pytest

from src.masks import get_mask, get_mask_account, get_mask_card_number


def test_get_mask():
    # Test for a 16-digit card number
    assert get_mask("1234123412341234") == "1234 12** **** 1234"
    assert get_mask(1234123412341234) == "1234 12** **** 1234"

    # Test for a 20-digit account number
    assert get_mask("12341234123412341234") == "**1234"
    assert get_mask(12341234123412341234) == "**1234"

    # Test for an invalid number length
    with pytest.raises(ValueError):
        get_mask("123")
        get_mask(123)

    # Test for invalid data type
    with pytest.raises(TypeError):
        get_mask("number")
        get_mask(["123"])
        get_mask({1: 5, 6: 8})


def test_get_mask_card_number():
    # Test for a 16-digit card number
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"
    assert get_mask_card_number(1234123412341234) == "1234 12** **** 1234"

    # Test for an invalid number length
    with pytest.raises(ValueError):
        get_mask_card_number("123")
    with pytest.raises(ValueError):
        get_mask_card_number(123)

    # Test for invalid data type
    with pytest.raises(TypeError):
        get_mask_card_number("number")
        get_mask_card_number(["123"])
        get_mask_card_number({1: 5, 6: 8})


def test_get_mask_account():
    # Test for a 20-digit account number
    assert get_mask_account("12341234123412341234") == "**1234"
    assert get_mask_account(12341234123412341234) == "**1234"

    # Test for an invalid number length
    with pytest.raises(ValueError):
        get_mask_account("123")
        get_mask_account(123)

    # Test for invalid data type
    with pytest.raises(TypeError):
        get_mask_account("number")
        get_mask_account(["123"])
        get_mask_account({1: 5, 6: 8})
