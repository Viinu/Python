def binary_search(l, num_find):
    start = 0
    end = len(l) - 1
    mid = (start + end) // 2
    found = False
    position = -1
    while start <= end:
        if l[mid] == num_find:
            found = True
            position = mid
            break       
        if num_find > l[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2  
    return (found, position)
if __name__=='__main__': 
    n,num = input().split()
    n = int(n)
    num = int(num)
    l = [int(x) for x in input().split()]
    found = binary_search(l, num)
    if found[0]:
        print('yes')
    else:
        print('no')
