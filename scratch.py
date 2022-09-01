def LongestWord(sen):
    wordList = []
    wordStart = 0
    for x in range(len(sen)):
        if not sen[x].isalpha() and not sen[x].isdigit():
            if len(sen[wordStart:x]) > 0:
                wordList.append(sen[wordStart:x])
            wordStart = x+1
    maxCount = 0
    maxindx = 0
    for x in range(len(wordList)):
        if len(wordList[x]) > maxCount:
            maxCount = len(wordList[x])
            maxindx = x
    # code goes here
    return wordList[maxindx]

# keep this function call here 
print(LongestWord(input()))