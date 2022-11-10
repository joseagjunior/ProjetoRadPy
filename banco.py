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


#dados_hospital = "INSERT INTO hospital (cnpj, nome, rua, numero, bairro, cidade, cep, telefone) VALUES (1, 2, 3, 4, 5, 6, 7, 8)"
#dml(dados_hospital)
        