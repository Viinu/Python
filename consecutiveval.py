val = str(input())
a = max(map(len, val.split('0')))
if a==0:
    print("-1")
else:
    print(a)
