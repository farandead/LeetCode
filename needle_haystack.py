def strStr(haystack, needle):
    pointer = needle[0]
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:len(needle)+i]== needle:
                return i
    return -1
            


print(strStr("adsadbut","sad"))