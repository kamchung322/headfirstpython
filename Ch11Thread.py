from threading import Thread
import time

def func_print(wait: int, msg: str) -> None:
    time.sleep(wait)
    print(msg)

t1 = Thread(target=func_print, args=(3, "I'm T1"))
t2 = Thread(target=func_print, args=(0.5, "I'm T2"))
t3 = Thread(target=func_print, args=(2, "I'm T3"))
t4 = Thread(target=func_print, args=(1, "I'm T4"))

t1.start()
t2.start()
t3.start()
t4.start()
