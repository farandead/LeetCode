def separateDigits(nums) 
    new_array = []
    for i in range(len(nums)):
        if len(str(nums[i])) == 1:new_array.append(int(nums[i]))
        else:
            new_value = str(nums[i])
            for i in range(len(new_value)):new_array.append(int(new_value[i]))
    return new_array