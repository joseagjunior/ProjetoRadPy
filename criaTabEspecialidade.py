import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE Especialdiade (
        ID INT AUTO_INCREMENT,
        Especialidade VARCHAR(50),
        PRIMARY KEY (ID)
        );
""")

print('tabela criada com sucesso')


conexao.commit()
conexao.close()