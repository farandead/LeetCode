from collections import Counter
def frequencySort(nums):
    dictonary_list = Counter(nums)
    new_list = []
    dictonary_list = dict(sorted(dictonary_list.items(), key=lambda x:x[1]))
    for key,value in dictonary_list.items():
        for i in range(value):
            new_list.append(key)
    return new_list

print(frequencySort([1,1,2,2,2,3]))