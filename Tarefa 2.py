import pandas as pd
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "API funcionando"

# a) Requisição para criar um arquivo .csv (enviando dados para adicionar no csv); 

@app.route('/criar_csv', methods=['POST'])
def criar_csv():

    dados = request.json

    df = pd.DataFrame(dados)

    df.to_csv("dados.csv", index=False)

    return "CSV criado"

# b) Requisição para editar um arquivo .csv (enviando dados para adicionar no csv original - 
# se pode especificar se quer deletar ou add alguma linha do csv, isso pode ficar por sua conta - seja criativo! =] ); 

@app.route('/editar_csv', methods=['POST'])
def editar_csv():

    dados = request.json

    df = pd.DataFrame([dados])

    df.to_csv("dados.csv", mode="a", index=False, header=False)

    return "Edição feita ao CSV"


# c) Requisição para ler de n a m linhas de um arquivo .csv;

@app.route('/ler_csv', methods=['GET'])
def ler_csv():

    n = int(request.args.get('n'))
    m = int(request.args.get('m'))

    df = pd.read_csv("dados.csv")

    resultado = df.iloc[n:m]

    return resultado.to_json(orient="records")

# d) Requisição para retornar valores filtrados com valores menores que x (enviar nome da coluna numérica que será realizado filtro);

@app.route('/filtrar_csv', methods=['GET'])
def filtrar_csv():

    var = request.args.get('var')
    x = float(request.args.get('x'))

    df = pd.read_csv("dados.csv")

    if var not in df.columns:
        return jsonify({"erro": "Coluna não encontrada"})

    df[var] = pd.to_numeric(df[var], errors="coerce")

    resultado = df[df[var] < x]

    return resultado.to_json(orient="records")


# e) Fique a vontade para inserir requisições (além das solicitadas nesta tarefa) que você ache interessante, aprendidas nos estudos da biblioteca pandas. 
# Requisição para excluir linhas refrentes ao genero de filme y;

@app.route('/excluir_genero', methods=['DELETE'])
def excluir_genero():

    genero = request.args.get('y')

    df = pd.read_csv("dados.csv")

    df = df[df["genero"] != genero]

    df.to_csv("dados.csv", index=False)

    return jsonify({"mensagem": f"Filmes do genero {genero} removidos"})

app.run(debug=True)








