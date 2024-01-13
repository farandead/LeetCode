def reverseStr(s, k):
    pointer = 0
    new_string = ''
    while pointer < len(s):
        new_string += s[pointer:pointer + k][::-1]
        new_string += s[pointer + k:pointer + (2*k)]
        pointer += k + k
    return new_string





print(reverseStr("Hello032",2))