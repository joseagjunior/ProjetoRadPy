import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE hospitalEnfermeiro (
        CNPJ INTEGER(14) NOT NULL,
        COREN INT NULL,
        CONSTRAINT FK_hospitalEnfermeiro_Hospital
        FOREIGN KEY (CNPJ) REFERENCES Hospital(CNPJ)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_hospitalEnfermeiro_Enfermeiro
        FOREIGN KEY (COREN) REFERENCES Enfermeiro(COREN)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()