import re
n = input()
numbers = re.findall('\d+',n)
numbers = map(int,numbers)
print(max(numbers))
