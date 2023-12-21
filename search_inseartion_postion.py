def searchInsert(nums, target):
        for index, number in enumerate(nums):

            if number == target:
                return  index
            if number >= target:
                return index
            if index >= len(nums)-1:
                return index+1
        return index
        

print(searchInsert([1,3,5,6],7))       