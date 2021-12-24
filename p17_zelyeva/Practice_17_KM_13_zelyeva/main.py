from factorial import factorial
from exp_root import exponent, root
from logarithm import logarithm

print('Select a program\nFirst program counts factorial of some number(1)\nSecond program count exponent and root'
      '(2 - exponent 2), (3 - exponent 3) (4 - root 2) (5 - root 3)'
      '\nThird program count logarithm(6 - logarithm with base)< (7 - natural logarithm), (8 - logarithm with base 10')
def chek1():
    val = input('Enter number: ')
    while type(val) != int:
        try:
            val = int(val)
            return int(val)
        except:
            val = input("Entered an incorrect value, try again,(you must enter a number  ")
    return int(val)
def chek2():
    val = input('Enter number: ')
    while type(val) != int:
        try:
            if int(val) <= 0 :
                val = "a"
            val = int(val)
            return int(val)
        except:
            val = input("Entered an incorrect value, try again,( you must keep a value > 0 ) :")
    return int(val)
def cheсk3():
    val = input('Enter number: ')
    while type(val) != int:
        try:
            if int(val) < 0 or int(val) == 1 :
                val = "a"
            val = int(val)
            return int(val)
        except:
            val = input("Entered an incorrect value, try again,")
    return int(val)
def choose():
    while True:
        x = int(input('Select program: '))
        if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8:
            break
        print('Please select program!')
    return x



if __name__ == '__main__':
    x = choose()
    if x == 1:
        factorial.fact(chek2())
    elif x == 2:
        exponent.exp2(chek1())
    elif x == 3:
        exponent.exp3(chek1())
    elif x == 4:
        root.root2(chek2())
    elif x == 5:
        root.root3(chek2())
    elif x == 6:
        logarithm.log(chek1(), cheсk3())
    elif x == 7:
        logarithm.ln(chek1())
    elif x == 8:
        logarithm.lg(chek1())