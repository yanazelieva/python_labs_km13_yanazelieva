a = ('diamonds', 'clubs', 'hearts', 'spades')
b = ('A', *range(2, 11), 'J', 'Q', 'K')
def generator():
    for i in range(len(a)):
        for j in range(len(b)):
            yield f'{b[j]} {a[i]}'

y = generator()
while True:
    print(next(y))
    print(' ')