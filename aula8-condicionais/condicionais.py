#if (se)
#if (passar uma condição) == True ou False:
#    isso sera feito
# condicional simples
idade = int(input("idade: "))
carteira_motorista = input('possui CNH')
#if idade >= 18 and carteira_motorista == 'sim':
#    print ('pode dirigir')
#else:
#    print ('não pode dirigir')
#condicionais compostas
#else ou elif
if idade>= 18:
    if carteira_motorista == 'sim':
        print('pode dirigir')
else:
    print ('não pode dirigir')