from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import negocio
import os

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5000"])

@app.route("/perguntas/<int:enquete_id>", methods=["GET"])
@cross_origin()
def recupera_perguntas(enquete_id: int):
    dados = negocio.recupera_perguntas(enquete_id)
    return jsonify(dados), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
