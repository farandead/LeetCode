
chardict = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "j": "6"
    }
def isSumEqual(firstWord, secondWord, targetWord):
    firstWord = "".join([chardict.get(item) for item in firstWord])
    secondWord = "".join([chardict.get(item) for item in secondWord])
    targetWord  = "".join([chardict.get(item) for item in targetWord ])
  
    if int(firstWord) + int(secondWord) == int(targetWord):
        return True
    else:
        return False

print(isSumEqual("acb","cba","cdb"))