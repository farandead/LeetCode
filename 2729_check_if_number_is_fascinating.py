import re
def isFascinating(n):
    result = []
    for i in range(1,4):
        result.append(i*n)
    s = str(result)
    if "0" in s:
        return False
    digit_count = {str(digit): s.count(str(digit)) for digit in range(1, 10)}
    return all(count == 1 for count in digit_count.values())


print(isFascinating(783))