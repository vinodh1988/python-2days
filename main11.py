from generators import infinite


geny = infinite()
while True:
    result=next(geny)
    print(result)
    if result%10==0:
        break;