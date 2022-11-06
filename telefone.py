
import sqlite3

conexao = sqlite3.connect('telefone.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE telefone (
        cod VARCHAR(4),
        documento VARCHAR(10),
        telefone VARCHAR(50)
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()