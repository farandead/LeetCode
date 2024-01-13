def findDisappearedNumbers(nums):
    set_nums = set(nums)
    result = []
    for item in range(1,len(nums)+1):
        if item not in set_nums:
            result.append(item)

    # result = [item for item in range(1,len(nums)) if item not in nums]
    return result


     
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))