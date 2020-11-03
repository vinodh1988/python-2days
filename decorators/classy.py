class classy:
    def __init__(self,function):
        self.func = function

    def __call__(self,*args, **kwargs):
        print('pre logic')
        self.func(*args,**kwargs)
        print('post logic')
    
    

#__methodname__ is called as magic method or dunder method