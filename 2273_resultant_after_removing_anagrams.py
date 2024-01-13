from collections import defaultdict
def removeAnagrams(words):
    defaultAnagram = defaultdict(list)
    for s in words:
        sorted_s = tuple(sorted(s))
        defaultAnagram[sorted_s].append(s)
    return [item[0] for item in defaultAnagram.values()]

print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))

def modifyString(s):
    # Convert the string into a list of characters for easy manipulation
    chars = list(s)

    for i in range(len(chars)):
        if chars[i] == '?':
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                # Check if the chosen letter is different from the previous and next characters
                if (i == 0 or ch != chars[i - 1]) and (i == len(chars) - 1 or ch != chars[i + 1]):
                    chars[i] = ch
                    break

    return "".join(chars)
