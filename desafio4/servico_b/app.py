from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        resposta = requests.get('http://servico-a:5000/users')
        dados = resposta.json()
        
        html = "<h1>Relatorio de Usuarios</h1><ul>"
        for usuario in dados:
            html += f"<li>O usuario <strong>{usuario['nome']}</strong> esta ativo desde {usuario['ano']}</li>"
        html += "</ul>"
        return html
        
    except:
        return "<h1>Erro: Nao consegui falar com o Servico A :(</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)