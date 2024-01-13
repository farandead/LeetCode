def maximumProduct(nums):
    nums = sorted(nums)
    nums1 = nums[-1]
    nums2 = 0
    nums3 = 0
    for i in range(0,len(nums)-1):
        num2 = max(nums[i],nums2[i+1])





print(maximumProduct([-100,-98,-1,2,3,4])) 