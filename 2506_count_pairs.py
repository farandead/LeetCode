from collections import defaultdict
def similarPairs(words):
    sets_words = defaultdict(list)
    count = 0
    for word in words:
        word = tuple(set(sorted(word)))
        print(word)
        sets_words[word].append(1)
    for value in sets_words.values():
        count += len(value) * (len(value) - 1) // 2
    
    return count       


print(similarPairs(["dcedceadceceaeddcedc","dddcebcedcdbaeaaaeab","eecbeddbddeadcbbbdbb","decbcbebbddceacdeadd","ccbddbaedcadedbcaaae","dddcaadaceaedcdceedd","bbeddbcbbccddcaceeea","bdabacbbdadabbbddaea"]

))