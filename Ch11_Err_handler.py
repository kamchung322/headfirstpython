import sys

def display_err_exc_info():
    try:
        1/0
    except:
        err = sys.exc_info()
        for e in err:
            print(e)
        print(err[1])

def display_err():
    try:
        1/0
    except Exception as err:
        print(err)

#  display_err()
#  display_err_exc_info()

class ConnectionError(Exception):
    pass

#  Refer to DBcm.py