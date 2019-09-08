def countwords(string, word): 
    a = string.split(" ") 
    count = 0
    for i in range(0, len(a)): 
        if (word == a[i]): 
           count = count + 1
    return count        
string = input()
word = input()
print(countwords(string, word))
