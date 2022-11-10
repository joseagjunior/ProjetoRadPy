import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE Paciente (
        CPF INTEGER(11) NOT NULL,
        RG INTEGER(10) NOT NULL,
        Nome VARCHAR(50) NOT NULL,
        Rua VARCHAR(50) NOT NULL,
        Numero INTEGER(5) NOT NULL,
        Bairro VARCHAR(30) NOT NULL,
        Cidade VARCHAR(20) NOT NULL,
        CEP INTEGER(8) NOT NULL,
        PRIMARY KEY (CPF)
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()