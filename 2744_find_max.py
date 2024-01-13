def maximumNumberOfStringPairs(words):
    number_of_pairs = 0

    for i in range(len(words)):
        for j in range(len(words)):
            print(words[i])
            if words[i] == reversed(words[j]):
                print(reversed(words[j]))
                print('Found')


print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))
