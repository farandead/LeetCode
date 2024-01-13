def containsDuplicate(nums):
    nums = sorted(nums)
    nums_set = set(nums)
    nums_array = sorted(list(nums_set))
    return nums != nums_array



print(containsDuplicate([3,1]))