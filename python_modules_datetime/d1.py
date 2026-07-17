from datetime import date

current_date = date.today()
print(current_date)

print(f"Current Year:{current_date.year}")
print(f"Current Month:{current_date.month}")
print(f"Current Day:{current_date.day}")


# format conversion
dmy = current_date.strftime("%d-%m-%Y")
print(dmy)