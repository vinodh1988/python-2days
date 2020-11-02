
def filterIt(x):
    if x%7 == 0:
        return True
    else:
        return False
    
def filterdemo():
    lista=[349,749,777,126,99,5849,34,245,646,75768]
    print(lista)
    print('--------------------------------------')
    result=list(filter(filterIt,lista));
    print(result)
    print('---------------------------------------------')
    result2=list(filter(lambda x: True if x>900 else False,lista))
    print(result2)
    print('---------------------------------------------')
    result2=list(filter(lambda x: filterIt(x),lista))
    print(result2)

