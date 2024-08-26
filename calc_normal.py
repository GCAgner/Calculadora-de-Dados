#versão 1.0 método da normal

import time
import math
from scipy.stats import norm

# Função para calcular probabilidades de dados com lados iguais
def calcula_normal_igual(x, y, z):
    inicio = time.time()  # Registra o tempo inicial

    # Média e variância de um dado
    media_dado = (x + 1) / 2
    variancia_dado = ((x - 1) * (x + 1)) / 12

    # Média e variância para a soma de y dados
    media_soma = y * media_dado
    variancia_soma = y * variancia_dado
    desvio_padrao_soma = math.sqrt(variancia_soma)

    # Probabilidade acumulada da distribuição normal
    prob = norm.cdf(z - 0.5, loc=media_soma, scale=desvio_padrao_soma)
    probabilidade = (1 - prob) * 100

    print(f"\nA probabilidade de o valor desejado acontecer é de: {probabilidade:} %")

    duracao = time.time() - inicio  # Calcula a duração da execução
    print(f"\nTempo necessário para calcular: {duracao:} segundos")

# Função para calcular probabilidades de dados com lados diferentes
def calcula_normal_diferente(y, z, vetor):
    inicio = time.time()  # Registra o tempo inicial

    media_soma = 0
    variancia_soma = 0

    for lados in vetor:
        # Média e variância de cada dado0

        media_dado = (lados + 1) / 2
        print(media_dado)

        variancia_dado = (((lados*lados) - 1)) / 12
        print(variancia_dado)

        # Somando as médias e variâncias
        media_soma += media_dado
        variancia_soma += variancia_dado

    desvio_padrao_soma = math.sqrt(variancia_soma)

    # Probabilidade acumulada da distribuição normal
    prob = norm.cdf(z - 0.5, loc=media_soma, scale=desvio_padrao_soma)
    probabilidade = (1 - prob) * 100

    print(f"\nA probabilidade de o valor desejado acontecer é de: {probabilidade:} %")

    duracao = time.time() - inicio  # Calcula a duração da execução
    print(f"\nTempo necessário para calcular: {duracao:} segundos")

# Função principal
def main():
    while True:
        resposta = int(input("Os dados são iguais ou diferentes? (0 = iguais, 1 = diferentes): "))
        print("\n")

        if resposta == 0:
            y = int(input("Digite a quantidade de dados: "))
            z = int(input("Digite o valor desejado: "))
            x = int(input("Digite o número de lados dos dados: "))

            calcula_normal_igual(x, y, z)

        elif resposta == 1:
            y = int(input("Digite a quantidade de dados: "))
            z = int(input("Digite o valor desejado: "))
            vetor = []

            for i in range(y):
                valor_dado = int(input(f"Digite o número de lados do dado {i+1}: "))
                vetor.append(valor_dado)

            calcula_normal_diferente(y, z, vetor)

        else:
            print("Opção inválida. Por favor, escolha 0 ou 1.")
            continue

        continuar = input("Deseja continuar testando? (sim/não): ")
        if continuar.lower() not in ["sim", "s"]:
            break

if __name__ == "__main__":
    main()
