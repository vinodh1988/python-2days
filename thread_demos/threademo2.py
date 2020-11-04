import threading
import random
import time

class SharedResource:
    def __init__(self,init=0):
        self.state = init
        self.lock = threading.Lock()
    
    def stateChanger(self):
        print('Inside thread ',threading.currentThread())
        print(threading.currentThread(), ' trying to acquire the lock')
        self.lock.acquire()
        print(threading.currentThread(), '  acquired the lock')
        temp = random.randint(0,100)
        self.state = self.state + temp
        print(threading.currentThread()," beforeProcessing ",self.state)
        time.sleep(1)
        print(threading.currentThread()," processed state ",self.state)
        
        print(threading.currentThread(), 'released the lock')

def call(shared):
    for a in range(5):
        shared.stateChanger()
        

shared = SharedResource(10)
t1 = threading.Thread(target=call,args=(shared,),name="Star Thread") 
t2 = threading.Thread(target=call,args=(shared,),name="Sky Thread") 

t1.start()
t2.start()

t1.join()
t2.join()