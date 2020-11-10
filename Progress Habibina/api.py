import backend
import os
import glob

from flask import Flask,redirect,render_template,request,url_for
from werkzeug.utils import secure_filename

import nltk
from nltk.tokenize import word_tokenize

curdir=os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER=curdir+'/templates/dokumen/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["POST","GET"])
def ahha():
    if request.method == "POST":
        f = request.files.getlist('dokumen')
        for file in f:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        string = request.form["query"]

        return redirect(url_for("result",query=string))

    else:
        return render_template("ahha.html")

@app.route('/result<query>', methods=["POST","GET"])
def result(query):
    if request.method == "POST":
        string = request.form["newquery"]
        return redirect(url_for("result",query=string))

    else:
        tuplesort = backend.vektorisasi(query)

        curdir=os.path.dirname(os.path.realpath(__file__))
        docpath=curdir+'/templates/dokumen/'

        ldoc=[]
        ljumlah=[]
        lpersen=[]
        lawal=[]
        for eltuple in tuplesort:
            doc = eltuple[0]
            ldoc.append(doc)
            f = open(docpath + "%s.txt" %doc, errors="ignore")
            article = f.read()
            jumlah = len(article.split())
            ljumlah.append(jumlah)
            persen = str("%.2f" % (eltuple[1]*100)) + '%'
            lpersen.append(persen)
            perkalimat = nltk.tokenize.sent_tokenize(article)
            awal = perkalimat[0]
            lawal.append(awal)

        hasil=[0 for i in range(len(ldoc))]
        for i in range(len(hasil)):
            hasil[i] = {"doc":ldoc[i]+".txt","jumlah":ljumlah[i],"persen":lpersen[i],"awal":lawal[i]}
        
        dokumen=[]
        dokumen.append(backend.clean(query))
        for doc in ldoc:
            dok = docpath+doc+".txt"
            baca = open(dok, "r",errors="ignore")
            bacain = baca.read()

            dokumen.append(backend.clean(bacain))

        listkata2 = backend.gabung(dokumen)
        [dataunion,datasort] = listkata2  
        dataquery = datasort[0]
        
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

@app.route('/<namafile>')
def buka(namafile):
    return render_template("/dokumen/"+namafile)

@app.route('/perihal')
def perihal():
    return render_template("perihal.html")

if __name__ == "__main__":
    app.run(debug=True)