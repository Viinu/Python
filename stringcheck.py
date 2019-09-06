string=input()
str1=0
str2=0
for i in string:
    if i=="(":
        str1+=1
    if i==")":
    	str2+=1
if str1==str2:
	print("yes")
else:
	print("no")
