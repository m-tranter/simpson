from functools import reduce
import timeit
import math

def simpson(f, a, b, n):
    def integ(acc, i):
        k = a + i * h
        return acc + (h/6) * (f(k) + 4 * f(k + h/2) + f(k + h))
    h = (b - a) / n
    return reduce(integ, [x for x in range(n)], 0)

def s1(f, a, b, n):
    h = (b - a) / n
    integ = 0
    for i in range(n):
        k1 = a + i * h
        k2 = k1 + h/2
        k3 = k1 + h
        integ += (h/6)*(f(k1) + 4*f(k2) + f(k3))
    return integ


print("*** Simpson's rule ***")
a = 1
b = 200
n = 100000
print("cos, a = {0}, b = {1}, n = {2}".format(a, b, n))

for elem in [["for loop", s1], ["reduce", simpson]]:
    tic = timeit.default_timer()
    print("\nUsing {}.".format(elem[0]))
    print(elem[1](math.cos, a, b, n))
    print("{:.5f} seconds".format(timeit.default_timer() - tic))
