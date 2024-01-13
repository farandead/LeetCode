def findNonMinOrMax(nums):
    max_num = max(nums)
    min_num = min(nums)
    answer = 0
    for i in range(len(nums)):
        if nums[i] != max_num and nums[i] != min_num:
            answer = nums[i]
    if answer == 0:
        return -1
    else:
        return answer
print(findNonMinOrMax([3,2,1,4]))
        