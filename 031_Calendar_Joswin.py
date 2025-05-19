import calendar

def get_month(year, month):
    return calendar.month(year, month)

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

print(get_month(year, month))