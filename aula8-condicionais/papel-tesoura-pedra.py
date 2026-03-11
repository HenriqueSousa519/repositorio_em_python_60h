import random #criar aleatoriedade
maquina = ['','✂️', '🪨', '🧻'] #lista icones -1 ->
escolha_maquina = random.choice(maquina[1:]) #escolha
id_maquina = maquina.index(escolha_maquina)#posição dos indices da lista da maquina

#-----------------------------------------------------------------
minhas = ['','✂️', '🪨', '🧻']
print("escolha '✂️-1','🪨-2','🧻-3'")
minha_escolha = int(input('escolha o objeto -> '))

if minha_escolha == id_maquina:
    print ('empate')
    print('esolha da maquina - ',escolha_maquina)
    print('minha escolha - ',minhas[minha_escolha])
elif id_maquina == 1 and minha_escolha == 3:
    print ('vitoria da maquina!')
    print ('escolha da maquina - ',escolha_maquina)
    print ('minha escolha - ', minhas[minha_escolha])
elif id_maquina == 2 and minha_escolha == 1:
    print ('vitoria da maquina!')
    print ('escolha da maquina - ',escolha_maquina)
    print ('minha escolha - ', minhas[minha_escolha])
elif id_maquina == 3 and minha_escolha == 2:
    print ('vitoria da maquina!')
    print ('escolha da maquina - ',escolha_maquina)
    print ('minha escolha - ', minhas[minha_escolha])
elif id_maquina == 3 and minha_escolha == 1:
    print ('vitoria!')
    print ('escolha da maquina - ',escolha_maquina)
    print ('minha escolha - ', minhas[minha_escolha])
elif id_maquina == 2 and minha_escolha == 3:
    print ('vitoria!')
    print ('escolha da maquina - ',escolha_maquina)
    print ('minha escolha - ', minhas[minha_escolha])
elif id_maquina == 1 and minha_escolha == 2:
    print ('vitoria!')
    print ('escolha da maquina - ',escolha_maquina)
    print ('minha escolha - ', minhas[minha_escolha])