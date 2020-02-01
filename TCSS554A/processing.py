from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem.snowball import SnowballStemmer
import glob

read_files = glob.glob(".\\transcripts\\transcripts\\*.txt")

# Combine all corpus to single txt file and change characters to lower case
with open("dump.txt", "wb") as outfile:
    for txtfile in read_files:
        with open(txtfile, "rb") as infile:
            outfile.write(infile.read().lower())


f = open('.\\dump.txt', encoding='utf-8')

# remove special characters in sentences
tokenizer = RegexpTokenizer(r'\w+')

word_tokens = tokenizer.tokenize(f.read())

f.close()

# remove stopwords from sentences
stop_words = set(stopwords.words('english'))

filtered_sentence = [w for w in word_tokens if not w in stop_words]

# stemming each word to the root
stemmer = SnowballStemmer("english")

stemmed_sentence = [stemmer.stem(w) for w in filtered_sentence]

f = open('.\\result.txt', 'w', encoding='utf-8')
f.write(TreebankWordDetokenizer().detokenize(stemmed_sentence))