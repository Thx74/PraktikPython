import random as r

def generator(x, a, b):
    for i in range(x):
        yield r.randint(a, b)

x = 0
a = r.randint(0, 10) #MinNum
b = r.randint(10, 20)#MaxNum
result = list(generator(x, a, b))
print(f"mass: {result}\nx = {x}\na = {a}\nb = {b}")