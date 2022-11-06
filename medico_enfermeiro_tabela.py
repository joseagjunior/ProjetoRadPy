import sqlite3

conexao = sqlite3.connect('cliente.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE medicos (
        crm VARCHAR(10),
        nome TEXT (50),
        cpf     VARCHAR(11) NOT NULL,
        bairro VARCHAR(11),
        rua TEXT NOT NULL,
        cidade TEXT(20),
        cep VARCHAR(8) NOT NULL
);
""")

print('tabela criada com sucesso')

cursor.execute("""
CREATE TABLE enfermeiros(
        corem VARCHAR(10),
        nome TEXT (50),
        cpf     VARCHAR(11) NOT NULL,
        bairro VARCHAR(11),
        rua TEXT NOT NULL,
        cidade TEXT(20),
        cep VARCHAR(8) NOT NULL
);
""")

print('tabela criada com sucesso')

conexao.commit()
conexao.close()