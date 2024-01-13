def findWords(words):
    set1= set("qwertyuiop")
    set2= set("asdfghjkl")
    set3= set("zxcvbnm")
    result = []
    for word in words:
        word_set = set(word.lower())

        if word_set <= set1 or word_set <= set2 or word_set <= set3:
            result.append(word)

    return result

print(findWords(["Hello","Alaska","Dad","Peace"]))
