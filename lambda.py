""" This .py file is for lambda function """
def x(a): return a+10
# print(x(5))


def y(a, b): return a*b
# print(y(5,6))


def z(a, b, c): return a+b+c
# print(z(1,2,3))


""" The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number: """


def myFunc(x):
    return lambda a: a*x


abc = myFunc(10)
print(abc(2))
