import calendar
from datetime import datetime

def display_calendar(y):
    print(calendar.calendar(y))

def display_calendar_month(y, m):
    print(calendar.month(y, m ))

def display_calendar_datetime():
    now = datetime.now()
    print(calendar.month(now.year, now.month))

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
display_calendar_month(year, month)
display_calendar(year)
display_calendar_datetime()





