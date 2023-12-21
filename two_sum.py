
  

def twoSum(nums, target):
    indexs = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                indexs.append(i),indexs.append(j)
                return indexs


print(twoSum([3,3],6))


