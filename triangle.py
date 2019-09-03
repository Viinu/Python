def sides(a, b, c):   
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True         
a = int(input())
b = int(input())
c = int(input())
if sides(a, b, c): 
    print("yes")  
else: 
    print("no")
