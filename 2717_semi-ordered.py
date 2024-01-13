def semiOrderedPermutation(nums):
    count = 0
    n = len(nums)
    while not (nums[0] == 1 and nums[-1] == n):
        for i in range(n - 1):
            if nums[i+1] < nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]  # Swap adjacent elements
                count += 1
    return count
    
print(semiOrderedPermutation([3,2,4,1]))