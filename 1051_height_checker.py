def heightChecker( heights):
    sorted_heights = sorted(heights)
    count = 0
    for i in range(heights):
        if sorted_heights[i] != heights[i]:
            count+=1
    return count