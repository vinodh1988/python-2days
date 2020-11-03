#python directly dont support the concept of overloading
#indirectly we can achieve it by using 
    # function with default parameters
    # function with iterable as parameters
def params(*args,**kwargs):
    for x in args:
        print(x)
  
    print(kwargs)
    print("-----------------------------------")

def fun(a,b):
    print(a,b)

def fun(a,b,c=900):
    print(a,b,c)

params(1,4,5,pen=34,paper=90)
params(2,3,4)
params('Lara','Janak');
fun(b=53,a="jack")
