def removeDuplicates(s):
                                                   #   Ex: azxxzy
        stack = []                                                #   ch    stack      stack.pop()
        for ch in s:                                    #  ––––   –––––––––  ––––––––––
            if stack and stack[-1]==ch: stack.pop()     #    a     [a]          
            else: stack.append(ch)                      #    z     [a,z]                                      #    x     [a,z,x]
        return ''.join(stack) 

print(removeDuplicates("abbaca"))

            
    

    