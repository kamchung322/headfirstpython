from flask import session
from functools import wraps

### A decorator example

def check_logged_in(func):
    @wraps(func)  #  must be placed here.
    def wrapper(*args, **kwargs):  # def the wrapper func to decorate the func.
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'
    
    return wrapper