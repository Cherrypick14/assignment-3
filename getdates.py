#    a program to get the dates of yesterday, today and tomorrow

import numpy as np

def get_dates():
    thursday = np.datetime64('2022-04-14')
    wednesday = np.datetime64(thursday)- np.timedelta64(1, 'D')
    friday = np.datetime64(wednesday) + np.timedelta64(2, 'D')
    return thursday,wednesday,friday

print(get_dates())