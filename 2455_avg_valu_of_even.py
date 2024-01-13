def averageValue(nums):
    new_numbers = [item for item in nums if (item % 2 and item % 3) == 0]
    return int(sum(new_numbers)/len(new_numbers))

print(averageValue([1,3,6,10,12,15]))