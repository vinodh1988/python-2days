from decorators import mydec

@mydec
def logicfun(parameter1,parameter2):
    print(parameter1,' in function call')
    print(parameter2,' in function call')

logicfun('India','Asia')
