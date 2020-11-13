import requests
import re
import glob
import math
import os
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

from bs4 import BeautifulSoup
tautan = []
for i in range(1,2):
    r = requests.get('https://www.detik.com/search/searchall?query=tanaman%20padi&siteid=3&sortby=time&sorttime=0&page=' + str(i))

    soup = BeautifulSoup(r.content, "html.parser")

    for link in soup.find('div',{'class':'list media_rows list-berita'}).find_all('a'):
        tautan.append(link['href'])

print(tautan) 

Document = []
titles = []

query = input("Masukkan query : ")
#cari link
for link in tautan :
    r = requests.get(link)
    data = []
    soup = BeautifulSoup(r.content, "html.parser")

    for i in soup.find('div',{'class':'detail__body-text itp_bodycontent'}).find_all('p'):
        data.append(i.text)
    for i in soup.find('div',{'class':'detail__header'}).find_all('h1'):
        judul = i.text.strip()
        
    Document.append(data)
    titles.append(judul)

print("Ini DOCUMENT")
print(Document)   

    
#buka semua link
dataunion = []
datasementara = []
data = []
for doc in Document:
    file1 = open("MyFile.txt","w") 
    
    for kalimat in doc :
        file1.write(clean(kalimat) + " ")
        
    file1.close()
    
    baca = open("MyFile.txt", "r")
    bacain = baca.read()
    
    dataunion.append(clean(bacain))

#masukkin query di dataunion  
dataunion.append(clean(query))
 

for i in dataunion:
    print("\n\n\n\n")
    print(i)

#Split
datagabung = []
datasementara = []
data = []
for doc in dataunion:
    datasementara = doc.split()
    dummy = []
    for kata in datasementara:
        if kata not in datagabung:
            datagabung.append(kata)
            
        dummy.append(kata)
    data.append(dummy)
    
#data gabung itu semua kata yang muncul di seluruh dokumen
#data itu semua kata yang muncul permasing2 dokumen
print(datagabung)
print(data)

datagabung.sort()
jumlahdata =[]
for arr in data:
    dummy = []
    
    for kata in datagabung :
        count = 0
        for data1 in arr:
            if kata == data1:
                count = count + 1
                
        dummy.append(count)
    jumlahdata.append(dummy)
    
cosine = []
for i in range (len(jumlahdata)-1) :
    cos = cosine_sim(jumlahdata[i], jumlahdata[(len(jumlahdata)-1)])
    cosine.append(cos)

print("\n\n\n\n")
print("data")
print(data)
print("\n\n\n\n")
print("datagabung")
print(datagabung)
print("\n\n\n\n")
print('jumlahdata')
a = 0
for i in jumlahdata:
    print("\n\n\n\n")
    print(a)
    print(i)
    
    a = a + 1
print("\n\n\n\n")
print('cosine')
a = 0
for i in cosine:
    print("\n\n\n\n")
    print(a)
    print(i)
    
    a = a + 1
     
   