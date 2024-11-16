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


def transaction_descriptions():
    pass


def card_number_generator():
    pass
