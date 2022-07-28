import re

txt = "book cupboard book rack section book page publisher author page cover"

x = re.findall("^book", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
