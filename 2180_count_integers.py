def countEven(num) :
    count = 0
    for i in range(1,num):
        
        if i % 2 == 0:
            print(i)
            count+=1
       
        
    return count

print(countEven(4))