import random
import time

def gene():
    i=1
    while i<10:
         yield random.randint(1,1000)
         time.sleep(2)
         i=i+1

def infinite():
    while True:
        yield random.randint(1,10000)
        print('continuing')
        


