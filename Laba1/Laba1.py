import random as r

def comprasion(a, b):   
    len_a = len(a) - 1
    len_b = len(b) - 1   
    if a[0] == b[0] or a[len_a] == b[len_b]:
        print(True)   
    else:
        print(False)

a = []
b = []
lenght_a = r.randint(1, 10)
lenght_b = r.randint(1, 10)
for i in range(0, lenght_a):    
    a.append(r.randint(1,10))
for i in range(0, lenght_b):
    b.append(r.randint(1,10))

comprasion(a, b)
print(f'{a}\n{b}')