sub_string = str(input())
index=[x for x,y in enumerate(list(sub_string)) if(y.isupper())] 
camel_=[]
temp=0
for m in index:
    camel_.append(sub_string[temp:m])
    temp=m
if(len(index)>0):
    camel_.append(sub_string[index[-1]::])
    print('yes')
else:
    camel_.append(sub_string)
    print('no')
