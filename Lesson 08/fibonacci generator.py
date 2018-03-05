# The generator fibonacci function
def fibonacci(limit):
    a = 0
    b = 1
    s = a + b
    for n in range(limit):
        yield a
        a = b
        b = s
        s = a + b


for number in fibonacci(100):
    print(number)
