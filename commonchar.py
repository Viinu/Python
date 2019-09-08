maximum_char = 26
def twoStrings(s1, s2) : 
    v = [0] * (maximum_char) 
    for i in range(len(s1)): 
        v[ord(s1[i]) - ord('a')] = True
    for i in range(len(s2)) : 
        if (v[ord(s2[i]) - ord('a')]) : 
            return True
    return False
if __name__ == "__main__": 
    str1,str2 = input().split() 
    if (twoStrings(str1, str2)): 
        print("yes") 
    else: 
        print("no")
