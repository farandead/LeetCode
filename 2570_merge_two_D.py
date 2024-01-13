from collections import Counter
from collections import OrderedDict
def mergeArrays(nums1, nums2):
    result = []
    new_num =  Counter(dict(nums1)) + Counter(dict(nums2))
    new_num = dict(new_num)
    new_num = OrderedDict(sorted(new_num.items()))
    for item,value in new_num.items():
        result.append([item,value])
    return result





print(mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))


