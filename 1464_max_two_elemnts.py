def maxProduct(nums):
    max_num = 0
    second_max = 0
    for i in range(len(nums)):
        if nums[i] > max_num :
            second_max = max_num
            max_num = nums[i]
    return (max_num-1) * (second_max-1)
        
print(maxProduct([3,4,5,2]))