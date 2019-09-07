a,b = input().split()
c,d = input().split()
e,f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
m = a*(d-f) + c*(f-b) + e*(b-d) 
if (m==0):
    print("yes")
else:
    print("no")
