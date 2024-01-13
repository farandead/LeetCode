def stringMatching(words):
    result = []
    for i in range(len(words)):
        key = words[i]
        for j in range(len(words)):
            value = words[j]
            if key in value and key != value:
                if key not in result:
                    result.append(key)
    return result

print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))