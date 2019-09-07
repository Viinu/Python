import re
inp = str(input())
val = sum(map(ord,re.findall(r"([aieou])",inp, flags=re.I)))
if val%8 == 0:
    print("1")
else:
    print("0")
