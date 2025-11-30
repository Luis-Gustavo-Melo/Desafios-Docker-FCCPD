from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Luis", "ano": 2020},
    {"id": 2, "nome": "Genshin Player", "ano": 2021},
    {"id": 3, "nome": "Dungeon Master", "ano": 2023}
]

@app.route('/users')
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)