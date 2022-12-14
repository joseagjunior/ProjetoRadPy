from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco
from cadastros import *

#tela e frame
menu_inicial = Tk()
menu_inicial.title("MedSystem")
#width = menu_inicial.winfo_screenwidth()
#height = menu_inicial.winfo_screenheight()
#menu_inicial.geometry("%dx%d" % (width, height))
menu_inicial.attributes('-fullscreen', True)
mi_frm = ttk.Frame(menu_inicial, padding=20)
mi_frm.grid()

#icones
hospital_icon = PhotoImage(file= r"icon\hospital_icon.png").subsample(8,8)
medico_icon = PhotoImage(file= r"icon\medico_icon.png").subsample(2,2)
especialidade_icon = PhotoImage(file= r"icon\especialidade_icon.png").subsample(8,8)
enfermeiro_icon = PhotoImage(file= r"icon\enfermeiro_icon.png").subsample(2,2)
paciente_icon = PhotoImage(file= r"icon\paciente_icon.png").subsample(2,2)
tratamento_icon = PhotoImage(file= r"icon\tratamento_icon.png").subsample(8,8)
exit_icon = PhotoImage(file= r"icon\exit_icon.png").subsample(2,2)

#botões
ttk.Button(mi_frm, text="Cadastrar Hosital", image=hospital_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=1, row=1)
ttk.Button(mi_frm, text="Cadastrar Médico(a)", image=medico_icon, compound=TOP, command=cadastro_medico, width=25, padding=7).grid(column=2, row=1)
ttk.Button(mi_frm, text="Cadastrar Especialidades", image=especialidade_icon, compound=TOP, command=cadastro_especialidade, width=25, padding=7).grid(column=3, row=1)
ttk.Button(mi_frm, text="Cadastrar Enfermeiro(a)", image=enfermeiro_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=4, row=1)
ttk.Button(mi_frm, text="Cadastrar Paciente", image=paciente_icon, compound=TOP, command=cadastro_paciente, width=25, padding=7).grid(column=5, row=1)
ttk.Button(mi_frm, text="Cadastrar Tratamento", image=tratamento_icon, compound=TOP, command=cadastro_hospital, width=25, padding=7).grid(column=6, row=1)
ttk.Button(mi_frm, text="Sair", image=exit_icon, compound=TOP, command=menu_inicial.destroy, width=25, padding=7).grid(column=7, row=1)

menu_inicial.mainloop()