from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco
import project
import pandas as pd
from PIL import ImageTk, Image



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
            dados_hospital = "INSERT INTO Hospital (CNPJ, Nome, Rua, Numero, Bairro, Cidade, CEP, Telefone) VALUES ('"+cnpj.get()+"', '"+nome.get()+"', '"+rua.get()+"', '"+numero.get()+"', '"+bairro.get()+"', '"+cidade.get()+"', '"+cep.get()+"', '"+telefone.get()+"')"
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

def cadastro_medico():
    cadastro_medico = Toplevel(project.menu_inicial)
    cadastro_medico.title("MedSystem - Cadastrar Médico")
    cadmed_frm = ttk.Frame(cadastro_medico, padding=20)
    cadmed_frm.pack(fill="both", expand="yes")


    im_checked = ImageTk.PhotoImage(Image.open("checked.png"))
    im_unchecked = ImageTk.PhotoImage(Image.open("unchecked.png"))



    def consulta_hospital():
        tv_hosp.delete(*tv_hosp.get_children())
        consulta = "SELECT Nome FROM Hospital ORDER BY Nome"
        linhas = banco.dql(consulta)
        for l in linhas:
            tv_hosp.insert('', 'end',values=l, tags="unchecked")

    def consulta_especialidade():
        tv_esp.delete(*tv_esp.get_children())
        consulta = "SELECT nomeEspecialidade FROM Especialidade ORDER BY nomeEspecialidade"
        linhas = banco.dql(consulta)
        for l in linhas:
            tv_esp.insert('', 'end',values=l, tags="unchecked")

    def toggleCheck(evento):
        rowid = tv_esp.identify_row(evento.y)
        tag = tv_esp.item(rowid, "tags")[0]
        tags = list(tv_esp.item(rowid, "tags"))
        tags.remove(tag)
        tv_esp.item(rowid, tags=tags)
        if tag == "checked":
            tv_esp.item(rowid, tags="unchecked")
        else:
            tv_esp.item(rowid, tags="checked")

    def toggleCheck2(evento):
        rowid = tv_hosp.identify_row(evento.y)
        tag = tv_hosp.item(rowid, "tags")[0]
        tags = list(tv_hosp.item(rowid, "tags"))
        tags.remove(tag)
        tv_hosp.item(rowid, tags=tags)
        if tag == "checked":
            tv_hosp.item(rowid, tags="unchecked")
        else:
            tv_hosp.item(rowid, tags="checked")



    def inserir_medico():
        print(crm.get(), cpf.get(), nome.get(), rua.get(), numero.get(), bairro.get(), cidade.get(), cep.get())
        if crm.get()=="" or cpf.get()=="" or nome.get()=="" or rua.get()=="" or numero.get()=="" or bairro.get()=="" or cidade.get()=="" or cep.get()=="":
            messagebox.showinfo(title="Erro", message="É necessário digitar todos os dados!")
            return
        try:
            dados_medico = "INSERT INTO paciente (CRM, CPF, Nome, Rua, Numero, Bairro, Cidade, CEP) VALUES ('"+crm.get()+"', '"+cpf.get()+"', '"+nome.get()+"', '"+rua.get()+"', '"+numero.get()+"', '"+bairro.get()+"', '"+cidade.get()+"', '"+cep.get()+"')"
            banco.dml(dados_medico)
            messagebox.showinfo(title="Salvo", message="Dados salvos com sucesso!")
        except SyntaxError:
            messagebox.showinfo(title="Erro", message="Erro ao inserir!")
            return
    
    ttk.Label(cadmed_frm, text="Cadastre o Médico\n\n", width=20).grid(column=0, columnspan=8, row=3)
    ttk.Label(cadmed_frm, text="CRM:", width=7).grid(column=0, row=5)
    crm = ttk.Entry(cadmed_frm, width=30)
    crm.grid(column=1, columnspan=3, row=5)

    ttk.Label(cadmed_frm, text="CPF:", width=7).grid(column=4, row=5, sticky='e')
    cpf = ttk.Entry(cadmed_frm, width=30)
    cpf.grid(column=5, columnspan=3, row=5)
    
    ttk.Label(cadmed_frm, text=" ", width=7).grid(column=1, row=6)
    ttk.Label(cadmed_frm, text="Nome:", width=7).grid(column=0, row=7)
    nome = ttk.Entry(cadmed_frm, width=50)
    nome.grid(column=1, columnspan=7, row=7, sticky='we')
    
    ttk.Label(cadmed_frm, text=" ", width=7).grid(column=1, row=8)
    ttk.Label(cadmed_frm, text="Rua:", width=7).grid(column=0, row=9)
    rua = ttk.Entry(cadmed_frm)
    rua.grid(column=1, columnspan=4, row=9, sticky='we')
    
    ttk.Label(cadmed_frm, text="Número:", width=8).grid(column=5, row=9)
    numero = ttk.Entry(cadmed_frm)
    numero.grid(column=6, columnspan=2, row=9, sticky='we')
    
    ttk.Label(cadmed_frm, text=" ", width=8).grid(column=1, row=10)
    ttk.Label(cadmed_frm, text="Bairro:", width=7).grid(column=0, row=11)
    bairro = ttk.Entry(cadmed_frm, width=30)
    bairro.grid(column=1, columnspan=2, row=11)
    
    ttk.Label(cadmed_frm, text="Cidade:", width=8).grid(column=4, row=11)
    cidade = ttk.Entry(cadmed_frm, width=30)
    cidade.grid(column=5, columnspan=3, row=11)
    
    ttk.Label(cadmed_frm, text=" ", width=7).grid(column=1, row=12)
    ttk.Label(cadmed_frm, text="CEP:", width=7).grid(column=0, row=13)
    cep = ttk.Entry(cadmed_frm)
    cep.grid(column=1, columnspan=2, row=13, sticky='w')

    ttk.Label(cadmed_frm, text=" \n", width=7).grid(column=1, row=14)

    #quadroGrid_hosp=LabelFrame(cadmed_frm, text="Seleção de Hospitais")
    #quadroGrid_hosp.pack(fill="right", expand="yes", padx=5, pady=5)
    

    tv_hosp=ttk.Treeview(cadmed_frm, columns=('Nome'))
    style_esp = ttk.Style(tv_hosp)
    style_esp.configure(cadmed_frm, rowheight=10)
    tv_hosp.tag_configure('checked', image=im_checked)
    tv_hosp.tag_configure('unchecked', image=im_unchecked)

    tv_hosp.grid(column=0, columnspan=7, row=15)
    tv_hosp.column('Nome', minwidth=200, width=300)
    tv_hosp.heading('Nome', text='Hospitais')

    tv_hosp.bind('botao', toggleCheck2)
    consulta_hospital()
    

    ttk.Label(cadmed_frm, text=" ", width=7).grid(column=1, row=16)
    #quadroGrid_esp=LabelFrame(cadmed_frm, text="Seleção de Hospitais")
    #quadroGrid_esp.pack(fill="left", expand="yes", padx=5, pady=5)

    tv_esp=ttk.Treeview(cadmed_frm, columns=('nomeEspecialidade'))
    style_esp = ttk.Style(tv_esp)
    style_esp.configure(cadmed_frm, rowheight=10)
    tv_esp.tag_configure('checked', image=im_checked)
    tv_esp.tag_configure('unchecked', image=im_unchecked)

    tv_esp.grid(column=0, columnspan=7, row=17)
    tv_esp.column('nomeEspecialidade', minwidth=200, width=300)
    tv_esp.heading('nomeEspecialidade', text='Especialidades')

    tv_esp.bind('botao', toggleCheck)
    consulta_especialidade()

    ttk.Label(cadmed_frm, text=" \n", width=7).grid(column=1, row=18)
    
    ttk.Button(cadmed_frm, text="Salvar", width=10, padding=5, command=inserir_medico).grid(column=2, columnspan=3, row=19, sticky='we')
    
    
    cadastro_medico.mainloop()

def cadastro_especialidade():
    cadastro_especialidade = Toplevel(project.menu_inicial)
    cadastro_especialidade.title("MedSystem - Cadastrar Especialidade")
    cadEspec_frm = ttk.Frame(cadastro_especialidade, padding=20)
    cadEspec_frm.pack(fill="both", expand="yes")

    
    def inserir_especialidade():
        print(nome.get())
        resultado = banco.dql("SELECT nomeEspecialidade FROM Especialidade")
        df = pd.DataFrame(resultado, columns=["nomeEspecialidade"])
        nomes = df['nomeEspecialidade'].tolist()
        for i in range(len(nomes)):
            nomes[i] = nomes[i].upper()
        if nome.get()=="":
            messagebox.showinfo(title="Erro", message="É necessário digitar o nome da Especialidade!")
            return
        elif nome.get().upper() in nomes:
            messagebox.showinfo(title="Atenção", message="Essa especialidade já foi cadstrada!")
            return
        try:
            dados_especialidade = "INSERT INTO Especialidade (nomeEspecialidade) VALUES ('"+nome.get()+"')"
            banco.dml(dados_especialidade)
            messagebox.showinfo(title="Salvo", message="Dados salvos com sucesso!")
        except SyntaxError:
            messagebox.showinfo(title="Erro", message="Erro ao inserir!")
            return
        nome.delete(0, END)
        nome.focus()
    
    ttk.Label(cadEspec_frm, text="Cadastre a Especialidade\n\n", width=27).grid(column=1, columnspan=7, row=3)
    ttk.Label(cadEspec_frm, text="Nome:", width=7).grid(column=0, row=7)
    nome = ttk.Entry(cadEspec_frm, width=50)
    nome.grid(column=1, columnspan=7, row=7, sticky='we')
    
    ttk.Label(cadEspec_frm, text=" \n", width=7).grid(column=1, row=14)

    ttk.Button(cadEspec_frm, text="Salvar", width=10, padding=5, command=inserir_especialidade).grid(column=2, columnspan=3, row=15, sticky='we')
    
    
    cadastro_especialidade.mainloop()


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
            dados_paciente = "INSERT INTO paciente (cpf, rg, nome, bairro, rua, cidade, cep) VALUES ('"+cpf.get()+"', '"+rg.get()+"', '"+nome.get()+"', '"+bairro.get()+"', '"+rua.get()+"', '"+cidade.get()+"', '"+cep.get()+"')"
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