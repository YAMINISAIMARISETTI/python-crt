import re
p=r"[bcdfghjklmnpqrstvwxyz]"
if re.search(p,"ear"):
    print("matchy consonant")
else:
    print("not match")