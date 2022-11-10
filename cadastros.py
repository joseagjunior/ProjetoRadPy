from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco
import project



def cadastro_hospital():
    cadastro_hospital = Toplevel(project.menu_inicial)
    cadastro_hospital.title("MedSystem - Cadastrar Hospital")
    cadhosp_frm = ttk.Frame(cadastro_hospital, padding=20)
    cadhosp_frm.pack(fill="both", expand="yes")

    
    def inserir_hospital():
        print(cnpj.get(), nome.get(), rua.get(), numero.get(), bairro.get(), cidade.get(), cep.get(), telefone.get())
        if cnpj.get()=="" or nome.get()=="" or rua.get()=="" or numero.get()=="" or bairro.get()=="" or cidade.get()=="" or cep.get()=="" or telefone.get()=="":
            messagebox.showinfo(title="Erro", message="É necessário digitar todos os dados!")
            return
        try:
            bancoDados = "hospital.db"
            dados_hospital = "INSERT INTO hospital (cnpj, nome, rua, numero, bairro, cidade, cep, telefone) VALUES ('"+cnpj.get()+"', '"+nome.get()+"', '"+rua.get()+"', '"+numero.get()+"', '"+bairro.get()+"', '"+cidade.get()+"', '"+cep.get()+"', '"+telefone.get()+"')"
            banco.conexaoBanco(bancoDados)
            banco.dml(dados_hospital)
            messagebox.showinfo(title="Salvo", message="Dados salvos com sucesso!")
        except SyntaxError:
            messagebox.showinfo(title="Erro", message="Erro ao inserir!")
            return
    
    ttk.Label(cadhosp_frm, text="Cadastre o Hospital\n\n", width=20).grid(column=0, columnspan=8, row=3)
    ttk.Label(cadhosp_frm, text="CNPJ:", width=7).grid(column=0, row=5)
    cnpj = ttk.Entry(cadhosp_frm, width=20)
    cnpj.grid(column=1, columnspan=2, row=5, sticky='w')

    ttk.Label(cadhosp_frm, text="Nome:", width=7).grid(column=3, row=5)
    nome = ttk.Entry(cadhosp_frm, width=35)
    nome.grid(column=4, columnspan=3, row=5, sticky='w')
    
    ttk.Label(cadhosp_frm, text=" ", width=7).grid(column=1, row=8)
    ttk.Label(cadhosp_frm, text="Rua:", width=7).grid(column=0, row=9)
    rua = ttk.Entry(cadhosp_frm, width=30)
    rua.grid(column=1, columnspan=3, row=9)
    
    ttk.Label(cadhosp_frm, text="Número:", width=8).grid(column=4, row=9)
    numero = ttk.Entry(cadhosp_frm, width=10)
    numero.grid(column=5, columnspan=2, row=9, sticky='w')
    
    ttk.Label(cadhosp_frm, text=" ", width=7).grid(column=1, row=10)
    ttk.Label(cadhosp_frm, text="Bairro:", width=7).grid(column=0, row=11)
    bairro = ttk.Entry(cadhosp_frm, width=30)
    bairro.grid(column=1, columnspan=3, row=11)
    
    ttk.Label(cadhosp_frm, text="Cidade:", width=8).grid(column=4, row=11)
    cidade = ttk.Entry(cadhosp_frm, width=25)
    cidade.grid(column=5, columnspan=2, row=11)
    
    ttk.Label(cadhosp_frm, text=" ", width=7).grid(column=1, row=14)
    ttk.Label(cadhosp_frm, text="CEP:", width=7).grid(column=0, row=15)
    cep = ttk.Entry(cadhosp_frm, width=20)
    cep.grid(column=1, row=15, sticky='w')
    
    ttk.Label(cadhosp_frm, text="Telefone:", width=8).grid(column=4, row=15)
    telefone = ttk.Entry(cadhosp_frm, width=25)
    telefone.grid(column=5, columnspan=2, row=15, sticky='w')
    
    ttk.Label(cadhosp_frm, text=" \n", width=7).grid(column=1, row=16)

    ttk.Button(cadhosp_frm, text="Salvar", width=10, padding=5, command=inserir_hospital).grid(column=0, columnspan=7, row=17)
    
    
    cadastro_hospital.mainloop()

def cadastro_paciente():
    cadastro_paciente = Toplevel(project.menu_inicial)
    cadastro_paciente.title("MedSystem - Cadastrar Paciente")
    cadPaciente_frm = ttk.Frame(cadastro_paciente, padding=20)
    cadPaciente_frm.pack(fill="both", expand="yes")

    
    def inserir_paciente():
        print(cpf.get(), rg.get(), nome.get(), bairro.get(), rua.get(), cidade.get(), cep.get())
        if cpf.get()=="" or rg.get()=="" or nome.get()=="" or bairro.get()=="" or rua.get()=="" or cidade.get()=="" or cep.get()=="":
            messagebox.showinfo(title="Erro", message="É necessário digitar todos os dados!")
            return
        try:
            bancoDados = "paciente.db"
            dados_paciente = "INSERT INTO paciente (cpf, rg, nome, bairro, rua, cidade, cep) VALUES ('"+cpf.get()+"', '"+rg.get()+"', '"+nome.get()+"', '"+bairro.get()+"', '"+rua.get()+"', '"+cidade.get()+"', '"+cep.get()+"')"
            banco.conexaoBanco(bancoDados)
            banco.dml(dados_paciente)
            messagebox.showinfo(title="Salvo", message="Dados salvos com sucesso!")
        except SyntaxError:
            messagebox.showinfo(title="Erro", message="Erro ao inserir!")
            return
    
    ttk.Label(cadPaciente_frm, text="Cadastre o Hospital\n\n", width=20).grid(column=0, columnspan=8, row=3)
    ttk.Label(cadPaciente_frm, text="CPF:", width=7).grid(column=0, row=5)
    cpf = ttk.Entry(cadPaciente_frm, width=20)
    cpf.grid(column=1, columnspan=2, row=5, sticky='w')

    ttk.Label(cadPaciente_frm, text="Nome:", width=7).grid(column=3, row=5)
    rg = ttk.Entry(cadPaciente_frm, width=35)
    rg.grid(column=4, columnspan=3, row=5, sticky='w')
    
    ttk.Label(cadPaciente_frm, text=" ", width=7).grid(column=1, row=8)
    ttk.Label(cadPaciente_frm, text="Rua:", width=7).grid(column=0, row=9)
    nome = ttk.Entry(cadPaciente_frm, width=30)
    nome.grid(column=1, columnspan=3, row=9)
    
    ttk.Label(cadPaciente_frm, text="Número:", width=8).grid(column=4, row=9)
    bairro = ttk.Entry(cadPaciente_frm, width=10)
    bairro.grid(column=5, columnspan=2, row=9, sticky='w')
    
    ttk.Label(cadPaciente_frm, text=" ", width=7).grid(column=1, row=10)
    ttk.Label(cadPaciente_frm, text="Bairro:", width=7).grid(column=0, row=11)
    rua = ttk.Entry(cadPaciente_frm, width=30)
    rua.grid(column=1, columnspan=3, row=11)
    
    ttk.Label(cadPaciente_frm, text="Cidade:", width=8).grid(column=4, row=11)
    cidade = ttk.Entry(cadPaciente_frm, width=25)
    cidade.grid(column=5, columnspan=2, row=11)
    
    ttk.Label(cadPaciente_frm, text=" ", width=7).grid(column=1, row=14)
    ttk.Label(cadPaciente_frm, text="CEP:", width=7).grid(column=0, row=15)
    cep = ttk.Entry(cadPaciente_frm, width=20)
    cep.grid(column=1, row=15, sticky='w')
    
    ttk.Label(cadPaciente_frm, text=" \n", width=7).grid(column=1, row=16)

    ttk.Button(cadPaciente_frm, text="Salvar", width=10, padding=5, command=inserir_paciente).grid(column=0, columnspan=7, row=17)
    
    
    cadastro_paciente.mainloop()