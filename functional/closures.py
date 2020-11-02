def outer():
    print("In outer function")
    a=40
    def inner():
        b=80
        print("inner function")
        print("still in inner function, a is %d, b is %d"%(a,b))
        print("exiting inner function")
    print("Continuing outer function");