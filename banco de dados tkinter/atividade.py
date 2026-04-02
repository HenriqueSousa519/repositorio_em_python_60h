import sqlite3

conn = sqlite3.connect('agencia_marketing.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS leads (
    nome TEXT,
    idade INTEGER,
    email TEXT,
    endereco TEXT,
    trabalho TEXT,
    graduacao TEXT
)
''')

print("--- Adicionar Novo Lead ---")
nome_digitado = input("Nome: ")
idade_digitada = input("Idade: ")
email_digitado = input("E-mail: ")
endereco_digitado = input("Endereço: ")
trabalho_digitado = input("Trabalho: ")
graduacao_digitada = input("Graduação: ")

cursor.execute('''
INSERT INTO leads (nome, idade, email, endereco, trabalho, graduacao) 
VALUES (?, ?, ?, ?, ?, ?)
''', (nome_digitado, idade_digitada, email_digitado, endereco_digitado, trabalho_digitado, graduacao_digitada))

conn.commit()

print("\n--- Leads cadastrados no Banco de Dados ---")
cursor.execute('SELECT * FROM leads')

for row in cursor.fetchall():
    print(row)

conn.close()