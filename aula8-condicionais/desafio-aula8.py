quantidade_de_pessoas = int(input('digite a quantidade de pessoas 1, 2 ou 3: '))
if quantidade_de_pessoas == 1:
    cliente1 = input('digite seu nome: ')
    idade1 = int(input('digite sua idade: '))
    print ('cadastrado: ', cliente1, idade1)
elif quantidade_de_pessoas == 2:
    cliente1 = input('digite seu nome: ')
    idade1 = int(input('digite sua idade: '))
    print ('cadastrado: ', cliente1, idade1)
    cliente2 = input('digite seu nome: ')
    idade2 = int(input('digite sua idade: '))
    print ('cadastrado: ', cliente2, idade2)
elif quantidade_de_pessoas == 3:
    cliente1 = input('digite seu nome: ')
    idade1 = int(input('digite sua idade: '))
    print ('cadastrado: ', cliente1, idade1)
    cliente2 = input('digite seu nome: ')
    idade2 = int(input('digite sua idade: '))
    print ('cadastrado: ', cliente2, idade2)
    cliente3 = input('digite seu nome: ')
    idade3 = int(input('digite sua idade: '))
    print ('cadastrado: ', cliente3, idade3)

quarto = input('digite o quarto desejado; simples R$100 duplo R$150 luxo R$250: ')
dias = int(input('digite a quantidade de dias da estadia: '))
if quarto == "simples":
    preco = dias*(100*quantidade_de_pessoas)
    print('o valor ficou: ', preco)
elif quarto == "duplo":
    preco = dias*(150*quantidade_de_pessoas)
    print('o valor ficou: ', preco)
elif quarto == "luxo":
    preco = dias*(250*quantidade_de_pessoas)
    print('o valor ficou: ', preco)
