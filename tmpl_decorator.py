from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
        # 1.  Code to excute BEFORE calling the decorated function.

        # 2.  Call the decorated function as required, returning
        #     its results if needed.
        return func(*args, **kwargs)

        # 3.  Code to execute INSTEAD OF calling the decorated function.

    return wrapper