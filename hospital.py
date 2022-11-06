
import sqlite3

conexao = sqlite3.connect('hospital.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE hospital (
        cnpj VARCHAR(11),
        nome VARCHAR(10),
        rua VARCHAR(50),
        bairro VARCHAR(20),
        cidade VARCHAR(20),
        cep VARCHAR(8),
        telefone VARCHAR(10)
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()