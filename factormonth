from calendar import monthrange
def factors(n):
    factor = []
    for i in range(1,n+1):
        if n%i == 0:
            factor.append(i)
    return factor
def month_conv(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month.strip()[:3]) + 1
month,year = input().split()
month = int(month_conv(month))
year = int(year)
temp , n = monthrange(year, month)
i,count = 0,0
for i in range(2,n+1):
    l = len(factors(i))
    if l <= 2:
        count += 1
print(count)
