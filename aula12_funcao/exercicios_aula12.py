print('exercicio 1: ')
def par_impar(): 
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite um numero: '))
    resto1 = num1 % 2
    resto2 = num2 % 2
    texto1 = 'par' if resto1 == 0 else 'Impar'
    texto2 = 'par' if resto2 == 0 else 'Impar'
    if texto1 == 'par' and texto2 == 'par':
        print ('os dois numeros são par')
    elif texto1 == 'par' and texto2 != 'par':
        print ('apenas o numero 1 é par')
    elif texto1 != 'par' and texto2 == 'par':
        print(' apenas o numero 2 é par')
    else:
        print ('os dois numeros são ímpar')
par_impar()

print('_________'*15)

print('exercicio 2: ')
def multiplicar():
    numero1 = int(input('digite um numero: '))
    numero2 = int(input('digite um numero: '))
    numero3 = int(input('digite um numero: '))
    mult = numero1 * numero2 * numero3
    print(mult)
multiplicar()

print('_________'*15)

print('exercicio 3: ')
def calcular_potencia():
    base = int(input('digite um numero: '))
    expoente = int(input('digite um numero: '))
    resultado = base ** expoente
    print("o numero ", base, "elevado ao ", expoente, "vai resultar ", resultado)
    return resultado
calcular_potencia()

print('_________'*15)

print('exercicio 4:')
def verificar_idade():
    idade = int(input('digite sua idade: '))
    if idade == 18:
        print('Olha, 18 anos, ja pode ir preso kkkk')
    else:
        print('voce tem', idade, 'anos.')
verificar_idade()

print('_________'*15)

print('Exercicio 5:')
def descobrir_idade():
    ano_nascimento = int(input('digite o ano em que voce nasceu: '))
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    print('voce tem (ou vai completar)', idade, 'anos.')
descobrir_idade()

print('_________'*15)

print('exercicio 6:')
#a copa foi em 1998 então eu troquei o ano
def copa_98():
    ano = 1998
    campeao = 'França'
    pais_pesquisado = input('qual pais voce quer saber se ganhou a copa? ')
    if pais_pesquisado == campeao:
        print('sim a', campeao, 'foi o campeao da copa de 1998')
    else:
        print('não, o/a', pais_pesquisado, 'não foi campeão da copa de 1998')
copa_98()

print('_________'*15)
print('exercicio 7:')
def cumprimento(nome):
    return 'olá', nome
def produto(lista_prod, prod, carrinho, meus_v, lista_valores, paga):

    carrinho.append(lista_prod[prod])
    meus_v.append(lista_valores[paga])
    return carrinho,'R$',  float(sum(meus_v))
def pagamento(lista_tip_pags, escolha_pag):
    return lista_tip_pags[escolha_pag]
def restaurante():
   
    menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
    valores  = [0,100,60,150,250]
    carrinho = []
    meus_valores = []
    nome = input('Nome: ')
    print(cumprimento(nome))
 
    for p, v in enumerate(zip(menu, valores)):
        print(p,'R$', v)    

    acrescentar =  input('deseja acrescentar ao carrinho? ')
    while acrescentar == 'sim':    
        e  =  int(input('Escolha seu produto: 1 ,2 ,3, 4:'))
        print( produto(menu, e, carrinho, meus_valores,valores, e ))
        acrescentar = input('Deseja continuar? ')
 
    else:
        lista_pag = ['', '1 pix', '2 CC', ' 3 CD']
        escolha =  int(input(f'Escolha a forma de pagamento,  {lista_pag}'))
        print(pagamento(lista_pag, escolha))
        print('Obrigado volte SEMPRE!')    
restaurante()