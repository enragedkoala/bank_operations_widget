import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_correct(list_for_generators):
    generator_usd = filter_by_currency(list_for_generators, "USD")
    assert next(generator_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator_usd) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator_usd) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    generator_rub = filter_by_currency(list_for_generators, "RUB")
    assert next(generator_rub) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currency_empty():
    generator_empty = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(generator_empty)


def test_filter_by_currency_no_match_currency(list_for_generators):
    generator_eur = filter_by_currency(list_for_generators, "EUR")
    with pytest.raises(StopIteration):
        next(generator_eur)


def test_filter_by_currency_no_currency(list_for_processing):
    generator_no_currency = filter_by_currency(list_for_processing, "USD")
    with pytest.raises(StopIteration):
        next(generator_no_currency)


def test_filter_by_currency_data_type():
    with pytest.raises(TypeError):
        generator_str = filter_by_currency("string", "USD")
        next(generator_str)
    with pytest.raises(TypeError):
        generator_int = filter_by_currency(123, "RUB")
        next(generator_int)


def test_transaction_descriptions_correct(list_for_generators):
    generator_descriptions = transaction_descriptions(list_for_generators)
    assert next(generator_descriptions) == "Перевод организации"
    assert next(generator_descriptions) == "Перевод со счета на счет"
    assert next(generator_descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_empty():
    generator_empty = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator_empty)


def test_transaction_descriptions_no_description(list_for_processing):
    generator = transaction_descriptions(list_for_processing)
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions_data_type():
    with pytest.raises(TypeError):
        generator_str = transaction_descriptions("string")
        next(generator_str)
    with pytest.raises(TypeError):
        generator_int = transaction_descriptions(123)
        next(generator_int)


def test_card_number_generator_correct():
    generator = card_number_generator(1234567891011121, 2121212121212121)
    assert next(generator) == "1234 5678 9101 1121"
    assert next(generator) == "1234 5678 9101 1122"
    assert next(generator) == "1234 5678 9101 1123"


def test_card_number_generator_data_type():
    with pytest.raises(TypeError):
        generator_no_end = card_number_generator(1234567891011121)
        next(generator_no_end)
    with pytest.raises(TypeError):
        generator_str = card_number_generator("string")
        next(generator_str)
    with pytest.raises(TypeError):
        generator_int = card_number_generator(123123)
        next(generator_int)


def test_card_number_generator_big_number():
    with pytest.raises(TypeError):
        generator = card_number_generator(1212121212121212, 34343434343434343434)
        next(generator)
