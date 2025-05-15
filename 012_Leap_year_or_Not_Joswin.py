def leap_year_or_not(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
y = int(input("Enter the year : "))
print(leap_year_or_not(y))