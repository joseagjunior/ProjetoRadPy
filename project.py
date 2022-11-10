from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco
from cadastros import *

menu_inicial = Tk()
menu_inicial.title("MedSystem")
mi_frm = ttk.Frame(menu_inicial, padding=20)
mi_frm.grid()

#icones
hospital_icon = PhotoImage(file= r"icon\hospital_icon.png").subsample(8,8)
medico_icon = PhotoImage(file= r"icon\medico_icon.png").subsample(8,8)
especialidade_icon = PhotoImage(file= r"icon\especialidade_icon.png").subsample(8,8)
enfermeiro_icon = PhotoImage(file= r"icon\enfermeiro_icon.png").subsample(8,8)
paciente_icon = PhotoImage(file= r"icon\paciente_icon.png").subsample(8,8)
tratamento_icon = PhotoImage(file= r"icon\tratamento_icon.png").subsample(8,8)

ttk.Button(mi_frm, text="Cadastrar Hosital", image=hospital_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=1, row=1)
ttk.Button(mi_frm, text="Cadastrar Médico(a)", image=medico_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=2, row=1)
ttk.Button(mi_frm, text="Cadastrar Especialidades", image=especialidade_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=3, row=1)
ttk.Button(mi_frm, text="Cadastrar Enfermeiro(a)", image=enfermeiro_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=4, row=1)
ttk.Button(mi_frm, text="Cadastrar Paciente", image=paciente_icon, compound=TOP, command=cadastro_paciente, width=25, padding=7).grid(column=5, row=1)
ttk.Button(mi_frm, text="Cadastrar Tratamento", image=tratamento_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=6, row=1)

menu_inicial.mainloop()