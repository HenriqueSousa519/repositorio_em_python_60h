print('exercicio 1:')
i = 0
while i <= 1000:
    print("numero ", i)
    i += 1
print('---'*20)
print ('exercicio 2:')
nomes = []
c = 0
while c < 10:
    nome = input('escreva seu nome:')
    nomes.append(nome)
    c += 1
print ('Nomes registrados: ')
for nome in nomes:
    print(nome)
print('---'*20)
