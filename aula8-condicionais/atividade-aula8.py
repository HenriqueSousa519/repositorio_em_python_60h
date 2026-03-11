print ('1')
numero = int(input('digite um numero: '))
if numero >= 0:
    print ('o numero é positivo')
else:
    print ('o numero é negativo')
print('---'*15)
print ('2')
idd = int(input('digite sua idade: '))
if idd >= 16:
    print ('já pode votar')
else:
    print('não pode votar')
print('---'*15)
print ('3')
vari = int(input('digite um numero: '))
if vari % 2 == 0:
    print (vari, 'é par')
else:
    print (vari, 'é ímpar')
print('---'*15)
print ('4')
n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
if n1 == n2 == n3:
    print('o triangulo é equilátero')
elif n1 == n2 != n3 or n1 == n3 != n2 or n1 != n2 == n3:
    print('o triangulo é isósceles')
elif n1 != n2 != n3:
    print ('o triangulo é escaleno')
print('---'*15)
print ('5')
num = int(input('digite um numero: '))
if num % 5 == 0 and num % 7 == 0:
    print ('é multiplo de 5 e 7')
else:
    print ('não é multiplo de 5 e 7')
print('---'*15)
print ('6')
posi = int(input('digite um numero: '))
if posi >= 0 and posi >= 10:
    print ('o numero é positivo e maior que 10')
else:
    print ('não é maior que 10 ou inteiro')
print('---'*15)
print ('7')
divi = int(input('digite um numero: '))
if divi % 3 == 0 and divi % 5 == 0:
    print('o numero é divisível por 3 e 5')
elif divi % 5 == 0:
    print ('o numero é divisivel por 5')
elif divi % 3 == 0:
    print ('o numero é divisivel por 3')
else:
    print ('não é divisivel nem por 3 e nem por 5')
print('---'*15)
print('---'*15)
print('---'*15)