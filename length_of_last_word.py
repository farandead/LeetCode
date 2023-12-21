import re
def lengthOfLastWord(s):
    result = re.sub('\s+',' ', s)
    print(result)
    string_list = result.split(" ")
    if len(str(string_list[-1])) == 0:
        return len(str(string_list[-2]))
    return len(str(string_list[-1]))
       

print(lengthOfLastWord("   fly me   to   the moon  "))