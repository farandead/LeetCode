def xorOperation( n, start) :
    array = []
    for i in range(n):
        array.append( start + 2 * i)
    result = 0
    for item in array:
        result ^= item
    return result

print(xorOperation(4,3))