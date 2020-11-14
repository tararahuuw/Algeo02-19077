import backend
import os
import glob

from flask import Flask,redirect,render_template,request,url_for
from werkzeug.utils import secure_filename

import nltk
from nltk.tokenize import word_tokenize

# tempat menyimpan dokumen
curdir=os.path.dirname(os.path.realpath(__file__))
docpath=curdir+'/dokumen/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = docpath

# halaman utama
@app.route('/', methods=["POST","GET"])
def ahha():
    # jika menerima input
    if request.method == "POST":

        # simpan dokumen ke folder
        f = request.files.getlist('dokumen')
        for file in f:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # mengambil input query
        string = request.form["query"]

        # pindah ke result
        return redirect(url_for("result",query=string))

    # jika tidak menerima input
    else:
        # render ahha.html
        return render_template("ahha.html")

# halaman result
@app.route('/result/<query>', methods=["POST","GET"])
def result(query):
    # jika menerima input baru, mengubah nilai query
    if request.method == "POST":
        string = request.form["query"]
        return redirect(url_for("result",query=string))

    else:
        tuplesort = backend.vektorisasi(query) # vektorisasi

        # menghitung hasil
        ldoc=[]
        ljumlah=[]
        lpersen=[]
        lawal=[]
        for eltuple in tuplesort:
            doc = eltuple[0]
            ldoc.append(doc)
            f = open(docpath + "%s.txt" %doc, encoding="utf8")
            article = f.read()
            jumlah = len(article.split())
            ljumlah.append(jumlah)
            persen = str("%.2f" % (eltuple[1]*100)) + '%'
            lpersen.append(persen)
            perkalimat = nltk.tokenize.sent_tokenize(article)
            awal = perkalimat[0]
            lawal.append(awal)

        # membuat dictionary hasil
        hasil=[0 for i in range(len(ldoc))]
        for i in range(len(hasil)):
            hasil[i] = {"doc":ldoc[i]+".txt","jumlah":ljumlah[i],"persen":lpersen[i],"awal":lawal[i]}
        
        # menngurutkan dokumen berdasarkan hasil
        dokumen=[]
        dokumen.append(backend.clean(query))
        for doc in ldoc:
            dok = docpath+doc+".txt"
            baca = open(dok, "r",encoding="utf8")
            bacain = baca.read()

            dokumen.append(backend.clean(bacain))

        listkata2 = backend.gabung(dokumen)
        [dataunion,datasort] = listkata2  
        dataquery = datasort[0]
        
        # menghitung kemunculan kata tiap dokumen
        kemunculan = []
        for kata in dataquery:
            dummy = [kata]
            for word in datasort:
                count = 0
                for i in word:
                    if kata == i:
                        count += 1
                dummy.append(count)
            kemunculan.append(dummy)

        return render_template("result.html",query=query,hasil=hasil,kemunculan=kemunculan)

# halaman webscraping
@app.route('/webscrapping', methods=["POST","GET"])
def webscrap():
    # jika menerima input
    if request.method == "POST":

        # mengambil input query
        string = request.form["query"]

        # pindah ke result
        return redirect(url_for("resultscrap",query=string))

    # jika tidak menerima input
    else:
        # render ahha.html
        return render_template("webscrapping.html")

@app.route('/webscrapping/<query>',methods=["POST","GET"])
def resultscrap(query):
    # jika menerima input baru, mengubah nilai query
    if request.method == "POST":
        string = request.form["query"]
        return redirect(url_for("resultscrap",query=string))
    
    else:
        retval = backend.webscrapping(query)
        [titles,kemunculan,sort] = retval
        return render_template("resultwebscrap.html",query=query,judul=titles,hasil=sort,kemunculan=kemunculan)

# halaman dokumen
@app.route('/dokumen/<namafile>')
def buka(namafile):
    with open(docpath+namafile, "r", encoding="utf8") as f:
        content = f.read()
    return render_template("dokumen.html",content=content,judul=namafile)

# halaman Images
@app.route('/images')
def gambar():
    return render_template("gambar.html")

# halaman perihal
@app.route('/perihal')
def perihal():
    return render_template("perihal.html")

# jalanin program
if __name__ == "__main__":
    app.run(debug=True)