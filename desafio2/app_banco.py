import sqlite3
import os
from datetime import datetime

caminho_pasta = "/dados"
caminho_banco = os.path.join(caminho_pasta, "banco_secreto.db")

if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)

print(f"--- Conectando ao banco em: {caminho_banco} ---")
conn = sqlite3.connect(caminho_banco)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS acessos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TEXT,
        mensagem TEXT
    )
''')

agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mensagem = "Eu sobrevivi a exclusao do container!"
cursor.execute("INSERT INTO acessos (data_hora, mensagem) VALUES (?, ?)", (agora, mensagem))
conn.commit()

print("\n--- LENDO DADOS DO BANCO ---")
cursor.execute("SELECT * FROM acessos")
registros = cursor.fetchall()

for registro in registros:
    print(f"ID: {registro[0]} | Data: {registro[1]} | Msg: {registro[2]}")

print("----------------------------\n")
conn.close()