import re

def isValid( s):
    parenthesis = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        } 
    for i in range(len(s)):
        value = parenthesis.get(s[i])
     
        if value in s :
            return True
        else:
            return False

print(isValid("()[]{}"))
