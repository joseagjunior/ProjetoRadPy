import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE Agendamento (
        CPF INTEGER(11) NOT NULL,
        CRM INT NULL,
        ID_Tratamento INT NULL,
        DATA DATE NOT NULL,
        CONSTRAINT FK_Agendamento_Paciente
        FOREIGN KEY (CPF) REFERENCES Paciente(CPF)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_Agendamento_Medico
        FOREIGN KEY (CRM) REFERENCES Medico(CRM)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_Agendamento_Tratamento
        FOREIGN KEY (ID_Tratamento) REFERENCES Tratamento(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()