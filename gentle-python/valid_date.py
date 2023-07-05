# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:26:43 2023

@author: Kuba

Write an isValidDate() function with parameters year, month, and day. The function
should return True if the integers provided for these parameters represent a valid date.
Otherwise, the function returns False. 
Months are represented by the integers 1 (for January) to 12 (for December)
and days are represented by integers 1 up to 28, 29, 30, or 31 depending on the month and year.
Your solution should import your leapyear.py program from Exercise #20 for its
isLeapYear() function, as February 29th is a valid date on leap years.
September, April, June, and November have 30 days. The rest have 31, except February which
has 28 days. On leap years, February has 29 days.
"""

import leap_year

months_31 = [1,3,5,7,8,10,12]
months_30 = [4,6,9,11]

def isValidDate(year,month,day):
    
    if month > 12:
        return False
    elif month == 0 or day == 0:
        return False
    elif day > 31:                                   
        return False        # dzien 32 i w gore
    elif day == 31 and month not in months_31:    
        return False        # dzien 31 w miesiac 30dniowy
    elif day in [29,30] and month == 2 and not leap_year.isLeapYear(year):
        return False        # 29 lutego nieprzestepny   

    else:
        return True





assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay