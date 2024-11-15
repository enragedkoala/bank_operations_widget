# Bank Operations Widget
## Overview
`Bank Operations Widget` is a Python project designed to mask sensitive information and process bank operation data. The project is organized into three main packages: `masks`, `widget`, and `processing`.
src/  
├── masks.py 
├── widget.py 
└── processing.py
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
## Error Handling
* Functions in masks.py and widget.py return error messages such as "Ошибка ввода" or "Ошибка длины номера счета" for invalid input.
* processing.py functions print "invalid input" and quit if the input list is missing required keys.

## Testing
### Overview of test coverage
The project includes thorough tests for the masks.py, widget.py, and processing.py modules. These tests ensure that functions behave as expected for both valid and invalid input. The tests are organized into separate files:
*test_masks.py: Covers functions in masks.py, including:
+get_mask()
+get_mask_card_number()
+get_mask_account()
*test_widget.py: Tests functions in widget.py, including:
+mask_account_card()
+get_date()
*test_processing.py: Verifies the behavior of functions in processing.py, including:
+filter_by_state()
+sort_by_date()
Test coverage report is attached to the project and is presented as index.html in test_report_html directory

### How to Run the Tests
The project uses pytest as the testing framework. To run the tests:
1. Ensure pytest is installed:
   ```pip install pytest```
2. Run all tests from the root directory of the project:
   ```pytest```

### Test details:
test_masks.py:
*Correct masking: Tests if the functions return correctly masked card and account numbers.
*Error handling: Ensures appropriate error messages are returned for invalid data types and input lengths.

test_widget.py:
*test_mask_account_card_correct: Checks if the mask_account_card() function correctly masks valid inputs.
*test_mask_account_card_wrong_input: Verifies that invalid inputs return the correct error messages.
*test_get_date: Confirms that the get_date() function formats dates correctly and handles non-ISO inputs with appropriate error responses.

test_processing.py:
*test_filter_by_state_correct: Tests filter_by_state() with valid inputs to ensure correct filtering.
*test_filter_by_state_wrong_data_type: Checks that non-list inputs return an empty list.
*test_sort_by_date_correct: Verifies that sort_by_date() correctly sorts a list of operations.
*test_sort_by_date_no_date: Ensures that operations missing a date key or an empty list are handled gracefully.

## Requirements
* Python 3.8 or higher
   
