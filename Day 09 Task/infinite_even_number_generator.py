def even_numbers():
    num = 2
    while True:
        yield num
        num += 2


g = even_numbers()

n = 30

for i in range(n):
    print(next(g))