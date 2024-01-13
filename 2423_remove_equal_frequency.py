from collections import Counter
def equalFrequency(word) :
    freq = Counter(word)
    for char in freq:
        print(freq[char])
        freq[char] -= 1
        
        # print(len(set(freq.values()) - {0}))
        print(freq.values() - {0})
        if len(set(freq.values()) - {0}) <= 1:
            return True
        freq[char] += 1 
    return False

print(equalFrequency("cccaa"))