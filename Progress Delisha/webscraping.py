import requests
import re

from bs4 import BeautifulSoup

r = requests.get('https://www.kompas.com/tag/tanaman-padi')

soup = BeautifulSoup(r.content, "html.parser")

tautan = []
for link in soup.find_all("h3"):
        for i in link.find_all("a") :
            artikel = i.get('href')
            tautan.append(artikel)

print(tautan)

documents = []
for i in tautan:
    try:
        r = requests.get(i)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, "html.parser")

        sen = []
        for i in soup.find('div',{'class':'read__content'}).find_all('p'):
            sen.append(i.text)
        
        print(sen)
        documents.append(' '.join(sen))
    
    except Exception as e:
        print(e.message)

print(documents)


# documents_clean = []
# for d in sen:
#     # Remove Unicode
#     document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
#     # Remove Mentions
#     document_test = re.sub(r'@\w+', '', document_test)
#     # Lowercase the document
#     document_test = document_test.lower()
#     # Remove punctuations
#     document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
#     # Lowercase the numbers
#     document_test = re.sub(r'[0-9]', '', document_test)
#     # Remove the doubled space
#     document_test = re.sub(r'\s{2,}', ' ', document_test)
#     documents_clean.append(document_test)