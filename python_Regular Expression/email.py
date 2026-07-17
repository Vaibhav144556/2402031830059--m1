import re

text = "999999999999"

emails = re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}', text)
print(emails)  # Output: 