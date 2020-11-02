from functional import callable,callable2


#function as a parameter to another function
#callback functions in python
#any function which is passed as parameter to another function will usually be called back
def myprocess(p):
    print("Pre processing is being done")
    p()
    print("Post processing is being done");

myprocess(callable)

myprocess(callable2)

def temp():
    print("Temporary definition")

myprocess(temp)


