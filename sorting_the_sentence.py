def sortSentence(s):
    newList = s.split(" ")
    dict_sentence = {
         
    }
    new_sentence = ""
    for i in range(len(newList)):
       dict_sentence[newList[i][-1]] =newList[i][:-1]
    # print(dict_sentence)
    for i in range(len(dict_sentence)):
       if dict_sentence.get(str(i+1)):
            new_sentence = new_sentence + str(dict_sentence.get(str(i+1)))+ " "
    print(new_sentence)



print(sortSentence('is2 sentence4 This1 a3'))