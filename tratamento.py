
import sqlite3

conexao = sqlite3.connect('tratamento.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE tratamento (
        cpf VARCHAR(11),
        crm VARCHAR(10),
        cid VARCHAR(50),
        data DATE NOT NULL
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()