def arrangeCoins(n):
    if n == 1:
        return 1
    reminder = n 
    for i in range(1,n+1):
        n = n-i  
        print(i)
        # print(n)
        if n < 0 : return i-1


print(arrangeCoins(8))