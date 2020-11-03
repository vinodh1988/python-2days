from functools import wraps

def argsdeco(arg1, arg2):

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print("Arguements passed to decorator %s and %s" % (arg1, arg2) )
            print("doing preprocessing")
            ret=function(*args, **kwargs)
            print("doing postprocessing",ret)
            return ret
        return wrapper
    return inner_function


#decorater with arguments