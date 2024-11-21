from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator takes function and filename(optional) for logging function completion or raising error with a type"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            inputs = f"Inputs: {args}, {kwargs}"
            try:
                result = func(*args, **kwargs)
                log_message = f"{func_name} ok.\n"
                return result
            except Exception as error:
                log_message = f"{func_name} error: {type(error).__name__}. {inputs}\n"
                raise error
            finally:
                if filename:
                    with open(filename, "w") as file:
                        file.write(log_message)
                else:
                    print(log_message)

        return wrapper

    return decorator
