import re
str1=" she sells sea shells at sea shore"
p1 = "sells"
if re.search(p1,str1):
    print("match found")
else:
    print(p1,"not present in string")