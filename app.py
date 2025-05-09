from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import negocio


app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1.5000"])

@app.route("/perguntas/<int:enquete_id>", methods=["GET"])
@cross_origin()
def recupera_perguntas(enquete_id: int):
	dados = negocio.recupera_perguntas(enquete_id)
	return (jsonify(dados), 200)

app.run(debug=True)