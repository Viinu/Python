n = int(input())
prod = 1
while(n!=0):
 prod = prod * (n % 10)
 n = n//10
print(prod)
