def findMiddleIndex(nums):
    total_sum = sum(nums)
    right_sum = 0
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        print(left_sum,right_sum)
        if right_sum == left_sum:
            return i
        left_sum = left_sum + nums[i]

    return -1


print(findMiddleIndex([2,3,-1,8,4]))
