def choice(a):
    if a == 1:
        def math(a,b): print("{0} + {1} = {2}".format(a, b, a + b))
    else:
        def math(a,b): print("{0} - {1} = {2}".format(a, b, a - b))
    return math

f = choice(1)
f(5,5)


def add(a,b):
    c = a + b
    print("The answer is %d" %c)

def QA(Function):
    Function(7,8)

QA(add)