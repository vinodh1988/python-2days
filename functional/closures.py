def outer():
    print("In outer function")
    a=40
    def inner():
        
        b=80
        nonlocal a
        a=150
        print("inner function")
        print("still in inner function, a is %d, b is %d"%(a,b))
        print("exiting inner function")
    inner()
    print("Continuing outer function, a is %d"%(a));