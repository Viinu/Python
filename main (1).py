import math
def square(l,m):
 product = l*m
 root = math.sqrt(product)
 if int(root + 0.5) ** 2 == product:
  print("yes")
 else:
  print("no")
square(5,5)