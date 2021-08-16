def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
fibo = list(fibonacci(10))
evenfibo = [x for x in fibo if x % 2 == 0]
print(evenfibo)