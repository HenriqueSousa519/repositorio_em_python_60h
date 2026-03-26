import random
def atividade1():
    x = random.radint(5,10)
    return x

def atividade2():
    x = random.radint(1,10)
    y = random.radint(1,10)
    z = random.radint(1,10)
    return x, y, z

def atividade3():
    x = range(10,30)
    y = random.choice(x)
    return y

def atividade4():
    cont_reg = 10
    while cont_reg > 0:
        print (cont_reg)
        cont_reg -= 1
        if cont_reg == 0:
            return ('fogo!')

def atividade5():
    num = int(input('digite um numero qualquer: '))
    soma = 0
    for i in range(2, num + 1):
        if i % 2 == 0:
            soma += i
    return soma

def atividade6():
    num = int(input('digite um numero de 1 a 10: '))
    mult = 0
    for i in range(1,11):
        mult = num * i
        print(num, 'x', i, "é igual a", mult)

def atividade7():
    for i in range(99, 0, -1):
        if i % 2 != 0:
            print(i)
        
    