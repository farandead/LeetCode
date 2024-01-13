import math
def subtractProductAndSum(n) :
    str_n = str(n)
    string_list = list(str_n)
    string_list = [int(item) for item in string_list] 
    return math.prod(string_list) - sum(string_list)

print(subtractProductAndSum(234))