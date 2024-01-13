from collections import Counter
def commonChars(words):
    counter_common = Counter(words[0])

    for word in words[0:]:
        word_counter=Counter(word)
        counter_common &= word_counter
    print(counter_common)
    result = []
    for char,value in counter_common.items():
        result += [char] * value

    print(result)


    
              

print(commonChars(["bella","label","roller"]))