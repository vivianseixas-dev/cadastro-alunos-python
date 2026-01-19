#Importando Tkinter ---------------------

import tkinter as tk

#Importando dependencias do Tkinter ---------------------

from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#Importando pillow ---------------------

from PIL import Image, ImageTk

#Importando tk calendar ---------------------

from tkcalendar import Calendar, DateEntry
from datetime import date

#Importando main ---------------
from main import *

#Cores ---------------------

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

#Janelas ---------------------

janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=False, height=False)
janela.grid_columnconfigure(0, weight=0)
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(3, weight=1)




style = Style(janela)
style.theme_use("clam")

#details ---------------------

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

#Header ---------------------

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

#Header_logo ---------------------

global imagem, imagem_string, l_imagem

app_logo = Image.open('logo.png')
app_logo = app_logo.resize((50,50))
app_logo = ImageTk.PhotoImage(app_logo)
label_logo = tk.Label(
    frame_logo,
    image=app_logo,
    text='Sistema de Registro de Alunos',
    width=850,
    compound=LEFT,
    padx=10,
    anchor=tk.NW,
    font=('Verdana 15'),
    background=co6,
    foreground=co1
)
label_logo.place(x=5, y=0)

#Abrir imagem

imagem = Image.open('logo.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(frame_details, image=imagem, bg=co1, fg=co4)
label_imagem.place(x=390, y=10)

#left_menu ---------------------

frame_left_menu = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_left_menu.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)



#details_name ---------------------

label_name = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_name.place(x=4, y=10)
entrada_name = Entry(frame_details, width=30, justify='left', relief='solid')
entrada_name.place(x=7, y=40)

#details_email ---------------------

label_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_email.place(x=4, y=70)
entrada_email = Entry(frame_details, width=30, justify='left', relief='solid')
entrada_email.place(x=7, y=100)

#details_phone ---------------------

label_phone = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_phone.place(x=4, y=130)
entrada_phone = Entry(frame_details, width=18, justify='left', relief='solid')
entrada_phone.place(x=7, y=160)

#details_gender ---------------------

label_gender = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_gender.place(x=127, y=130)
c_gender = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_gender['values'] = ('M', 'F', 'T')
c_gender.place(x=130, y=160)

#details_date ---------------------

label_birth = Label(frame_details, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_birth.place(x=220, y=10)
entrada_birth = DateEntry(frame_details, width=20, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2026)
entrada_birth.place(x=224, y=40)

#details_address ---------------------

label_address = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_address.place(x=220, y=70)
entrada_address = Entry(frame_details, width=22, justify='left', relief='solid')
entrada_address.place(x=224, y=100)

#details_course ---------------------

courses = ['Engenharia', 'Medicina', 'Sociais']

label_course = Label(frame_details, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_course.place(x=220, y=130)
c_course = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_course['values'] = (courses)
c_course.place(x=224, y=160)

#----------------------- Funções para CRUD -----------------------

#Função adicionar
def add():
    global imagem, imagem_string, l_imagem

    #obtendo os valores
    name = entrada_name.get()
    email = entrada_email.get()
    phone = entrada_phone.get()
    gender = c_gender.get()
    birth = entrada_birth.get()
    address = entrada_address.get()
    course = c_course.get()
    img = imagem_string

    list = [name, email, phone, gender, birth, address, course, img]

    #verificação de valores da lista

    for i in list:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    #Registrar valores
    registration_system.register_student(list)

    #Limpar campos de entrada
    entrada_name.delete(0, END)
    entrada_email.delete(0, END)
    entrada_phone.delete(0, END)
    c_gender.delete(0, END)
    entrada_birth.delete(0, END)
    entrada_address.delete(0, END)
    c_course.delete(0, END)

    #Mostrar valores na tabela
    mostrar_alunos()

#Função procurar
def procurar():
    global imagem, imagem_string, l_imagem

    #Obter Id do Aluno
    id_aluno = int(entrada_procuraraluno.get())

    #Procurar aluno
    dados = registration_system.search_students(id_aluno)

    #Limpar campos de entrada
    entrada_name.delete(0, END)
    entrada_email.delete(0, END)
    entrada_phone.delete(0, END)
    c_gender.delete(0, END)
    entrada_birth.delete(0, END)
    entrada_address.delete(0, END)
    c_course.delete(0, END)

    #Inserir campos de entrada
    entrada_name.insert(END, dados[1])
    entrada_email.insert(END, dados[2])
    entrada_phone.insert(END, dados[3])
    c_gender.insert(END, dados[4])
    entrada_birth.insert(END, dados[5])
    entrada_address.insert(END, dados[6])
    c_course.insert(END, dados[7])


    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    
    label_imagem = tk.Label(frame_details, image=imagem, bg=co1, fg=co4)
    label_imagem.place(x=390, y=10)

#Função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem

    #Obter Id do Aluno
    id_aluno = int(entrada_procuraraluno.get())

    #obtendo os valores
    name = entrada_name.get()
    email = entrada_email.get()
    phone = entrada_phone.get()
    gender = c_gender.get()
    birth = entrada_birth.get()
    address = entrada_address.get()
    course = c_course.get()
    img = imagem_string

    list = [name, email, phone, gender, birth, address, course, img, id_aluno]

    #verificação de valores da lista

    for i in list:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    #Registrar valores
    registration_system.update_student(list)

    #Limpar campos de entrada
    entrada_name.delete(0, END)
    entrada_email.delete(0, END)
    entrada_phone.delete(0, END)
    c_gender.delete(0, END)
    entrada_birth.delete(0, END)
    entrada_address.delete(0, END)
    c_course.delete(0, END)

    #Limpar a imagem
    
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    
    label_imagem = tk.Label(frame_details, image=imagem, bg=co1, fg=co4)
    label_imagem.place(x=390, y=10)

    #Mostrar valores na tabela
    mostrar_alunos()

#Função deletar
def deletar():
    global imagem, imagem_string, l_imagem

    #Obter Id do Aluno
    id_aluno = int(entrada_procuraraluno.get())
    
    #Deletando o aluno
    registration_system.delete_student(id_aluno)
    
    #Limpar campos de entrada
    entrada_name.delete(0, END)
    entrada_email.delete(0, END)
    entrada_phone.delete(0, END)
    c_gender.delete(0, END)
    entrada_birth.delete(0, END)
    entrada_address.delete(0, END)
    c_course.delete(0, END)

    entrada_procuraraluno.delete(0,END)

    #Limpar a imagem
    
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    
    label_imagem = tk.Label(frame_details, image=imagem, bg=co1, fg=co4)
    label_imagem.place(x=390, y=10)

    #Mostrar valores na tabela
    mostrar_alunos()

#Função para escolher imagem ---------------------

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open('imagem')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(frame_details, image=imagem, bg=co1, fg=co4)
    label_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'ALTERAR FOTO'

botao_carregar = Button(frame_details, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font='Ivy 7 bold', bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)

#Table --------------------- 

frame_table = Frame(janela, bg=co1, relief=SOLID)
frame_table.grid(row=3, column=0, pady=5, padx=10, sticky="nsew", columnspan=2)



#Tabela ALunos ---------------------

def mostrar_alunos():

    list_header = ['Id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Curso']

    #ver todos os estudantes
    df_list = registration_system.view_all_students()

    tree_aluno = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")
    

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_aluno.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    frame_table.grid_columnconfigure(0, weight=1)
    frame_table.grid_rowconfigure(1, weight=1)
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_table.grid_rowconfigure(1, weight=1)
    frame_table.grid_columnconfigure(0, weight=1)

    hd=["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h=[40, 150,150,70,70,70,120,100,100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])
        n+=1
    
    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

#Procurar aluno ---------------------

frame_procuraraluno = Frame(frame_left_menu, width=40, height=55, bg=co1, relief=RAISED)
frame_procuraraluno.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

label_name = Label(frame_procuraraluno, text="Procurar aluno [Insira o ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_name.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
entrada_procuraraluno = Entry(frame_procuraraluno, width=5, justify='center', relief='solid', font=('Ivy 10'))
entrada_procuraraluno.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procuraraluno, command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font='Ivy 7 bold', bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

#Botões menu esquerdo -------------------------

app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
botao_app_img_adicionar = Button(frame_left_menu, command=add, image=app_img_adicionar, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co1, fg=co0)
botao_app_img_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('update.png')
app_img_atualizar = app_img_atualizar.resize((22,22))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
botao_app_img_atualizar = Button(frame_left_menu, command=atualizar, image=app_img_atualizar, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co1, fg=co0)
botao_app_img_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('delete.png')
app_img_deletar = app_img_deletar.resize((22,22))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
botao_app_img_deletar = Button(frame_left_menu, command=deletar, image=app_img_deletar, relief=GROOVE, text=' Deletar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co1, fg=co0)
botao_app_img_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

#Separador Vertical ----------------

label_linha = Label(frame_left_menu, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font='Ivy 1', bg=co1, fg=co0)
label_linha.place(x=243, y=15)


mostrar_alunos()

janela.mainloop()

