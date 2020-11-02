global_state = "global variable"
def outer(param):
    print("In outer function")

    a=40
    state=param
    global global_state
    global_state = param
    #inner function definition
    def inner():
        
        b=80
        nonlocal a
        a=150
        print("inner function")
        print("still in inner function, a is %d, b is %d and state is %s"%(a,b,state))
        print("exiting inner function")
    # again in outer
    print("Continuing outer function, a is %d"%(a));
    #function as return type
    return inner

def something():
    print(global_state);
   

