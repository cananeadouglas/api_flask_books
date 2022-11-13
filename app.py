from flask import Flask, jsonify, request, redirect, url_for, render_template
import json
from src.db import livros

#tinydb <- ver

app = Flask(__name__)

@app.route('/')
def index():
    variavel = "Você esta programando em Python Flask"
    return render_template("index.html", variavel_base = variavel)


# Consultar (todos) os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    
    return jsonify(livros)



# Consultar por (id) não está funcionando
@app.route('/livrosporid/{id}', methods=['GET'])
def pesquisar_livros(id: int):
    if request.method == "GET":
        idlivro = int(request.form['idlivro'])
        for livro in livros:
            if livro.get('id') == idlivro:
                return jsonify(livro)
    else:
        return "error"
    




# Editar por
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Criar ou adicionar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

app.run(debug=True, port=5000)
