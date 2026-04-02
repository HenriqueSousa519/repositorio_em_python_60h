import tkinter as tk

def enviar():
    nome = input_nome.get()
    idade = input_idade.get()
    email = input_email.get()
    endereco = input_endereco.get()
    celular = input_celular.get()
    cep = input_cep.get()
    cidade = input_cidade.get()
    cursos = input_cursos.get()

    print('DADOS DO CLIENTE')
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'E-mail: {email}')
    print(f'Endereço: {endereco}')
    print(f'Celular: {celular}')
    print(f'CEP: {cep}')
    print(f'Cidade: {cidade}')
    print(f'Cursos: {cursos}')

    texto_resultado.config(text=f'Dados de {nome} enviados com sucesso no console!', fg='green')


janela = tk.Tk()
janela.title('Sistema de Cadastro de Clientes')

janela.geometry('1700x750')
janela.configure(bg='white')
janela.iconbitmap('masqueico.ico')

titulo = tk.Label(janela, text='SISTEMA DE CADASTRO DE CLIENTES', font=('arial', 30, 'bold'), bg='white')
titulo.pack(pady=40)

frame_form = tk.Frame(janela, bg='white')
frame_form.pack()

campos = [
    "Nome:", 
    "Idade:", 
    "E-mail:", 
    "Endereço:", 
    "Celular:", 
    "Cep:", 
    "Cidade:", 
    "Cursos:"
]

inputs = []

for i, campo in enumerate(campos):
    tela = tk.Label(frame_form, text=campo, font=('arial', 20), bg='white')
    tela.grid(row=i, column=0, sticky='e', pady=10, padx=20)
    
    enter = tk.Entry(frame_form, font=('arial', 20), bg='#e5e5e5')
    enter.grid(row=i, column=1, pady=10, padx=20)
    inputs.append(enter)

(input_nome, input_idade, input_email, input_endereco, 
 input_celular, input_cep, input_cidade, input_cursos) = inputs

btn = tk.Button(
    janela, 
    text='ENVIAR', 
    font=('arial', 20, 'bold'), 
    bg="#1b5d1e", 
    command=enviar,
    cursor="hand2",
    width=15
)
btn.pack(pady=40)

texto_resultado = tk.Label(janela, text='AGUARDANDO ENVIO...', font=('arial', 20), bg='white', fg='gray')
texto_resultado.pack(pady=10)

janela.mainloop()