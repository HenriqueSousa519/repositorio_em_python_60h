import os
import shutil

print('exercicio 1:')
with open('exercicio1.txt', 'w') as arquivo:
    arquivo.write('teste')
    

with open('exercicio1.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print('---'*20)
print('exercicio 2:')
with open('exercicio2.txt', 'w') as novo_arquivo:
    os.mkdir('1exercicio')
with open('1exercicio\exercicio4.txt', 'w') as arquivo:
    arquivo.write('teste4')

print('---'*20)
print('exercicio 3:')
os.rename('1exercicio', '1exercicio_e_exercicio3')

print('---'*20)
print('exercicio 4:')
with os.scandir('1exercicio_e_exercicio3') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

print('---'*20)
print('exercicio 5:')
shutil.copytree('1exercicio_e_exercicio3', 'exercicio5')

print('---'*20)
print('exercicio 6:')
shutil.rmtree('c:/Users/aluno/Downloads/aula14/exercicio5')