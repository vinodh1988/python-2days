def mydec(fun):
    def inner(*args,**kwargs):
        for x in args:
            print(x, ' is manipulated before')
        fun(*args,**kwargs)
        print('post process')
    return inner

#decorator without any arguments

