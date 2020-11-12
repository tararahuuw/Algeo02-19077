import glob
import math
import os
import io
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

import nltk
from nltk.tokenize import word_tokenize

#Membuat fungsi cosine similarity
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
        
    return (hasildot / (besar1 * besar2))

#Fungsi untuk membersihkan kalimat
def clean(doc) :
    tandabaca = [".",",","-","%", ")", "("]
    for i in doc:
        doc = doc.lower()
        doc = stopword.remove(doc)
    
    for td in tandabaca:
        if (td == '-'):
            doc=doc.replace(td," ")
        else:
            doc=doc.replace(td,"")
            
    doc = stemmer.stem(doc)
    return (doc)

def docinput(query):

    curdir=os.path.dirname(os.path.realpath(__file__))
    path = curdir+'/templates/dokumen'
    dokumen = glob.glob(path + "/*.txt")

    document = []
    document.append(clean(query))

    #loopping buat masukkin semua file ke array document
    for doc in dokumen:
        baca = open(doc, "r",encoding="utf8")
        bacain = baca.read()

        document.append(clean(bacain))

    return (document)

def gabung(document):
    dataunion = []
    datasementara = []
    data = []
    for doc in document:
        datasementara = doc.split()
        dummy = []
        for kata in datasementara:
            if kata not in dataunion:
                dataunion.append(kata)

            dummy.append(kata)
        data.append(dummy)
    listdata = [dataunion,data]
    return(listdata)

def hitung(listdata):
    dataunion = listdata[0]
    data = listdata[1]

    dataunion.sort()
    jumlahdata =[]
    for arr in data:
        dummy = []

        for kata in dataunion :
            count = 0
            for data1 in arr:
                if kata == data1:
                    count = count + 1

            dummy.append(count)
        jumlahdata.append(dummy)

    return (jumlahdata)

def urut(jumlahdata,document):
    cosine = []
    for i in range (len(jumlahdata)-1) :
        cos = cosine_sim(jumlahdata[0], jumlahdata[i+1])
        cosine.append(cos)

    curdir=os.path.dirname(os.path.realpath(__file__))
    path=curdir+'/templates/dokumen/'
    # print nama file tanpa extentionnya
    entries = os.listdir(path)
    filename = []
    for entry in entries:
        file = os.path.splitext(entry)[0]
        filename.append(file)

    dictionary = {filename[i]: cosine[i] for i in range(len(document)-1)}

    sort = sorted(dictionary.values() , reverse = True)

    #print(data)
    #print(document)
    #print(dataunion)
    #print(jumlahdata)
    #print(cosine)
    #print(filename)
    #print(dictionary)
    #print(sort)

    tuplesort = sorted(dictionary.items(), key = lambda kv:kv[1], reverse = True)

    return tuplesort
    #for eltuple in tuplesort:
    #    doc = eltuple[0]
        #print(doc)
    #    f = open(path + "%s.txt" %doc,encoding="utf8")
    #    article = f.read()
    #    jumlah = len(article.split())
        #print(jumlah)
    #    persen = str("%.2f" % (eltuple[1]*100)) + '%'
        #print(persen)
    #    perkalimat = nltk.tokenize.sent_tokenize(article)
    #    awal = perkalimat[0]
        #print(awal)

def vektorisasi(query):
    document = docinput(query)
    listdata = gabung(document)        
    jumlahdata = hitung(listdata)
    tuplesort = urut(jumlahdata,document)
    return (tuplesort)