
from flask import Flask, request, render_template, send_file
from bark_engine import gerar_audio
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        nome_arquivo = gerar_audio(texto)
        return send_file(nome_arquivo, as_attachment=True)
    return render_template('index.html')
