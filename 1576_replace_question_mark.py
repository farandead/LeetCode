from collections import Counter
from collections import defaultdict
import string
import random
def modifyString(s) :
    default_counter = defaultdict(list)
    changes = {}
    result = []
    for i in range(len(s)):
        default_counter[i].append(s[i])
    for index,value in default_counter.items():
        if value == ['?']:
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                # print(default_counter[index+1])
                print(default_counter[index-1][0])
                if (index == 0 or ch != default_counter[index-1][0]) and (index == len(s) - 1 or ch != default_counter[index+1][0]):
                    changes[index] = ch
                    
            
            default_counter[index].append(value)
            default_counter[index].remove('?')
    for index, char in changes.items():
        default_counter[index][0] = char
        
    for index,value in default_counter.items():
        result.append(value[0])

    
    return "".join(result)
def modifyString(s):
    string_list = list(s)
    for i in range(len(string_list)):
        if string_list[i] == '?':
            for char in 'abcdefghijklmnopqrstuvwxyz':
               if((i == 0 or char != string_list[i-1]) and (i == len(string_list) - 1 or char != string_list[i+1])):
                string_list[i] = char
    return "".join(string_list)
print(modifyString("j?qg??b"))



