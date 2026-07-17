from dateutil.parser import parse

mydate="24-04-2003"
print("mydate : ",mydate)

print("\nnow convert mydate str into original type date using parse function.")
ori_date=parse(mydate)
print("original type date : ",ori_date)

print("\nnow change the formate using strftime function.")
print(ori_date.strftime("%d-%m-%Y"))
print(ori_date.strftime("%A-%B-%Y"))

