def merge(nums1,m,nums2,n):
    # nums1,nums2, = nums1[0:m],nums2[0:n]
    for j in range(n):
        nums1[m+j] = nums2[j]
        
    print(nums1.sort())
    return nums1.sort()



print(merge([1,2,3,0,0,0],3,[2,5,6],3))



