num = int(input('k = '))
lst = []
for i in range (num):
 k = [int(x) for x in input().split()]
 lst.append(k)
arr = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        arr.append(lst[i][j])
arr.sort()
print(*arr)
