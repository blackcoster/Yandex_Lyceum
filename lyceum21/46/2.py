def leap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(True)
    else:
        print(False)
# leap(2024)