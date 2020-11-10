import os
from flask import Flask,redirect,render_template,request,url_for
from werkzeug.utils import secure_filename
import backend
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
            print(filename)

        string = request.form["query"]
        tuplesort = backend.back(string)

        curdir=os.path.dirname(os.path.realpath(__file__))
        docpath=curdir+'/templates/dokumen/'

        ldoc=[]
        ljumlah=[]
        lpersen=[]
        lawal=[]
        print(tuplesort)
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
        print(ldoc)
        print(ljumlah)
        print(lpersen)
        print(lawal)
        hasil=[0 for i in range(len(ldoc))]
        for i in range(len(hasil)):
            hasil[i] = {"doc":ldoc[i]+".txt","jumlah":ljumlah[i],"persen":lpersen[i],"awal":lawal[i]} 
        print(hasil)
        return redirect(url_for("result",query=string,hasil=hasil))

    else:
        return render_template("ahha.html")

@app.route('/result<query>/<hasil>', methods=["POST","GET"])
def result(query,hasil):
    if request.method == "POST":
        string = request.form["newquery"]
        return redirect(url_for("result",query=string,hasil=hasil))

    else:
        return render_template("result.html",query=query,hasil=hasil)

@app.route('/<namafile>')
def buka(namafile):
    return render_template("/dokumen/"+namafile)

@app.route('/perihal')
def perihal():
    return render_template("perihal.html")

if __name__ == "__main__":
    app.run(debug=True)