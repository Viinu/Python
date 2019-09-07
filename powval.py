inp = input()
lists = list(map(int, str(inp)))
output = 0
for lis in lists:
    output = output + pow(lis,len(inp))
print(output)
