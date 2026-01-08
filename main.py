import sqlite3
from tkinter import messagebox

class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           email TEXT NOT NULL,
                           phone TEXT NOT NULL,
                           gender TEXT NOT NULL,
                           birth TEXT NOT NULL,
                           address TEXT NOT NULL,
                           course TEXT NOT NULL,
                           picture TEXT NOT NULL)''')
        
    def register_student(self, students):
        self.c.execute("INSERT INTO students(name, email, phone, gender, birth, address, course, picture) VALUES (?,?,?,?,?,?,?,?)", (students))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registrado com Sucesso!')
    
    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Name: {i[1]} | Email: {i[2]} | Phone: {i[3]} | Gender: {i[4]} | Birth: {i[5]} | Address: {i[6]} | Course: {i[7]} | Picture: {i[8]} ')
    
    def search_students(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        dados = self.c.fetchone()
        
        print(f'ID: {dados[0]} | Name: {dados[1]} | Email: {dados[2]} | Phone: {dados[3]} | Gender: {dados[4]} | Birth: {dados[5]} | Address: {dados[6]} | Course: {dados[7]} | Picture: {dados[8]} ')
        
    def update_student(self, new_values):
        query = "UPDATE students SET name=?, email=?, phone=?, gender=?, birth=?, address=?, course=?, picture=? WHERE id=?"
        self.c.execute(query, new_values)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID:{new_values[8]} foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id, ))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi deletado!')

# Criando uma instância do Sistema de Registro
registration_system = RegistrationSystem()

#Informações
#student = ('Elena', 'elenao@gmail.com', '9999-9999', 'F', '01/05/2005', 'Angola,Luanda', 'IMedicina', 'imagem2.png')
#registration_system.register_student(student)

#Ver estudantes
#all_students = registration_system.view_all_students()

#Procurar Aluno
#search_student = registration_system.search_students(3)

#Atualizar cadastro
#tudent = ('Elena', 'elenao@gmail.com', '444', 'F', '01/05/2005', 'Angola,Luanda', 'IMedicina', 'imagem2.png', 2)
#update_student = registration_system.update_student(student)

#Deletar Aluno
registration_system.delete_student(1)
        
all_students = registration_system.view_all_students()   




