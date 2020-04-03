#  4 things that you need to know and understand
#  to write a decorator

def simple_func() -> None:
    """How to create a function."""
    print("I'm simple function")

def pass_func_to_func() -> None:
    """ pass func to func example.\n
        How to pass a function as an argument to a function."""
    print("I pass function 'simple_function' to BIF 'id()'")
    print(id(simple_func))
    print('Another example is BIF type(simple_func)')

def apply(func: object, value: object ) -> object:
    """ pass func to func example.\n
        accept a func and value and execute it """
    return func(value)

def return_func_from_func() -> object:
    """How to return a function from a function"""
    def inner_func() -> None:
        print('This is inner func.')

    print('This is outer func.')
    return inner_func

def run_return_func_from_func() -> None:
    """Run return_func_from_func"""
    a = return_func_from_func()
    print(type(a))
    a()

def accept_any_arg(*args) -> None:
    """How to process any number and 
    type of function argument."""
    for a in args:
        print(a, end=",")
    if args:
        print()

def accept_keyword_arg(**kwargs) -> None:
    for k,v in kwargs.items():
        print(k, v, sep="->", end=", ")
    
    if kwargs:
        print()

def accept_any_keyword_arg(*args, **kwargs) -> None:
    if args:
        print('*args')
        for a in args:
            print(a, end=",")
        print()

    if kwargs:
        print('**kwargs')
        for k,v in kwargs.items():
            print(k, v, sep="->", end=", ")
        print()

def run_accept_any_arg() -> None:
    print('accept_any_arg(10)')
    accept_any_arg(10)
    print('accept_any_arg()')
    accept_any_arg()
    print('accept_any_arg(1,2,3,4,5,6)')
    accept_any_arg(1,2,3,4,5,6)
    values = [5,6,7,8,9]
    print('accept_any_arg(list)')
    accept_any_arg(values)
    print('accept_any_arg(*list)')
    accept_any_arg(*values)

def run_accept_kwarg() -> None:
    print('accept_keyword_arg()')
    accept_keyword_arg()
    dict = {'Name': 'Python', 'Version': 3.8}
    print('accept_keyword_arg(**dict)')
    accept_keyword_arg(**dict)
    print("accept_keyword_arg(Name='C#', Version=9.0)")
    accept_keyword_arg(Name='C#', Version=9.0)

def run_accept_any_keyword_arg() -> None:
    print('accept_any_keyword_arg(1,2,3)')
    accept_any_keyword_arg(1,2,3)
    print('accept_any_keyword_arg(a=1,b=2,c=3)')
    accept_any_keyword_arg(a=1,b=2,c=3)
    print('accept_any_keyword_arg(1,2,3, a=1,b=2,c=3)')
    accept_any_keyword_arg(1,2,3, a=1,b=2,c=3)

def func_in_func() -> None:
    """ func inside func.\n 
        useful for break a complex func 
        to several simple small func."""
    msg = 'I am outer func.'

    def inner_func() -> None:
        msg = 'I am inner func.'
        print (msg)
    
    print(msg)
    inner_func()

run_accept_any_keyword_arg()
#  run_accept_kwarg()
#  run_return_func_from_func()
#  run_accept_any_arg()
#  func_in_func()
#  apply(print, 123)