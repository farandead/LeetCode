def createTargetArray(nums,index):
    new_array = []
    for i in range(len(nums)):
        new_array.insert(index[i], nums[i])
    return new_array
        

print(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))