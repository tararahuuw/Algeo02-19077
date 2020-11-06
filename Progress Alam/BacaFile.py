from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

REGEX = re.compile(r"\s")
def tokenize(text):
    return [tok.strip().lower() for tok in REGEX.split(text)]

file = open("Document1.txt","r");
raw1 = file.read()
print("Load File")
print(raw1)
print("")

tandabaca = [".",",","-","%", ")", "("]
for td in tandabaca:
    if (td == '-'):
        raw1=raw1.replace(td," ")
    else:
        raw1=raw1.replace(td,"")
        
print ("Remove tanda baca")
print(raw1)
print("")
 
for i in raw1:
    raw1 = raw1.lower()
print("lowercase")
print(raw1)
print("")
    
for i in raw1:
    raw1  = stemmer.stem(raw1)

print("stemming")
print(raw1)
print("")

for i in raw1 :
    raw1 = stopword.remove(raw1)

print("Stopword")
print(raw1)
print("")
file = open("Document2.txt","r");
raw2 = file.read()
print("Load File")
print(raw2)
print("")

tandabaca = [".",",","-","%", ")", "("]
for td in tandabaca:
    if (td == '-'):
        raw2=raw2.replace(td," ")
    else:
        raw2=raw2.replace(td,"")
        
print ("Remove tanda baca")
print(raw2)
print("")
 
for i in raw2:
    raw2 = raw2.lower()
print("lowercase")
print(raw2)
print("")
    
for i in raw2:
    raw2  = stemmer.stem(raw2)

print("stemming")
print(raw2)
print("")

for i in raw2 :
    raw2 = stopword.remove(raw2)

print("Stopword")
print(raw2)
print("")

gabung = [raw1, raw2]
count_vectorizer = CountVectorizer(tokenizer=tokenize)
data = count_vectorizer.fit_transform(gabung).toarray()

print ("data",data)
rpi