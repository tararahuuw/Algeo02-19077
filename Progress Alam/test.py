import glob
import math
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

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

path = r'E:\Tubes ALGEOW anjg\Document'
read_files = glob.glob(path + "/*.txt")

document = []
query = input("Masukkan query : ")
document.append(clean(query))

#loopping buat masukkin semua file ke array document
for doc in read_files:
    baca = open(doc, "r")
    bacain = baca.read()
    
    document.append(clean(bacain))

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
    
cosine = []
for i in range (len(jumlahdata)-1) :
    cos = cosine_sim(jumlahdata[0], jumlahdata[i+1])
    cosine.append(cos)
    
dictionary = {document[i+1]: cosine[i] for i in range(len(document)-1)}

print(data)
print(document)
print(dataunion)
print(jumlahdata)
print(cosine)
print(dictionary)


