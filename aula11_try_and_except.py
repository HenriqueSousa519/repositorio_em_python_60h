num = 0
try:
    num = int(input('digite um numero: '))
    print (num)
except ValueError:
    print('digite um numero inteiro')

print ('________'*15)
print ("exercicio 2")
try:
    a = int(input('digite o dividendo: '))
    b = int(input('digite o divisor: '))
    print( a/b )
except ZeroDivisionError:
    print('não pode ser dividido por 0')

print ('______'*15)
print ('exercicio 3')
try:
    lista = [1,2,3,4,5,6,7,8,9,10]
    i = int(input('digite um numero: '))
    print (lista[i])
except IndexError:
    print('numero não está na lista')
