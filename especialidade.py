
import sqlite3

conexao = sqlite3.connect('especialidade.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE especialdiade (
        cod VARCHAR(4),
        documento VARCHAR(10),
        especialidade VARCHAR(50)
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()