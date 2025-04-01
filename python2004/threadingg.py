"""
A thread is a light weight process
run()
sleep()
join()
is_alive()
getName()
start()
"""


import threading
from threading import *
from time import sleep
class first_thread(Thread):
    def run(self):
        for i in range(0,10):
            print(i,"this is 1st thread")
            sleep(2)
class second_thread(Thread):
    def run(self):
        for i in range(0,10):
            print(i,"this is 2nd thread")
            sleep(2)
t1=first_thread()
t2=second_thread()
t1.start()
print(t1.is_alive())
t2.start()
print(t2.is_alive())
t1.join()#to make thread die
print(t1.is_alive())
t2.join()
print(t2.is_alive())

print(threading.current_thread().getName())