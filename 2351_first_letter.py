from collections import defaultdict
def repeatedCharacter(s):
    string_list = s
    dictionary_list = defaultdict(set)
    for i in range(0,len(string_list)):
        for j in range(i,len(string_list)):
            previous = string_list[i]
            current = string_list[j]  
            if previous != current:
                pass
            else:
                dictionary_list[previous].add(i)
                dictionary_list[previous].add(j)
                pass
    print(dictionary_list)
    return ""
print(repeatedCharacter("abccbaacz"))
        