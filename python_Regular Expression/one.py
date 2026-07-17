import re

name = input("Enter your name:")
# patt = "^[a-zA-Z]{2,}$"
# patt = "^a...h$"
# patt = "^me+t$"
# patt = "^me*$"
# patt = "^me?$"

result = re.match(patt,name)

if result is None:
	print("Missmatched characters")
else:
	print("Your name is:",name)