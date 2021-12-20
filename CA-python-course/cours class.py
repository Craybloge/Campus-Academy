from carre import Carre as ca


c = ca(5)
print(c)
b=c.factor(2)
print(b)

d= b+c
print(d)

e= d-c
print(e)
print(int(c))
print(e<d)

print(c.counter)

with open("test.txt", 'r') as test:

    print(test.read())
