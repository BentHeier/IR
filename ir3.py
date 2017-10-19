import random; random.seed(123)
import codecs
import string
import re

f = codecs.open("pg3300.txt", "r", "utf-8")

docs = f.read()
docs = docs.split("\r\n\r\n")

for i, e in reversed(list(enumerate(docs))):
    if("Gutenberg" in e):
        del docs[i]

print(docs[0])
