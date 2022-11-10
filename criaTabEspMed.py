import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE EspecialdiadeMed (
        CRM INT NULL,
        ID INT AUTO_INCREMENT,
        CONSTRAINT FK_EspecialidadeMed_Medico
        FOREIGN KEY (CRM) REFERENCES Medico(CRM)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        CONSTRAINT FK_EspecialidadeMed_Especialidade
        FOREIGN KEY (ID) REFERENCES Especialidade(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()