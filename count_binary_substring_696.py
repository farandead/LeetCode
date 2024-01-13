def countBinarySubstrings(s):
    groups = [1]

    for i , curr in enumerate(s[1:]):
        previous = s[i]
        # print(f"Current: {curr}")
        # print(f"previous:{previous}")
        if curr == previous:
            groups[-1] += 1
            # print(groups)
            
        else:
            groups += [1]
    mins = []
    for i ,curr in enumerate(groups[1:]):
        prev = groups[i]
        # print(f"Current: {curr}")
        # print(f"previous:{prev}")
        mins += [(min(prev,curr))]
        # print(prev,i,curr,mins)
    # print(groups)
    # print(mins)
    return sum(groups)


print(countBinarySubstrings("00110011"))