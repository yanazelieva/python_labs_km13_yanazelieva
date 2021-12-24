pages = int(input("Enter number of pages in the book (should be <= 1280): "))
while True:
    if pages >= 1280:
        print("Your number should be less ot equal to 1280 and more than 0!")
        pages = int(input("Enter number of pages in the book (should be <= 1280) : "))


    if pages < 1:
        print("Your number should be less ot equal to 1280!")
        pages = int(input("Enter number of pages in the book (should be > 0) : "))
    break

notebook = int(input("Enter number of pages in one notebook (should be 16, 24 or 32): "))
while True:
    if notebook not in [16, 24, 32]:
        print("Your number should be 16, 24 or 32!")
        pages = int(input("Enter number of pages in one notebook (should be 16, 24 or 32): "))
    break
parametr = int(input("Enter 0 or 1: "))
while True:
    if parametr not in [0, 1]:
        print("Your number should be either 1 or 0!")
        parametr = int(input("Enter 0 or 1: "))
    break
def decorator1(pages, notebook, parametr):
    def decorator(func):
        def wrapper(pages, notebook):
            result = func(pages, notebook)
            if parametr:
                print(result)
            else:
                for line in result:
                    for el in line:
                        print(el, end=' ')
                    print()
                print(f'Notebooks count = {pages // notebook}')
        return wrapper
    return decorator
@decorator1(pages, notebook, parametr)
def res(pages, notebook):
    notebooks = pages // notebook

    result = []
    for i in range(1, notebooks + 1):
        notebook_pages = []
        for j in range(0, notebook // 2, 2):
            notebook_pages.append((notebook - j) * i)
            notebook_pages.append((1 + j) + (i - 1) * notebook)
            notebook_pages.append((2 + j) + (i - 1) * notebook)
            notebook_pages.append((notebook - 1 - j) * i)
        result.append(notebook)
    return result
while pages % notebook != 0:
    print('Your number of pages in the book should be dividable by number of pages in one notebook!')
    pages = int(input('Enter new number of pages: '))

res(pages, notebook)