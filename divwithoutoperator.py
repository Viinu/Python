a,b = input().split()
a = int(a)
b = int(b)
sign = -1 if ((a<0) ^ (b<0)) else 1
a = abs(a)
b = abs(b)
res = 0
while (a>=b):
    a -= b
    res += 1
print(sign*res)

