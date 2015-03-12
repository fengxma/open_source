def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        # print(a)
        a, b = b, a + b

for n in fib(10):
    print(n, end=' ')

print(list(fib(10)))