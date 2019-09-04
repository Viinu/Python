n = int(input())
l = [int(x) for x in input().split()]
m = sum(l)
if(m%2==0 and m%3==0 and m%5==0):
 print("1")
else:
 print("0")
