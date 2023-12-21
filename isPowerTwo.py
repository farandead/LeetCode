def isPowerOfTwo(n):
    return (n and (not(n & (n - 1))) )


print(isPowerOfTwo(4))