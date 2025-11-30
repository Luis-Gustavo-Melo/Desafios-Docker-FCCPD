from flask import Flask, jsonify

app = Flask(__name__)

lista_usuarios = [
    {"id": 1, "nome": "Luis", "role": "Admin"},
    {"id": 2, "nome": "Batman", "role": "Heroi"}
]

@app.route('/users')
def get_users():
    return jsonify(lista_usuarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)