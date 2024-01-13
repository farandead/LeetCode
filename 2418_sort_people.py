def sortPeople(names, heights):
    dictionary_values = {}
    for i in range(len(names)):
        dictionary_values.update({heights[i]:names[i]})
    dictionary_values = dict(sorted(dictionary_values.items(),reverse=True))
    return [item for item in dictionary_values.values()]
    


print(sortPeople(["Mary","John","Emma"],[180,165,170]))