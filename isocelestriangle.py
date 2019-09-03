a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a==b==c):
 print("no")
elif(a==b or b==a or c==a):
 print("no")
else:
 print("yes")
