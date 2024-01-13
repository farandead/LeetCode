from collections import Counter
def lemonadeChange(bills):

    spare_change = Counter()

    for item in bills:
        if item == 5:
            spare_change[5] += 1
        elif item == 10:
            if spare_change[5] > 0:
                spare_change[5] -= 1
                spare_change[10] += 1
            else:
                return False 
        else: 
            if spare_change[10] > 0 and spare_change[5] > 0:
                spare_change[10] -= 1
                spare_change[5] -= 1
            elif spare_change[5] >= 3:
                spare_change[5] -= 3
            else:
                return False

    return True
    

 
        

    


print(lemonadeChange([5,5,10,10,20]))