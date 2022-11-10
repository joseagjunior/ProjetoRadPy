import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE Especialidade (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeEspecialidade VARCHAR(50)
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()