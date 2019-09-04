def gcd(a, b): 
    if (a == 0 or b == 0):
     return 0
    if (a == b): 
     return a 
    if (a > b):  
     return gcd(a - b, b) 
     return gcd(a, b - a) 
def coprime(a, b): 
    if (gcd(a, b) == 1): 
        print("0") 
    else: 
        print("1")      
a,b = input().split()
a = int(a)
b = int(b)
coprime(a, b)
