''#for the leap year in the 400th year it should be divisible by four it should be a leap year and it should be divisible by 100
def is_leap(year):
    if (year % 4 == 0 and (year % 100 == 0 and (year % 400 == 0))):
        return True
    else:
        return False


year = int(input("Enter a year: "))
print(is_leap(year))