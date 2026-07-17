import re 

string = "apple banana apple mengo banana apple cherry"
patt = r"\s"

result = re.split(patt,string)
print(result)

message = "hello World"

result = re.sub("hello World","Hello Python Programming",message)

print(result)