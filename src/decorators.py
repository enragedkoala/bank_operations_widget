def log(filename=None):
    """Decorator takes function and filiname(optional) for logging function completion or raising error with its type"""
    def decorator(func):
        def wrapper(*args, **kwargs):
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
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message)
        return wrapper
    return decorator

