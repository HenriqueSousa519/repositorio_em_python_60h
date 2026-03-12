print('1:')
numero = int(input('digite um numero: '))
match numero:
    case numero if numero % 2 == 0:
        print('o numero é par')
    case _:
        print ('o numero é ímpar')
print('___'*15)
print ('2:')
numero2 = int(input('digite um numero: '))
match numero2:
    case numero2 if numero2 > 0:
        print('o numero é positivo')
    case numero2 if numero2 < 0:
        print ('o numero é negativo')
    case numero2 if numero2 == 0:
        print ('o numero é zero')
print('___'*15)
print ('3:')
palavra = input('digite uma palavra: ')
match palavra:
    case '':
        print ('está vazia')
    case _:
        print ('não está vazia, foi digitado: ', palavra)
print('___'*15)
print ('4:')
numero3 = int(input('digite um numero: '))
match numero3:
    case numero3 if numero3 > 10:
        print('o numero é maior que 10')
    case numero3 if numero3 < 10:
        print('o numero é menor que 10')
    case numero3 if numero3 == 10:
        print('o numero é 10, bobão')
print('___'*15)
print ('5:')
idade = int(input('digite uma idade: '))
match idade:
    case idade if idade <= 12:
        print('é uma criança')
    case idade if idade <= 17:
        print('é um adolescente')
    case idade if idade <= 35:
        print('é um jovem')
    case idade if idade >35 <64:
        print('é um adulto')
    case _:
        print('é um idoso')