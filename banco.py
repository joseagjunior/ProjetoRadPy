import sqlite3
from sqlite3 import Error
import os

pastaApp=os.path.dirname(__file__)
nomeBanco="dados.db"

def conexaoBanco():
    conecta=None
    try:
        conecta=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return conecta

def dql(query): #select
    conexao = conexaoBanco()
    cursor = conexao.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def dml(query): #insert, update, delete
    try:
        conexao = conexaoBanco()
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        conexao.close()
    except Error as ex:
        print(ex)


#dados_hospital = "INSERT INTO Especialidade (nomeEspecialidade) VALUES ('ClinicoGeral')"
#dml(dados_hospital)
        