#currying

def curried_f(x, y = None, z = None):
    def f(x, y, z):
        return x ** 3 + y ** 2 + z

    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y, z)
    return lambda y, z = None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z))
    )

#print(curried_f(2, 3, 4))
g = curried_f(2)
h = g(3)
i = h(4)
print(i)

# #############################
import operator

def curry(func, var):
    y = var
    def f(x):
        return func(x, y)
    return f

if __name__ == '__main__':
    double = curry(operator.mul, 2)
    add = curry(operator.add, 7)
    a = double(6)
    b = add(2)
    print("Double 6: %i" %a)
    print("Add 7 to 2: %i" %b)


# out:
# 21
# Double 6: 12
# Add 7 to 2: 9