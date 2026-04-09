import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# 1. CONFIGURAÇÃO DO BANCO DE DADOS

def conectar():
    return sqlite3.connect('xyz_comercio.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL
        )''')
    conn.commit()
    conn.close()

# 2. FUNÇÕES CRUD

def limpar_campos():
    entry_cpf.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

def inserir_cliente():
    cpf = entry_cpf.get().strip()
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    endereco = entry_endereco.get().strip()
    
    if cpf and nome and email and telefone and endereco:
        try:
            conn = conectar()
            c = conn.cursor()
            c.execute('INSERT INTO clientes (cpf, nome, email, telefone, endereco) VALUES (?,?,?,?,?)', 
                      (cpf, nome, email, telefone, endereco))
            conn.commit()
            conn.close()
            messagebox.showinfo('Sucesso','Cliente cadastrado com sucesso!')
            limpar_campos()
            mostra_clientes()
        except sqlite3.IntegrityError:           
            messagebox.showerror('Erro', 'Este CPF já está cadastrado no sistema!')
        except sqlite3.Error as e:
            messagebox.showerror('Erro do Banco', f'Erro ao salvar: {e}')
    else:
        messagebox.showwarning('Aviso', 'Por favor, preencha todos os campos.')

def mostra_clientes():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()        
    c.execute('SELECT * FROM clientes')
    clientes = c.fetchall()
    for cliente in clientes:
        tree.insert('', 'end', values=cliente)
    conn.close()    

def preencher_campos_ao_clicar(event):
    """Função para preencher os inputs quando o usuário clica em uma linha da tabela"""
    selecao = tree.selection()
    if selecao:
        limpar_campos()       
        valores = tree.item(selecao)['values']
        
        entry_cpf.insert(0, valores[0])
        entry_nome.insert(0, valores[1])
        entry_email.insert(0, valores[2])
        entry_telefone.insert(0, valores[3])
        entry_endereco.insert(0, valores[4])

def editar_cliente():
    selecao = tree.selection()
    if selecao:
        cliente_cpf = tree.item(selecao)['values'][0]
        
        novo_nome = entry_nome.get().strip()
        novo_email = entry_email.get().strip()
        novo_telefone = entry_telefone.get().strip()
        novo_endereco = entry_endereco.get().strip()
        
        if novo_nome and novo_email and novo_telefone and novo_endereco:
            try:
                conn = conectar()
                c = conn.cursor()                
                c.execute('''UPDATE clientes 
                             SET nome = ?, email = ?, telefone = ?, endereco = ? 
                             WHERE cpf = ?''', 
                          (novo_nome, novo_email, novo_telefone, novo_endereco, cliente_cpf))
                conn.commit()
                conn.close()
                messagebox.showinfo('Sucesso','Dados do cliente atualizados!')
                limpar_campos()
                mostra_clientes()
            except sqlite3.Error as e:
                messagebox.showerror('Erro', f'Erro ao atualizar: {e}')
        else:
            messagebox.showwarning('Aviso', 'Preencha todos os campos antes de atualizar.')
    else:
        messagebox.showwarning('Aviso', 'Selecione um cliente na tabela para editar.')

def deletar_cliente():
    selecao = tree.selection()
    if selecao:
        resposta = messagebox.askyesno('Confirmar Exclusão', 'Tem certeza que deseja excluir este cliente?')
        if resposta:
            cliente_cpf = tree.item(selecao)['values'][0]
            try:
                conn = conectar()
                c = conn.cursor()
                c.execute('DELETE FROM clientes WHERE cpf = ?', (cliente_cpf,))
                conn.commit()
                conn.close()
                messagebox.showinfo('Sucesso', 'Cliente removido do sistema.')
                limpar_campos()
                mostra_clientes()
            except sqlite3.Error as e:
                messagebox.showerror('Erro', f'Erro ao deletar: {e}')
    else:
        messagebox.showwarning('Aviso', 'Selecione um cliente na tabela para excluir.')    

# 3. INTERFACE GRÁFICA (GUI)

janela = tk.Tk()
janela.geometry('800x650')
janela.title('XYZ Comércio - Cadastro de Clientes')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background='#f0f0f0', font=('Segoe UI', 10))
style.configure('TEntry', font=('Segoe UI', 10))
style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=5)
style.configure('Treeview.Heading', font=('Segoe UI', 10, 'bold'))
style.configure('Treeview', font=('Segoe UI', 10))

# Frame Principal
main_frame = ttk.Frame(janela, padding=15)
main_frame.pack(fill=tk.BOTH, expand=True)
style.configure('TFrame', background='#f0f0f0')

# Título
titulo = ttk.Label(main_frame, text='SISTEMA DE GESTÃO DE CLIENTES', font=('Segoe UI', 14, 'bold'))
titulo.grid(row=0, columnspan=2, pady=(0, 15))

# 4. FORMULÁRIO DE ENTRADA

input_frame = ttk.LabelFrame(main_frame, text=' DADOS DO CLIENTE ', padding=15)
input_frame.grid(row=1, column=0, columnspan=2, sticky='ew', pady=(0, 15))

# CPF
ttk.Label(input_frame, text='CPF (Apenas números):').grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_cpf = ttk.Entry(input_frame, width=20)
entry_cpf.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# NOME
ttk.Label(input_frame, text='Nome Completo:').grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_nome = ttk.Entry(input_frame, width=40)
entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# E-MAIL
ttk.Label(input_frame, text='E-mail:').grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_email = ttk.Entry(input_frame, width=40)
entry_email.grid(row=2, column=1, padx=5, pady=5, sticky='w')

# TELEFONE
ttk.Label(input_frame, text='Telefone:').grid(row=3, column=0, padx=5, pady=5, sticky='e')
entry_telefone = ttk.Entry(input_frame, width=20)
entry_telefone.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# ENDEREÇO
ttk.Label(input_frame, text='Endereço:').grid(row=4, column=0, padx=5, pady=5, sticky='e')
entry_endereco = ttk.Entry(input_frame, width=60)
entry_endereco.grid(row=4, column=1, padx=5, pady=5, sticky='w')

# 5. BOTÕES DE AÇÃO

btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=2, column=0, columnspan=2, pady=(0, 15))

btn_salvar = ttk.Button(btn_frame, text='➕ CADASTRAR', command=inserir_cliente)
btn_salvar.pack(side=tk.LEFT, padx=10)

btn_atualizar = ttk.Button(btn_frame, text='✏️ ATUALIZAR', command=editar_cliente)
btn_atualizar.pack(side=tk.LEFT, padx=10)

btn_deletar = ttk.Button(btn_frame, text='❌ DELETAR', command=deletar_cliente)
btn_deletar.pack(side=tk.LEFT, padx=10)

btn_limpar = ttk.Button(btn_frame, text='🧹 LIMPAR CAMPOS', command=limpar_campos)
btn_limpar.pack(side=tk.LEFT, padx=10)

# 6. TABELA (TREEVIEW)

tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=3, column=0, columnspan=2, sticky='nsew')

main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(3, weight=1)

# Criação da TreeView com as colunas atualizadas
columns = ('CPF', 'NOME', 'E-MAIL', 'TELEFONE', 'ENDEREÇO')
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configuração das colunas
tree.heading('CPF', text='CPF')
tree.column('CPF', width=100, anchor='center')

tree.heading('NOME', text='NOME')
tree.column('NOME', width=180, anchor='w')

tree.heading('E-MAIL', text='E-MAIL')
tree.column('E-MAIL', width=180, anchor='w')

tree.heading('TELEFONE', text='TELEFONE')
tree.column('TELEFONE', width=100, anchor='center')

tree.heading('ENDEREÇO', text='ENDEREÇO')
tree.column('ENDEREÇO', width=220, anchor='w')

# Evento para preencher os campos ao clicar em uma linha
tree.bind('<ButtonRelease-1>', preencher_campos_ao_clicar)
# Scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# 7. INICIALIZAÇÃO
criar_tabela()
mostra_clientes()

janela.mainloop()