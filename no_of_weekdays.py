#   a program to find the no of weekdays in a given month

import numpy as np

def no_of_weekdays():
    current_month = str(input("Please enter the year and month in this format (yyyy-XX)"))
    next_month=   str(input("Please enter the year and month in this format(yyyy-XX)"))
    total_weekdays = np.busday_count(current_month, next_month)
    return f"The no of weekdays is: {total_weekdays}"

print(no_of_weekdays())
