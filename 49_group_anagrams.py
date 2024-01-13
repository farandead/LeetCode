from collections import defaultdict
def groupAnagrams(strs):
    groupAnagrams = defaultdict(list)
    for s in strs:
        sorted_s = tuple(sorted(s))
        groupAnagrams[sorted_s].append(s)
    return [value for value in groupAnagrams.values()]


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))