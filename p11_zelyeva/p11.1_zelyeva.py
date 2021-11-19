def cons(head, tail=[]):
    tail.insert(0, head)
    return  tail

# Перевірка
l = cons(3,
        cons(2,
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

#Друга частина завдання
def sum(lst):
    if not lst:
        return 0
    return lst[0] + sum(lst[1:])

# Перевірка
print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')
