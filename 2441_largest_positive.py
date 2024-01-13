def findMaxK(nums):
    max_num = 0
    found = False
    for i in range(len(nums)):
        if nums[i] > max_num and -(nums[i]) in nums:
            max_num = nums[i]
            found = True
    if found:
        return max_num
    else:
        return -1

        
print(findMaxK([-10,8,6,7,-2,-3]))