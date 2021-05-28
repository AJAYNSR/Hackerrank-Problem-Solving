year = int(input("enter the year:\n"))
if((year%400 == 0) or ((year%100 != 0) and (year%4 == 0))):
    print(year,"is leap year")
else:
    print(year, "not a leap year")