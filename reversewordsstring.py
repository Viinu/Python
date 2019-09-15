s = input()[::-1]
words = s.split(' ') 
string =[] 
for word in words: 
    string.insert(0, word)  
print(*string,sep=' ')
