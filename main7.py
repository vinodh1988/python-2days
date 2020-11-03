from decorators import argsdeco

@argsdeco("positional parameter 1","postional parameter 2")
def myfun(a):
    return "hi "+a;

print(myfun('Johnson'));