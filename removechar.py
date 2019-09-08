from collections import OrderedDict 
def removeDupWithoutOrder(string): 
 return "".join(set(string)) 
def removeDupWithOrder(string): 
 return "".join(OrderedDict.fromkeys(string))
if __name__ == "__main__": 
 string = str(input())
print (removeDupWithoutOrder(string)) 
