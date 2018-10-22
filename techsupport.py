from flask import Flask, request, render_template
app = Flask(__name__)
import annealing_decryption
import re
import string
import json

key = string.ascii_uppercase
ciphertype = "substitution"

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
<<<<<<< HEAD
    selected = []
    if request.form.get('substition'):
        selected.append("substition")
    if request.form.get('vigenere'):
        selected.append("vigenere")
    if request.form.get('columntrans'):
        selected.append('columntrans')
    print(json.dumps(selected))
    text = request.form['text']
    userinput = text.upper()
    regex = re.compile('[^A-Z]')
    print(regex.sub('', userinput), "HE")
    return (annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", ""))
=======
        selected = []
        if request.form.get('substition'):
            selected.append("substition")
        if request.form.get('vigenere'):
            selected.append("vigenere")
        if request.form.get('columntrans'):
            selected.append('columntrans')
        print(json.dumps(selected))
	text = request.form['text']
	userinput = text.upper()
	regex = re.compile('[^A-Z]')
	decoded = annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", "")
    return render_template("result.html", data = decoded)
>>>>>>> 94fbdbfcfcbf3c4e471a708e3063a17b233fb74b

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)	
