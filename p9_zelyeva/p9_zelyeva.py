import numpy as np
import itertools

z = True
while z:
    try:
        x = int(input("Введіть розмір квадратної матриці: "))
        if x > 0: # the size of the matrix cannot be less than zero


            def random_matrix(dim):
                """
                The function generates dim x dim array of integers
                between 0 and 10.
                """
                matrix = np.random.randint(10, size=(dim, dim))
                return matrix



            t = list(itertools.permutations('1234567890', x))
            A = random_matrix(x)
            print(A)
            i = 1
            j = 1


            def minor(A, i, j):
                # find minor
                for i in range(len(A) - 1):
                    for j in range(len(A) - 1):
                        if len(A[i]) > len(A[j]):
                            del A[j]
                        elif len(A[i]) < len(A[j]):
                            del A[i]


            def det_recursive(A):
                # функція використовує numpy для обчисленої матриці

                sol = 0
                if A.shape != (1, 1):
                    for i in range(A.shape[0]):
                        sol = sol + (-1) ** i * A[i, 0] * det_recursive(np.delete(np.delete(A, 0, axis=1), i, axis=0))
                    return sol
                else:
                    return A[0, 0]


            print(det_recursive(A))
            print(np.linalg.det(A))  # перевірка правильності роботи
        else:
            print('Невірний тип даних, спробуйте ще раз')
    except:
            print('Невірний тип даних, спробуйте ще раз')
            continue



