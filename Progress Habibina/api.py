from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def ahha():
    return render_template("ahha.html")

@app.route('/perihal')
def perihal():
    return render_template("perihal.html")

if __name__ == "__main__":
    app.run(debug=True)