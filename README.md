# Bank Operations Widget
## Overview
`Bank Operations Widget` is a Python project designed to mask sensitive information and process bank operation data. The project is organized into three main packages: `masks`, `widget`, and `processing`.  
src/  
├── masks.py   
├── widget.py  
├── processing.py  
└── generators.py
## Packages and Their Functionalities

### 1. `masks.py`
This package includes functions for masking card and account numbers.
- **`get_mask(number: Union[int, str]) -> str`**: Masks a number based on its length (16 for cards, 20 for accounts).
- **`get_mask_card_number(number: Union[int, str]) -> str`**: Masks a 16-digit card number with a specific format.
- **`get_mask_account(number: Union[int, str]) -> str`**: Masks a 20-digit account number by displaying only the last 4 digits with `**`.

### 2. `widget.py`
This package contains functions for formatting card/account numbers and dates.
- **`mask_account_card(crd_or_account: str) -> str`**: Reformats and masks a card or account number, validating input length and type.
- **`get_date(date_unformatted: str) -> str`**: Reformats a date string from the `yyyy-mm-dd` format to `dd.mm.yyyy`.

### 3. `processing.py`
This package provides functionality for filtering and sorting bank operations.
- **`filter_by_state(list_of_operations: list, state_wanted: str = "EXECUTED") -> list`**: Filters a list of bank operations based on a given state.
- **`sort_by_date(list_of_operations: list, descending: bool = True) -> list`**: Sorts a list of bank operations by date, with descending order as the default.

### 4. `generators.py`
This package provides functionality for filtering and sorting bank operations.
- **`filter_by_currency(transactions: list, currency: str) -> Iterator`**: Filters a list of bank operations based on currency and returning an itterator.
- **`transaction_descriptions(transactions: list) -> Iterator`**: Returns a transaction description as an itterator.  
- **`card_number_generator(start: int, end: int) -> Iterator`**: generates a card number in a given range as an itterator.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/last-bank-operations-widget.git
   ```
2. Ensure all dependencies are installed:
   ```
   pip install -r requirements.txt
   ```
## Usage
### Example for Masking Card Numbers:
```
from masks import get_mask_account, get_mask_card_number

# Masking a 16-digit card number
masked_card = get_mask_card_number("1234567890123456")
print(masked_card)  # Output: "123456******3456"
```
### Example for Widget Functions:
```
from widget import mask_account_card, get_date

# Masking and formatting a card number
result = mask_account_card("1234 5678 9101 1121")
print(result)  # Output: Formatted and masked card

# Formatting a date
formatted_date = get_date("2024-10-19")
print(formatted_date)  # Output: "19.10.2024"
```
### Example for Processing Functions:
```
from processing import filter_by_state, sort_by_date

# Filtering operations by state
operations = [{"state": "EXECUTED", "date": "2024-10-19"}, {"state": "PENDING", "date": "2024-09-15"}]
executed_ops = filter_by_state(operations)
print(executed_ops)

# Sorting operations by date
sorted_ops = sort_by_date(operations)
print(sorted_ops)
```

### Example for Generators Functions:
```
# Sample to work with
transactions = [
    {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
]
# This function filters transactions based on the specified currency and returns an iterator of matching transactions.
for transaction in filter_by_currency(transactions, "USD"):
    print(transaction)
# Generates an iterator that yields the descriptions of transactions.
for description in transaction_descriptions(transactions):
    print(description)
#  Generates card numbers in the format XXXX XXXX XXXX XXXX from a given start to an end value.
for card_number in card_number_generator(1, 5):
    print(card_number)
```
## Error Handling
- Functions in masks.py and widget.py return error messages such as "Invalid input(number length)" or "Invalid input(data type)" for invalid input.
- processing.py functions print "invalid input" and quit if the input list is missing required keys.
- functions in generators.py raise `TypeError` for invalid input

## Testing
### Overview of test coverage
The project includes thorough tests for the `masks.py`, `widget.py`, and `processing.py` modules. These tests ensure that functions behave as expected for both valid and invalid input. The tests are organized into separate files:
1. **`test_masks.py`**: Covers functions in `masks.py`, including:
- `get_mask()`
- `get_mask_card_number()`
- `get_mask_account()`
2. **`test_widget.py`**: Tests functions in widget.py, including:
- `mask_account_card()`
- `get_date()`
3. **`test_processing.py`**: Verifies the behavior of functions in processing.py, including:
- `filter_by_state()`
- `sort_by_date()`
4. **`test_generators.py`**: Verifies the behavior of functions in generators.py, including:
- `filter_by_currency()`
- `transaction_descriptions()`
- `card_number_generator`
Test coverage report is attached to the project and is presented as index.html in test_report_html directory

### How to Run the Tests
The project uses pytest as the testing framework. To run the tests:
1. Ensure pytest is installed:
   ```pip install pytest```
2. Run all tests from the root directory of the project:
   ```pytest```

### Test details:
**`test_masks.py`**:
- Correct masking: Tests if the functions return correctly masked card and account numbers.
- Error handling: Ensures appropriate error messages are returned for invalid data types and input lengths.

**`test_widget.py`**
- `test_mask_account_card_correct`: Checks if the mask_account_card() function correctly masks valid inputs.
- `test_mask_account_card_wrong_input`: Verifies that invalid inputs return the correct error messages.
- `test_get_date`: Confirms that the get_date() function formats dates correctly and handles non-ISO inputs with appropriate error responses.

**`test_processing.py`**:
- `test_filter_by_state_correct` Tests filter_by_state() with valid inputs to ensure correct filtering.
- `test_filter_by_state_wrong_data_type`: Checks that non-list inputs return an empty list.
- `test_sort_by_date_correct`: Verifies that sort_by_date() correctly sorts a list of operations.
- `test_sort_by_date_no_date`: Ensures that operations missing a date key or an empty list are handled gracefully.

**`test_generators.py`**:
- `test_filter_by_currency_correct`: Verifies that the filter_by_currency function returns correct transactions matching the specified currency.
- `test_filter_by_currency_empty`: Ensures that an empty input returns an iterator that raises StopIteration.
- `test_filter_by_currency_no_match_currency`: Tests when no transaction matches the specified currency.
- `test_filter_by_currency_data_type`: Checks that non-list inputs raise a TypeError.
- `test_transaction_descriptions_correct`: Confirms that the transaction_descriptions function yields correct descriptions.
- `test_transaction_descriptions_empty`: Verifies that an empty list input raises StopIteration.
- `test_transaction_descriptions_data_type`: Checks that non-list inputs raise a TypeError.
- `test_card_number_generator_correct`: Verifies correct generation of card numbers.
- `test_card_number_generator_data_type`: Checks that invalid inputs raise TypeError.
- `test_card_number_generator_big_number`: Ensures that excessively large numbers raise TypeError.

## Requirements
- Python 3.8 or higher
   

