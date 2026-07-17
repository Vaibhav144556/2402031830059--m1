from datetime import date

live_date=date.today()

print("Current date with variable : ",live_date)
print("Current date without variable : ",date.today())

print("\nExtract all day month and year : ")

print("Day   : ",live_date.day)
print("month : ",live_date.month)
print("year  : ",live_date.year)

print("\nby formate changer(strftime) : ")

print("with variable : ",live_date.strftime("%d-%m-%Y"))
print(live_date.strftime("%d-%m-%Y"))