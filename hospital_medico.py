import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE hospitalMedico (
        CNPJ INTEGER(14) NOT NULL,
        CRM INT NULL,
        CONSTRAINT FK_hospitalMedico_Hospital
        FOREIGN KEY (CNPJ) REFERENCES Hospital(CNPJ)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_hospitalMedico_Medico
        FOREIGN KEY (CRM) REFERENCES Medico(CRM)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()