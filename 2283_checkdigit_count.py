import re
def digitCount(num):
    for i in range(len(num)):
        if len(re.findall(str(i), num)) == int(num[i]):
            pass
        else:
            return False
    return True



print(digitCount("030"))