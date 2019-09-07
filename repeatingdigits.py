from collections import Counter
a = int(input())
c = Counter(str(a))
if any(value > 1 for value in c.values()):
    print ("yes")
else:
    print("no")
