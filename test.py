from math import * 

def f(x):
    return 3*pow(x,2)

def f_res(y):
    return sqrt(y/3)

print(f(f_res(3)))