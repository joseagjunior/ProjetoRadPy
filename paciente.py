import sqlite3

conexao = sqlite3.connect('paciente.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE paciente (
        cpf     VARCHAR(11) NOT NULL,
        rg     VARCHAR(10) NOT NULL,
        nome     VARCHAR(50) NOT NULL,
        bairro VARCHAR(20),
        rua TEXT NOT NULL,
        cidade TEXT(20),
        cep VARCHAR(8) NOT NULL
);
""")

print('tabela criada com sucesso')