import re

sentence = "There are 20 books and 30 novels"
patt  = r"\d+"

result = re.findall(patt,sentence)
print(result)