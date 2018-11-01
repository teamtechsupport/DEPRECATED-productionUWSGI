from flask import Flask, request, render_template
app = Flask(__name__)
import annealing_decryption
import re
import string
import json
from column_transposition import transpos
key = string.ascii_uppercase
ciphertype = "substitution"

@app.route('/')
def my_form():
    return render_template('index.html')

regex = re.compile('[^A-Z]')
@app.route('/', methods=['GET', 'POST'])
def my_form_post():
<<<<<<< HEAD
    text = request.form['text']
    userinput = text.upper()
=======
>>>>>>> 42f3e6171813e7efdd84eb72ab3410c2b456c7ae
    selected = []
    substitionresult = ""
    columntransresult= ""
    if request.form.get('substition'):
        selected.append("substition")
        print(regex.sub('', userinput), "HE")
        substitionresult = annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", "")
    if request.form.get('vigenere'):
        selected.append("vigenere")
    if request.form.get('columntrans'):
        selected.append('columntrans')
        columns = request.form['columns']
        colno = 0
        if columns == "":
            colno = 0
        else:
            colno = int(columns)
        if colno > 1:
            columntransresult = transpos(regex.sub('', userinput), colno)
        else:
            for x in range(2, 21):
                columntransresult = transpos(regex.sub('', userinput), x)
    print(json.dumps(selected))
<<<<<<< HEAD
    return render_template("result.html", substitionresult = substitionresult, columntransresult = columntransresult)
=======
    text = request.form['text']
    userinput = text.upper()
    regex = re.compile('[^A-Z]')
    print(regex.sub('', userinput), "HE")
    decoded = annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", "")
    return render_template("result.html", data = decoded)
>>>>>>> 42f3e6171813e7efdd84eb72ab3410c2b456c7ae

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)	
