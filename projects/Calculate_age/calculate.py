# -*- coding: utf-8 -*-
import time
from calendar import isleap

# Judge if it's a leap year
def judge_leap_year(year):
    return isleap(year)

# Return number of days in a month
def month_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if judge_leap_year(year) else 28

# Input
name = input("Input your name: ")
try:
    age = int(input("Input your age in years: "))
except ValueError:
    print("Invalid age input.")
    exit()

# Get current date
localtime = time.localtime()
current_year = localtime.tm_year
current_month = localtime.tm_mon
current_day = localtime.tm_mday

# Calculate birth year
birth_year = current_year - age

# Total months
total_months = age * 12 + current_month

# Total days
total_days = 0

# Add full years' days
for year in range(birth_year, current_year):
    total_days += 366 if judge_leap_year(year) else 365

# Add months of current year
for month in range(1, current_month):
    total_days += month_days(month, current_year)

# Add current month days
total_days += current_day

# Output
print(f"{name}'s age is {age} years or {total_months} months or {total_days} days.")
