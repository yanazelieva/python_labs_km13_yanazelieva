print('ax²+bx+c=0')
try:
    a = input('Введіть значення a: ')
    b = input('Введіть значення b: ')
    c = input('Введіть значення c: ')
    a = float(a)
    b = float(b)
    c = float(c)
    dyscryminant = b ** 2 - 4 * a * c
    print('Дискримінант = ' + str(dyscryminant))

    if dyscryminant < 0 and a<0 and a>0:
            print('Коренів в дійсних числах немає!')
    elif dyscryminant == 0 and a<0 and a>0:
            try:
                x = -b / (2 * a)
                print('x = ' + str(x))
            except ZeroDivisionError:
                print("Помилка! Ділення на 0.")
    else:
            try:
                x1 = (-b + dyscryminant ** 0.5) / (2 * a)
                x2 = (-b - dyscryminant ** 0.5) / (2 * a)
                print('x₁ = ' + str(x1))
                print('x₂ = ' + str(x2))
            except ZeroDivisionError:
                print("Помилка, ділення на 0!")
except ValueError:
    print('Ви ввели неможливий тип даних!')

















