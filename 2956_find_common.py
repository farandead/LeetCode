def findIntersectionValues(nums1, nums2):
    count1,count2 = 0,0
    
    for item in nums1:
        if item in nums2:
            count1+=1
    for item in nums2:
        if item in nums1:
            count2+=1
    return [count1,count2]
    

print(findIntersectionValues([3,4,2,3],[1,5]))

        