
# coding: utf-8

# In[24]:

##Project Euler Problems

#Problem 19: Counting Sundays

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
start = [1, "Jan", 1901]
end = [31, "Dec", 2000]

def is_leapyr(year):
    if year % 4 > 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

def days_in_month(month, year = 1):
    thirtydays = ["Sep", "Apr", "Jun", "Nov"]
    if month is "Feb":
        if is_leapyr(year):
            return 29
        else:
            return 28
    elif month in thirtydays:
        return 30
    else:
        return 31
def diff_day(date1, date2):
    global MONTHS
    difference = 0
    cur_yr = date1[2]
    print (cur_yr)
    #Difference in years
    for year in range(date1[2] + 1, date2[2]):
        cur_yr += 1
        if is_leapyr(year):
            difference += 366
        else:
            difference += 365
    print (cur_yr)
    #Difference in Days
    difference += (days_in_month(date1[1], date1[2]) - date1[0]) + (date2[0])
    #Difference in Months
    for month1 in range(MONTHS.index(date1[1]) + 1, len(MONTHS)):
        difference += days_in_month(MONTHS[month1], date1[2])
    end_month = MONTHS.index(date2[1])
    for month2 in range(end_month):
        difference += days_in_month(MONTHS[month2], date2[2])
    return difference

new_list = []

for i in MONTHS:
    print (i, days_in_month(i))


# In[ ]:



