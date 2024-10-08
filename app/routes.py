from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'path_para_o_seu_diretorio_de_upload'

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/testar_modelo', methods=['GET', 'POST'])
def test_model():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Nenhum arquivo foi enviado'
        file = request.files['file']
        if file.filename == '':
            return 'Nenhum arquivo selecionado'
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            # Aqui você pode chamar o seu modelo para fazer a detecção de fogo na imagem
            resultado = detect_fire(filepath)  # Suponha que você tenha uma função `detect_fire` para isso
            return render_template('resultado.html', resultado=resultado)
    return render_template('testar_modelo.html')
