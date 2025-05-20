def Leap_year_or_not(year):
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

inp_year = int(input("Enter the year: "))
if Leap_year_or_not(inp_year):
    print(f"{inp_year} is a leap year")
else:
    print(f"{inp_year} is not a leap year")
