from collections import Counter
def findSpecialInteger(arr):
    c = Counter(arr)
    a = [i for i in c.keys() if c[i] == max(c.values())]
    return a[0] if a else -1  


print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))