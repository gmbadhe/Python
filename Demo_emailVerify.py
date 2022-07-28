import re

#pattern =r"(^[a-zA-Z0-9_.+-]+@[@a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+$)"

pattern=r"(^[a-zA-Z40]+$)"
email="testemail@gmail.com"

print(re.match(pattern,email))
