arr = input()
l=[]
for i in arr:
    l.append(i)
for i in range(0,len(arr)-1,2):
    l[i],l[i+1] = l[i+1],l[i]
for i in l:
    print(i,end="")
