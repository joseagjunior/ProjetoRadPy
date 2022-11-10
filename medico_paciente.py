import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE medicoPaciente (
        CRM INT NULL,
        CPF INTEGER(11) NOT NULL,
        CONSTRAINT FK_medicoPaciente_Medico
        FOREIGN KEY (CRM) REFERENCES Medico(CRM)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_medicoPaciente_Paciente
        FOREIGN KEY (CPF) REFERENCES Paciente(CPF)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()