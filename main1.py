from functional import callable,callable2


def myprocess(p):
    print("Pre processing is being done")
    p()
    print("Post processing is being done");

myprocess(callable)

myprocess(callable2)
