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

curdir=os.path.dirname(os.path.realpath(__file__))
docpath=curdir+'/dokumen/'

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

# membaca query dan dokumen
def docinput(query):

    dokumen = glob.glob(docpath + "/*.txt")

    document = []
    document.append(clean(query))

    #loopping buat masukkin semua file ke array document
    for doc in dokumen:
        baca = open(doc, "r",encoding="utf8")
        bacain = baca.read()

        document.append(clean(bacain))

    return (document)

# menggabungkan kata-kata query dan dokumen
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

# menghitung kemunculan kata di dokumen dengan gabungan
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

# mengurutkan kemunculannya
def urut(jumlahdata,document):
    cosine = []
    for i in range (len(jumlahdata)-1) :
        cos = cosine_sim(jumlahdata[0], jumlahdata[i+1])
        cosine.append(cos)

    # print nama file tanpa extentionnya
    entries = os.listdir(docpath)
    filename = []
    for entry in entries:
        file = os.path.splitext(entry)[0]
        filename.append(file)

    dictionary = {filename[i]: cosine[i] for i in range(len(document)-1)}

    sort = sorted(dictionary.values() , reverse = True)

    tuplesort = sorted(dictionary.items(), key = lambda kv:kv[1], reverse = True)

    return tuplesort

# memanggil semua fungsi buat vektorisasi
def vektorisasi(query):
    document = docinput(query)
    listdata = gabung(document)        
    jumlahdata = hitung(listdata)
    tuplesort = urut(jumlahdata,document)
    return (tuplesort)