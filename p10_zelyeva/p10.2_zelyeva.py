import numpy as np
years = np.arange(1900, 2020+1, 1)
def leap_year_check(i):
    i = years[i]
    if (i % 400 == 0):
        return True
    else:
        if (i % 100 == 0):
            return False
        else:
            if (i % 4 == 0):
                return True
            else:
                return False

def list_add(i):
    b = int(years[i])
    return b

def check_leap_of_year(years):
    l = range(0,len(years))
    k = list(filter(leap_year_check,l))
    p = list(map(list_add,k))
    return p

def check_count_day_of_month(function,month,year):
    function = function(years)
    if month == 2:
        if function.count(year) > 0:
            return 29
        else:
            return 28
    elif month % 2 == 0:
        return 31
    else:
        return 30
print("Among these years: \n", years)
y = check_leap_of_year(years)
print("Leap years:\n", y)
lsd = int(input("Enter your month: "))
year = int(input("Enter your year (1900-2020): "))
z = check_count_day_of_month(check_leap_of_year, lsd, year)
print("\nNumber of days on ", lsd, " month - ", z, " days")