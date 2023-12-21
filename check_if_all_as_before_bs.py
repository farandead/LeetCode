def checkString(s):
    string_nwe = ''.join(sorted(s))
    if string_nwe == s:
        return True
    else:
        return False
print(checkString("abab"))

