def sides(a, b, c):   
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True         
a = 3
b = 4
c = 5
if sides(a, b, c): 
    print("yes")  
else: 
    print("no")
