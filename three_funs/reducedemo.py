from functools import reduce

def reducedemo():
    listc=['Jackson','Harrison','Ferguson','Mahesh','Joshi','Jagan','Steven']
    print(listc)
    print("--------------------------------------")
    result=reduce(lambda x,y: x+":"+y,listc)
    print(result)

def numberreduce():
    listd=[35,35657,45,4775,5457,454,7,3,575,45477,34554]
    print(listd)
    print("--------------------------------------------------")
    result = reduce(lambda x,y: x if x>y else y,listd)
    print(result)