def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            isIncreasing = False
        if nums[i] < nums[i + 1]:
            isDecreasing = False
        return isIncreasing or isDecreasing


print(isMonotonic([1,2,2,3]))