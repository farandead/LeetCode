from collections import Counter
def intersection(nums):
    result = []
    for i in range(len(nums)):
        result.append(dict(Counter(nums[i])))
    common_elements = result[0].keys()
    for item in result[1:]:
        common_elements &= item.keys()
   return list(common_elements)


    


print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))