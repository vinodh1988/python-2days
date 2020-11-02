def mapdemo():
    listb=['Javid','Harish','Nicholas','Shaun','Javagal']
    print(listb)
    print("--------------------------------------")
    result=list(map(lambda x: x.upper() if len(x)>6 else  x[::-1],listb))
    print(result)
