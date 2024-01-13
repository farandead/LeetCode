def findKthPositive(arr, k):
    missing_numbers= []
    i = 0
    while(len(missing_numbers) != k+1):
        if i not in arr and i == k:
            missing_numbers.append(i)
            print(i)
        i+=1
    return missing_numbers[-1]
print(findKthPositive([1,2,3,4],2))