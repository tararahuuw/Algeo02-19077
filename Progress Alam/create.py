from sklearn.feature_extraction.text import CountVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import math
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

REGEX = re.compile(r"\s")

def tokenize(text):
    return [tok.strip().lower() for tok in REGEX.split(text)]

file = open("Document1.txt","r");
raw1 = file.read()
print(raw1)

tandabaca = [".",",","-","%", ")", "("]
for td in tandabaca:
	raw1=raw1.replace(td,"")
 
for i in raw1 :
    raw1 = stopword.remove(raw1)
    
factory = StemmerFactory()
stemmer = factory.create_stemmer()


hasilstem1 = stemmer.stem(raw1)

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
 
for i in raw2:
    raw2 = raw2.lower()

for i in raw2 :
    raw2 = stopword.remove(raw2)

hasilstem2  = stemmer.stem(raw2)


f = open("dummy.txt", "w")
teks = input ("Masukkan Query :")

f.write(teks)
f.close()
dummy = open("dummy.txt", "r")
dummy = dummy.read()
print(dummy)

tandabaca = [".",",","-","%", ")", "("]
for td in tandabaca:
	dummy=dummy.replace(td,"")
 
for i in dummy :
    dummy = stopword.remove(dummy)
    
factory = StemmerFactory()
stemmer = factory.create_stemmer()


hasilstemdummy = stemmer.stem(dummy)

train_set = [hasilstemdummy, hasilstem1, hasilstem2]

count_vectorizer = CountVectorizer(tokenizer=tokenize)
data = count_vectorizer.fit_transform(train_set).toarray()
vocab = count_vectorizer.get_feature_names()

print ("Jumlah Term FREQUENCY=============================")
print (data)

print ("VECTOR FITUR=============================")
print (vocab)

def cosine_sim(vec1, vec2):
    hasildot = 0
    for i in range(len(vec1)):
        hasildot = hasildot + (vec1[i] * vec2[i])
        
    sum1 = 0;
    sum2 = 0
    for i in range(len(vec1)):
        sum1 = sum1 + vec1[i] ** 2
        sum2 = sum2 + vec2[i] ** 2
  
    besar1 = math.sqrt(sum1)
    besar2 = math.sqrt(sum2)
        
    return hasildot / (besar1 * besar2)

    
cosine = []
for i in range (len(train_set)-1) :
    cos = cosine_sim(data[0], data[i+1])
    cosine.append(cos)
    
def Urutindongkaka(data):
    max = data[0]
    
    while (len(data) != 0) :
        i = 0;
        while (i < len(data)) :
            if (max < data[i]) :
                max = data[i]
            i = i + 1

        print("cosine :",data[i-1],",","document",(i))
        data.pop(i-1)
    
    
Urutindongkaka(cosine)