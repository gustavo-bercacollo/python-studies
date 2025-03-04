# Python Exercise #032 - Leap Year

from datetime import date

year = int(input("\033[35mEnter a year to check if it is a leap year, or enter 0 to analyse the current year:\033[m "))

if year == 0:
    year = date.today().year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year!")
else:
    print(f"The year {year} is not a leap year.")
