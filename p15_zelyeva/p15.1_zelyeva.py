while True:
    try:
        num = int(input("Введіть кількість рядків: "))
        if num <=0:
            num = int(input("Введіть число > 0: "))

        bin =[1]
        for i in range(num+1):
            print(*bin)
            nm = [1]
            nm +=[bin[k]+bin[k+1] for k in range(len(bin)-1)]+[1]
            bin = nm
    except ValueError:
        print('Невірне введення, спробуйте ще раз')
        continue
    break