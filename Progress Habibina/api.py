from flask import Flask,render_template,request,url_for
app = Flask(__name__)

@app.route('/')
def ahha():
    return render_template("ahha.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/perihal')
def perihal():
    return render_template("perihal.html")

if __name__ == "__main__":
    app.run(debug=True)