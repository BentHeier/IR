import random; random.seed(123)
import codecs
import string
import re
from nltk.stem.porter import PorterStemmer

f = codecs.open("pg3300.txt", "r", "utf-8")

docs = f.read()
docs = docs.split("\r\n\r\n")
words =[]
for i, e in reversed(list(enumerate(docs))):
    if("Gutenberg" in e):
        del docs[i]
    else:
        words.append(docs[i].split())
words.reverse()

for w in words:
    for i in range(0, len(w)):
        w[i] = w[i].translate(str.maketrans('','',string.punctuation+"\n\r\t"))
        w[i] = w[i].lower()

stemmer = PorterStemmer()
word = "Economics"
print(stemmer.stem(word.lower()))
