n=int(input())
temp,last,first,rev = 0,0,0,0
last = n % 10
while n > 0:
    temp= n%10
    rev = rev * 10 + temp
    n = int(n / 10)
first = rev % 10
print(first+last)
