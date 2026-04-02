import tkinter as tk



def mostrar():
    dado =  input_1.get()
    print('dados', dado)


janela  =  tk.Tk()
janela.geometry('800x600')
janela.configure(bg = 'white')
janela.iconbitmap('masqueico.ico')

# tk.Label(janela, text = 'ISSO É UM TESTE...').pack()
texto = tk.Label(janela, text = 'DIGITE ALGO...', font=('arial', 25), bg = 'white')
texto.pack(pady=90)

input_1  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
input_1.pack()


btn  =  tk.Button(janela, text= 'MOSTRAR', font=('arial', 15), bg = '#e5e5e5', command=mostrar)
btn.pack(pady=65)

texto2 = tk.Label(janela, text = 'VAI APARECER AQUI', font=('arial', 25), bg = 'white')
texto2.pack(pady=20)

janela.mainloop()