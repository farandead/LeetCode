import math
def isPerfectSquare(num):
    result = math.sqrt(num)
    return result % 1 == 0



print(isPerfectSquare(16))