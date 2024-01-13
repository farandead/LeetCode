def minimizedStringLength(s):
    string_list = list(s)
    new_string_list = []
    for i in range(1,len(string_list)):
        previous = string_list[i-1]
        current = string_list[i]  
        if i == len(string_list)-1:
            new_string_list.append(string_list[-1])
        if previous != current:
            new_string_list.append(previous)
        else:
            string_list[i-1]  = "-"

    return new_string_list
        
print(minimizedStringLength("dddaaa"))
