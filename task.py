import math


def firstrun():
    return 'success'


def c_area(radius):
    return (radius * radius) * 3.14


def get_firstlast(list_):
    return [list_[0]] + [list_[-1]]


def get_date_distance(date1, date2):  # mm/dd/yyyy
    months = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
              '11': 30, '12': 31, '01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31,
              '09': 30}

    def helper(num):
        if num == 0:
            return 0
        return months[str(num)] + helper(num - 1)

    days2 = int(date2[6:10]) * 365 + int(date2[3:5]) + helper(int(date2[0:2])-1) + math.floor(int(date2[6:10])//4)
    # making sure to count leap years
    days1 = int(date1[6:10]) * 365 + int(date1[3:5]) + helper(int(date1[0:2])-1) + math.floor(int(date1[6:10])//4)
    return days2 - days1
