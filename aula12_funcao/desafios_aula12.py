print ('desafio 2:')
import statistics

empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

empresas = {
    'empresa 1': empresa1,
    'empresa 2': empresa2,
    'empresa 3': empresa3,
    'empresa 4': empresa4
}

def obter_moda(salarios):
    if len(set(salarios)) == len(salarios):
        return 'não tem moda'
    return "R$ " + int(statistics.mode(salarios))

def calcular_e_exibir_estatisticas(nome, salarios):
    media = statistics.mean(salarios)
    mediana = statistics.median(salarios)
    desvio_padrao = statistics.stdev(salarios)
    moda = obter_moda(salarios)
    print(nome, ":")
    print("Média: R$", media)
    print("Mediana: R$", mediana)
    print("Moda:", moda)
    print("Desvio: R$", desvio_padrao)
    print("---" * 40)
    
    return media

def analisar_todas_as_empresas(dicionario_empresas):
    maior_media = 0
    empresa_maior_media = ""

    for nome, salarios in dicionario_empresas.items():
        media_atual = calcular_e_exibir_estatisticas(nome, salarios)
        
        if media_atual > maior_media:
            maior_media = media_atual
            empresa_maior_media = nome
            

    print("A", empresa_maior_media, "foi escolhida por ter a maior média salarial no valor de R$", maior_media)


analisar_todas_as_empresas(empresas)