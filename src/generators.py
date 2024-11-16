from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Function takes list of dicts, representing operations and returns Iterator with wanted currency operations"""
    for transaction in transactions:
        if (
            "operationAmount" in transaction and
            "currency" in transaction["operationAmount"] and
            transaction["operationAmount"]["currency"]["code"] == currency
        ):
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator:
    """Function takes list of dicts, representing operations and returns Iterator with operations descriptions"""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator:
    """Function generates split 16-digit card numbers in range (start, end+1)"""
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        split_card_number = f"{card_number[:4]} {card_number[5:8]} {card_number[9:12]} {card_number[12:]}"
        yield split_card_number
