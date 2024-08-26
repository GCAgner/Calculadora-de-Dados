#versão 1.7 #método matricial

import time

# função para calcular probabilidades de dados com lados iguais
def calcula_igual(x, y, z):
    inicio = time.time()  # Registra o tempo inicial
    c = 0
    cont = 0
    vetor = list(range(1, x + 1))  # Inicializa o vetor para a primeira iteração

    while c < y - 1:
        p = len(vetor)  # O tamanho de p agora é o comprimento do vetor anterior
        matriz = [[0 for _ in range(p)] for _ in range(x)]

        if c == 0:
            a = 0
            while a < x:
                b = 0
                while b < p:
                    matriz[a][b] = vetor[b] + a + 1
                    if c == y - 2:
                        if matriz[a][b] >= z:
                            cont += 1
                    b += 1
                a += 1

        else:
            a = 0
            while a < x:
                b = 0
                while b < p:
                    matriz[a][b] = vetor[b] + a + 1
                    if c == y - 2:
                        if matriz[a][b] >= z:
                            cont += 1
                    b += 1
                a += 1

        c += 1

        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print('\t')

        vetor = [elemento for linha in matriz for elemento in linha]
        vetor = sorted(vetor)
        print("\n", vetor, "\n")

    print("total de combinações favoráveis:", cont)
    print("total de combinações possíveis", x ** y)
    print("\nA probabilidade de o valor desejado acontecer é de:\n", (cont / (x ** y)) * 100, "%")

    # Calcular a média
    media = sum(vetor) / len(vetor)
    print(f"Média dos valores: {media:}")

    # Calcular a variância
    variancia = sum((v - media) ** 2 for v in vetor) / len(vetor)
    print(f"Variância dos valores: {variancia:}")

    duracao = time.time() - inicio  # Calcula a duração da execução
    print(f"\nTempo necessário para calcular: {duracao:} segundos")


# função para calcular probabilidades de dados com lados diferentes
def calcula_diferente(y, z, vetor):
    inicio = time.time()  # Registra o tempo inicial
    c = 0
    cont = 0
    vetor_atual = list(range(1, vetor[0] + 1))  # Inicializa o vetor para a primeira iteração

    while c < y - 1:
        p = len(vetor_atual)  # O tamanho de p agora é o comprimento do vetor anterior
        matriz = [[0 for _ in range(p)] for _ in range(vetor[c + 1])]

        if c == 0:
            a = 0
            while a < vetor[c + 1]:
                b = 0
                while b < p:
                    matriz[a][b] = a + 1 + vetor_atual[b]
                    if c == y - 2:
                        if matriz[a][b] >= z:
                            cont += 1
                    b += 1
                a += 1

        else:
            a = 0
            while a < vetor[c + 1]:
                b = 0
                while b < p:
                    matriz[a][b] = vetor_atual[b] + a + 1
                    if c == y - 2:
                        if matriz[a][b] >= z:
                            cont += 1
                    b += 1
                a += 1

        c += 1

        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print('\t')

        vetor_atual = [elemento for linha in matriz for elemento in linha]
        vetor_atual = sorted(vetor_atual)
        print("\n", vetor_atual, "\n")

    print("total de combinações favoráveis:", cont)
    print("total de combinações possíveis", len(vetor_atual))
    print("\nA probabilidade de o valor desejado acontecer é de:\n", (cont / (len(vetor_atual))) * 100, "%")

    # Calcular a média
    media = sum(vetor_atual) / len(vetor_atual)
    print(f"Média dos valores: {media:}")

    # Calcular a variância
    variancia = sum((v - media) ** 2 for v in vetor_atual) / len(vetor_atual)
    print(f"Variância dos valores: {variancia:}")

    duracao = time.time() - inicio  # Calcula a duração da execução
    print(f"\nTempo necessário para calcular: {duracao:} segundos")


# função principal
def main():
    while True:
        resposta = int(input("Os dados são iguais ou diferentes? (0 = iguais, 1 = diferentes): "))
        print("\n")

        if resposta == 0:
            y = int(input("Digite a quantidade de dados: "))
            z = int(input("Digite o valor desejado: "))
            x = int(input("Digite o número de lados dos dados: "))

            calcula_igual(x, y, z)

        elif resposta == 1:
            y = int(input("Digite a quantidade de dados: "))
            z = int(input("Digite o valor desejado: "))
            vetor = []

            for i in range(y):  
                valor_dado = int(input(f"Digite o número de lados do dado {i + 1}: "))
                vetor.append(valor_dado)

            calcula_diferente(y, z, vetor)

        else:
            print("Opção inválida. Por favor, escolha 0 ou 1.")
            continue

        continuar = input("Deseja continuar testando? (sim/não): ")
        if continuar.lower() not in ["sim", "s"]:
            break

if __name__ == "__main__":
    main()
