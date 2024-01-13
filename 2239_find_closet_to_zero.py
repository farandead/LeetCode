def findClosestNumber(nums):
    value = [abs(item) for item in nums]
    print(abs(-1)) 
    return value if value in nums else -value

print(findClosestNumber([2,-1,1]))
