import random; random.seed(123)
import codecs
import string
import re
from nltk.stem.porter import PorterStemmer
import gensim

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
dictionary = gensim.corpora.Dictionary(words)

s = codecs.open('common-english-words.txt', "r", "utf-8")
stopwords = s.read().split(',')
stop_ids = []

for stopword in stopwords:
    #stops at the last characther
    if stopword == '\n':
        break
    try:
        stopword_id = dictionary.token2id[stopword]
        stop_ids.append(stopword_id)
        dictionary.filter_tokens(stop_ids)
        #skips stopwords not in dictionary
    except KeyError:
        pass

corpus = [dictionary.doc2bow(text) for text in words]

tfidf_model = gensim.models.TfidfModel(corpus)
tfidf_corpus = tfidf_model[corpus]

index = gensim.similarities.MatrixSimilarity(corpus)
lsi_model = gensim.models.LsiModel(corpus, id2word=dictionary, num_topics=2)
lsi_index = gensim.similarities.MatrixSimilarity(lsi_model[corpus])


query_text = "What is the function of money?"
query_text.lower().translate(str.maketrans('','',string.punctuation+"\n\r\t"))
query = query_text.split()
query = dictionary.doc2bow(query)
query_index = tfidf_model[query]
doc2similarity = enumerate(index[query])
results = sorted(doc2similarity, key=lambda kv: -kv[1])[:3]

print("Results for the TF-IDF:\n")
for r in results:
    print(docs[r[0]])

lsi_query = lsi_model[query]
doc2similarity = enumerate(lsi_index[lsi_query])
lsi_results = ( sorted(doc2similarity, key=lambda kv: -kv[1])[:3] )
print("\nResults for LSI")
for r in lsi_results:
    print(docs[r[0]])
