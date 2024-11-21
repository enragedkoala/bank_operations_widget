from typing import Union


def log(filename=None):
    """"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            inputs = f"Inputs: {args}, {kwargs}"
            try:
                log_message = f"{func_name} started. {inputs}\n"
                result = func(*args, **kwargs)
                log_message += f"{func_name} ok. Result: {result}\n"
                return result
            except Exception as error:
                log_message += f"{func_name} error: {type(error).__name__}. {inputs}\n"
                raise error
            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message)
        return wrapper
    return decorator


@log(filename="get_mask_log")
def get_mask(number: Union[int, str]) -> str:
    """Func returns masked number based on its length(16 for card, 20 for account)"""
    if isinstance(number, str) and number.isdigit() or isinstance(number, int):
        num_str = str(number)
    else:
        print("Invalid input(data type)")
        raise TypeError
    num_list = []
    if len(num_str) == 16:
        num_stars = num_str[0:6] + "*" * 6 + num_str[-4:]
        for i in range(0, 13, 4):
            num_list.append(num_stars[i : i + 4])
        num_masked = " ".join(num_list)
    elif len(num_str) == 20:
        num_masked = "**" + num_str[-4:]
    else:
        print("Invalid input(number length)")
        raise ValueError
    return num_masked

y = get_mask("1234123412f341234")
