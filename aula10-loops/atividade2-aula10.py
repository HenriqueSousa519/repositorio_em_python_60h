login = {
    "usuário":"professor",
    "senha":"professor122"
}
media1 = 0
media2 = 0
media3 = 0
for tentativas in range(3):
    print ('olá professor')
    senha = input('digite sua senha:')
    if senha == login["senha"]:
        notas = input('deseja digitar a nota dos alunos?')
        while notas == 'sim':
            print('escolha o aluno', '1 - Henrique | 2 - Rafael | 3 - Vinicius')
            aluno = int(input('aluno:'))
            if aluno == 1:
                nota1 = int(input('digite a nota 1:'))
                nota2 = int(input('digite a nota 2:'))
                nota3 = int(input('digite a nota 3:'))
                media1 = (nota1 + nota2 + nota3) / 3
                print (media1)
                notas = input('deseja digitar a nota dos alunos?')
                if notas == 'sim':
                    print('escolha o aluno', '1 - Henrique | 2 - Rafael | 3 - Vinicius')
                    aluno = int(input('aluno:'))
                elif notas != 'sim':
                    breakpoint
            if aluno == 2:
                nota1 = int(input('digite a nota 1:'))
                nota2 = int(input('digite a nota 2:'))
                nota3 = int(input('digite a nota 3:'))
                media2 = (nota1 + nota2 + nota3) / 3
                print (media2)
                notas = input('deseja digitar a nota dos alunos?')
                if notas == 'sim':
                    print('escolha o aluno', '1 - Henrique | 2 - Rafael | 3 - Vinicius')
                    aluno = int(input('aluno:'))
                elif notas != 'sim':
                    breakpoint
            if aluno == 3:
                nota1 = int(input('digite a nota 1:'))
                nota2 = int(input('digite a nota 2:'))
                nota3 = int(input('digite a nota 3:'))
                media3 = (nota1 + nota2 + nota3) / 3
                print (media3)
                notas = input('deseja digitar a nota dos alunos?')
                if notas == 'sim':
                    print('escolha o aluno', '1 - Henrique | 2 - Rafael | 3 - Vinicius')
                    aluno = int(input('aluno:'))
                elif notas != 'sim':
                    breakpoint
        medias = input('deseja ver a media dos alunos?')
        if medias == 'sim':
            print('media de Henrique', media1)
            print('media de Rafael', media2)
            print('media de Vinicius', media3)
        sair = input('deseja sair?')
        if sair == 'sim':
            confirmar = input('aperte enter para confirmar')
            break
else:
    print('conta bloqueada por excesso de erro')