import operator as op

class Solution(object):
    def removeElement(self, nums, val):
        count = op.countOf(nums, val)
        new_List = [] 
        for i in range(len(nums)):
            if nums[i] != val:
                new_List.append(nums[i])
        
        nums[:] = new_List
       
        return nums
        

sol = Solution()

print(sol.removeElement([0,1,2,2,3,0,4,2],2))
