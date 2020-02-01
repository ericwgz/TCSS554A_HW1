from nltk.tokenize import word_tokenize
from collections import Counter
onceCount = 0
uniqueWordCount = 0
wordSet = set()
occurMoreThanOnce = set()
f = open('.\\result.txt', 'r', encoding='utf-8')
words = word_tokenize(f.read())
for word in words:
    # print(word)
    if word in wordSet:
        if(word in occurMoreThanOnce):
            continue
        else:
            onceCount -= 1
            occurMoreThanOnce.add(word)
    else:
        onceCount += 1
        uniqueWordCount += 1
        wordSet.add(word)
print('words occur only once:' + str(onceCount))
print('unique word:' + str(uniqueWordCount))