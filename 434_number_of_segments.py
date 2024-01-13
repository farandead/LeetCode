def countSegments(s):
    s = s.split(" ")
    count = 0

    spaces = [True if item == "" else False for item in s]
    count_spaces = spaces.count(True)
    print(count_spaces)
    if all(spaces) == True: return 0
    if len(s) == 0 : return 0
    return len(s)-count_spaces


print(countSegments(", , , ,        a, eaefa"))
