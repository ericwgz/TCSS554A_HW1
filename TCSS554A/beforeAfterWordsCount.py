from nltk.tokenize import  sent_tokenize
from nltk.tokenize import word_tokenize

# Count words in corpus before processing
corpusBeforeProcessing = word_tokenize(open('.\\dump.txt', encoding='utf-8').read())

wordsCountBefore = 0

for w in corpusBeforeProcessing:
    print(w)
    wordsCountBefore += 1

print('words before processing: ' + str(wordsCountBefore))

# Count words in corpus after processing
corpusAfterProcessing = word_tokenize(open('.\\result.txt', encoding='utf-8').read())

wordsCountAfter = 0

for w in corpusAfterProcessing:
    wordsCountAfter += 1

print('words after processing: ' + str(wordsCountAfter))

