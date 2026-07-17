import re

name = "dog:bark cat:meow"
patt = r"dog:\w+"

result = re.search(patt,name)
print(result)
if result is None:
	print("Not available in sentence")
else:
	print("available in sentence")
