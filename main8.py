from decorators import classy,classyargs

@classy
def logical():
    print("called me")

logical()
print("------------------------------------")
@classyargs('one','two')
def logical2(a):
    print(a,' inside function')

logical2('DEC TST')

