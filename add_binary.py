def addBinary( a, b):
    result = bin(a + b)
    return result[7:]
        

print(addBinary(1101,100))