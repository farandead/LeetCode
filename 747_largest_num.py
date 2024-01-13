def dominantIndex(nums):
        max_num = max(nums)
        new
        for i in range(len(nums)):
            if max_num >= nums[i] * 2 :
                break
            elif max_num * 2 ==  nums[i] * 2:
                break
            else:
                flag = False
        return -1 if flag == False else nums.index(max_num)


print(dominantIndex([1,2,3,4]))