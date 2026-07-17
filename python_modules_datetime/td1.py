from datetime import date,timedelta

cdate = date.today()
past_7days = cdate + timedelta(weeks=1)
print(cdate)
print(past_7days)