def foo(x):
    def fvv(y):
        return x*y
    return fvv

g = foo(3)(5)

print(g)
a=1
b = ++a
print(b)
a+=5
print(a)

