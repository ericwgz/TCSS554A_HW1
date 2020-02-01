from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import glob
import math

tokenizer = RegexpTokenizer(r'\w+')

stemmer = SnowballStemmer("english")

# Top 30 term frequence & tf (norm)

f = open('.\\result.txt', encoding='utf-8')
word_tokens = f.read().split()
cnt = Counter(word_tokens)
res = cnt.most_common()[:30]
print(res)

for entry in res:
    print(str(entry[0]) + ' : ' + str(math.log(entry[1], 10) + 1))

# Top 30 document frequence & idf
dict = {}
for entries in cnt.most_common()[:30]:
    dict[entries[0]] = 0
read_files = glob.glob(".\\transcripts\\transcripts\\*.txt")
for txtfile in read_files:
    with open(txtfile, "r") as infile:
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in tokenizer.tokenize(infile.read().lower()) if not w in stop_words]
        stemmed_sentence = [stemmer.stem(w) for w in filtered_sentence]
        for key in dict:
            if key in stemmed_sentence:
                dict[key] = dict[key] + 1
print(dict)
for key in dict:
    print(str(key) + ' idf : ' + str(math.log(404/dict[key], 10)))

# Top 30 tf(norm) * idf
for entry in res:
    print(str(entry[0]) + ' tf(norm) * idf: ' + str((math.log(entry[1], 10) + 1) * math.log(404/dict[key], 10)))

# top 30 P = tf / N
for entry in res:
    print(str(entry[0]) + ' P: ' + str(entry[1] / 109360* 100) )