import threading 
import random
import time

def first():
    while True:
        r=random.randint(0,100)
        print('first one running',r)
        time.sleep(0.2)  #blocking
        if r==17 :
            break

def second():
    while True:
        r=random.randint(0,100)
        print('second one running',r)
        time.sleep(0.2)
        if r==29 :
            break

t1 = threading.Thread(target=first) 
t2 = threading.Thread(target=second) 

t1.start()
t2.start()

t1.join()
t2.join()

print("EVERYTHING DONE")