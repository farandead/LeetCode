def longestCommonPrefix(strs):

    current_prefix = ""

    for string in strs:

        for i in range(len(string)):

            if string[i] != string[0][]