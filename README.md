# Algeo02-19077
## Tubes Algeo 2

                Tugas Besar 2
        Aljabar Linear dan Geometri
                Dibuat oleh: 
       - M. Fahmi Alamsyah (13519077)
       - Habibina Arif Muzayyan (13519125)
       - Delisha Azza Naadira (13519133)

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Tugas besar ini bertujuan membuat search engine dengan menggunakkan metode cosine similarty dnegan spesifikasi sebagai berikut :
1. Program mampu menerima search query. Search query dapat berupa kata dasar maupun berimbuhan. 
2. Dokumen yang akan menjadi kandidat dibebaskan formatnya dan disiapkan secara manual. Minimal terdapat 15 dokumen berbeda sebagai kandidat dokumen. Bonus: Gunakan web      scraping untuk mengekstraksi dokumen dari website. 
3. Hasil pencarian yang terurut berdasarkan similaritas tertinggi dari hasil teratas hingga hasil terbawah berupa judul dokumen dan kalimat pertama dari dokumen tersebut. Sertakan juga nilai similaritas tiap dokumen. 
4. Program disarankan untuk melakukan pembersihan dokumen terlebih dahulu sebelum diproses dalam perhitungan cosine similarity. Pembersihan dokumen bisa meliputi hal-hal berikut ini. 
    a. Stemming dan Penghapusan stopwords dari isi dokumen. 
    b. Penghapusan karakter-karakter yang tidak perlu. 
5. Program dibuat dalam sebuah website lokal sederhana. Dibebaskan untuk menggunakan framework pemrograman website apapun. Salah satu framework website yang bisa dimanfaatkan adalah Flask (Python), ReactJS, dan PHP. 
6. Kalian dapat menambahkan fitur fungsional lain yang menunjang program yang anda buat (unsur kreativitas diperbolehkan/dianjurkan). 
7. Program harus modular dan mengandung komentar yang jelas. 
8. Dilarang menggunakan library cosine similarity yang sudah jadi.


## Screenshots
![masuk](https://user-images.githubusercontent.com/49779495/99183433-5459f700-276e-11eb-8181-573e37962e12.png)

![masuk2](https://user-images.githubusercontent.com/49779495/99183486-bfa3c900-276e-11eb-8039-2562f502bcbc.png)

## Technologies
* Python 3

## Setup
1. Install library Sastrawi
2. Install library Flask
3. Install library nltk
4. Download folder src
5. Run API.py
6. Masukkan document yang ingin dicari
7. Masukkan query pencarian

## Code Examples
-Install library Sastrawi on cmd with command 'pip install sastrawi'

-Install library Flask on cmd with command 'pip install flask'

-Install library NLTK on cmd with command 'pip install nltk'

![cmd](https://user-images.githubusercontent.com/49779495/99183061-c67d0c80-276b-11eb-99f3-a129a1a049b4.PNG)

-Open API.py with text Editor

-Run program in cmd with command 'python API.py'

-copy link in cmd http://127.0.0.1:5000/ and paste in Google

![cmd2](https://user-images.githubusercontent.com/49779495/99183368-c54cdf00-276d-11eb-91a3-8ede745956e3.PNG)

## Features
List of features ready:
* Search Query dari document txt
* Search Query dengan web scraping dari https://www.detik.com/search/searchall?query=tanaman%20padi&siteid=3&sortby=time&sorttime=0&page=1
* About
* Images
* Changing background image with timer
* Table of Query
* Hyperlink

To-do list for future development :
* Implemetasi ke web online

## Status
Project is: _finished_

## Inspiration
https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Tubes2-Algeo-2020.pdf

https://towardsdatascience.com/create-a-simple-search-engine-using-python-412587619ff5

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

https://youtu.be/HLNdqYFhasc

## Contact
feel free to contact us!

Created by Muhammad Fahmi Alamsyah (https://www.github.com/tararahuuw)

Created by Habibina Arif Muzayyan (https://www.github.com/habibinaarif)

Created by Delisha Azza Naadira (https://www.github.com/delishaandr)
