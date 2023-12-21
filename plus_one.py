def plusOne(digits):
    list1 = []
    digits = int("".join(str(e) for e in digits)) + 1 
    return [int(digit) for digit in str(digits)]

print(plusOne([1,2,3]))