def maximumValue(strs):
    max_value = 0
    i = 0
    while i <= len(strs)-1 :
        try:
            if type(int(strs[i])) == int and max_value <= int(strs[i]):
                max_value = int(strs[i])
                
        except:
            if type((strs[i])) == int and max_value <= int(strs[i]):
                max_value = int(strs[i])
                
        if type(strs[i]) == str and max_value <= len(str(strs[i])):
            print("goes here 2")
            try:
                if int(strs[i]) + 1:
                  pass
            except:
                print("goes here 3")
                max_value = len(str(strs[i]))
              
        i+=1           
    return max_value

print(maximumValue(["iw1","61939","7","7i","cye","bv7yg","t3ye6","990"]))