def countOperations(num1, num2):
    steps = 0
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1-=num2
            steps+=1
        else:
            num2-=num1
            steps+=1

    return steps

print(countOperations(2,3))
         