class classyargs:
    
    def __init__(self, arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        
    def __call__(self,fun,*args,**kwargs):
        def inner_func(*args, **kwargs):
            print("Decorating", fun.__name__)
            print(self.arg1,self.arg2, ' are the dec parameters')
            print(args, ' is being processed')
            fun(*args,**kwargs)
        return inner_func