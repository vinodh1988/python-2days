
def callfun(f):
    p=f("XXXXXXXXX") # f is a function
    print(p)
    

def temp(data):
    print("Callback fun named temp") #to be passed as callback
    return data+ " I also processed it"

def caller():
    callfun(temp);