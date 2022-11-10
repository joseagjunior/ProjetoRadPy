import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE Tratamento (
        CPF INTEGER(11) NOT NULL,
        CRM INT NULL,
        CID INT NULL,
        DATA DATE NOT NULL,
        CONSTRAINT FK_Tratamento_Paciente
        FOREIGN KEY (CPF) REFERENCES Paciente(CPF)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
''')

print('tabela criada com sucesso')


conexao.commit()
conexao.close()