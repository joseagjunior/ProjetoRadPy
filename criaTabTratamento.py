import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE Tratamento (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CID VARCHAR(10),
        Descricao VARCHAR(30),
        Observacao VARCHAR(300)
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()