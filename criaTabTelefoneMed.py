import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE TelefoneMed (
        ID INT AUTO_INCREMENT,
        CRM VARCHAR(10) NOT NULL,
        Telefone INTEGER(11) NOT NULL,
        PRIMARY KEY (ID),
        CONSTRAINT FK_Telefone_Medico
        FOREIGN KEY (CRM) REFERENCES Medico(CRM)
        ON DELETE CASCADE
        ON UPDATE CASCADE
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()