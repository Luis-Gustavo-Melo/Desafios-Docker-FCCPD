from flask import Flask, jsonify

app = Flask(__name__)

lista_pedidos = [
    {"id": 100, "item": "Placa de Video", "valor": 3000},
    {"id": 101, "item": "Mouse Gamer", "valor": 150}
]

@app.route('/orders')
def get_orders():
    return jsonify(lista_pedidos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)