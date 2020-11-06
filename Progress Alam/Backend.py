from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

Doc1 = 'Perekonomian bangga di Indonesia, indonesia sedang sedang dalam pertumbuhan yang membanggakan.'
print(Doc1)
stemming   = stemmer.stem(Doc1)
print(stemming)

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

stopword = stopword.remove(stemming)
print(stopword)

lowercase = stopword.lower()
print(lowercase)

import string
tandabaca = lowercase.translate(str.maketrans("","",string.punctuation))
print(tandabaca)

split = tandabaca.split()
print(split)
splitword = []
countsplit = []

for word in split:
    if (word) not in splitword:
        splitword.append(word)
i = 0
for i in range(len(splitword)):
    count = 0;
    for j in range (len(split)) :
        if (splitword[i] == split[j]):
            count = count + 1
    countsplit.append(count)
    
print(splitword)
print(countsplit)
