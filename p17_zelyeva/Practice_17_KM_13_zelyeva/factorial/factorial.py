def fact(n):
    factorial = 1

    for i in range(2, n + 1):
        factorial *= i

    print(f'The factorial {n} is ', factorial)
