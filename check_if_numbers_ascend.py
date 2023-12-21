def areNumbersAscending( s):
    new_list = s.split(" ")
    intenger_list = []
    for i in range(len(new_list)):
        try:
            if isinstance(int(new_list[i]),int):
                intenger_list.append(int(new_list[i]))
        except:
            pass
    return all(intenger_list[i-1] < intenger_list[i] for i in range(1, len(intenger_list)))


print(areNumbersAscending('sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s'))