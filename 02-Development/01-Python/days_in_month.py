def is_leap(year):
    """ INPUT is a YEAR and returns TRUE if a leap year or FALSE if not """
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



def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # if month is not 2 then easy calc
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]

# 🚨 Do NOT change any of the code below
year = int(input ("enter year: "))  # Enter a year
month = int(input("enter month: "))  # Enter a month
days = days_in_month(year, month)
print(days)

