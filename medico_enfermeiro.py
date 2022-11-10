import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE medicoEnfermeiro (
        CRM INT NULL,
        COREN INT NULL,
        CONSTRAINT FK_medicoEnfermeiro_Medico
        FOREIGN KEY (CRM) REFERENCES Medico(CRM)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_medicoEnfermeiro_Enfermeiro
        FOREIGN KEY (COREN) REFERENCES Enfermeiro(COREN)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()