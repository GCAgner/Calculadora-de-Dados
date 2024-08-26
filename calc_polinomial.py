#versão 1.3 método polinomial

from sympy import symbols, expand
import re, time

def contar_repeticoes_e_somar(polinomio, limite_expoente):
    # Inicializa um dicionário para armazenar o número de ocorrências para cada par de valores
    contagem_valores = {}
    soma_valores_e = 0

    # Procura padrões de valores no polinômio usando expressões regulares
    padrao_valores = r'(?:(\d+)\*)?e\*\*\((\d+)\*t\)'
    matches = re.findall(padrao_valores, polinomio)

    # Itera sobre os valores encontrados
    for match in matches:
        valor_e, expoente_t = map(lambda x: int(x) if x else 1, match)
        if expoente_t >= limite_expoente:
            soma_valores_e += valor_e
            # Se o expoente for maior que o limite, atualiza a contagem
            contagem_valores[(valor_e, expoente_t)] = contagem_valores.get((valor_e, expoente_t), 0) + 1

    return soma_valores_e, contagem_valores

def calcular_combinacoes_iguais(w, y, z):

    inicio = time.time()

    e, t = symbols('e t')

    somatorio = 0

    for i in range(1, y+1):
        somatorio += e**(i*t)

    print(somatorio)
    print("\n")

    produto = 1

    for i in range(z):
        produto = produto * somatorio
        demonstracao = expand(produto)
        print(demonstracao)

    print("\n")

    produto_expandido = expand(produto)

    print(produto_expandido)

    # Chamada da função para contar as repetições e somar os valores de e
    soma_valores_e, contagem = contar_repeticoes_e_somar(str(produto_expandido), w)

    duracao = time.time() - inicio  # Calcula a duração da execução
    print(f"\nTempo necessário para calcular: {duracao:} segundos")

    # Imprime a soma dos valores de e
    print("Soma dos valores de e cujo expoente:", soma_valores_e)

    # Imprime o resultado da contagem
    print("Contagem de repetições para valores e expoentes:")
    for valores, quantidade in contagem.items():
        valor_e, expoente_t = valores
        print("Valor de e:", valor_e, "- Expoente de t:", expoente_t)
    print("Probabilidade da combinação desejada = ", ((soma_valores_e/(y**z))*100), "%")

def calcular_combinacoes_diferentes(z, w, vetor):

    inicio = time.time()

    e, t = symbols('e t')

    combinacoes = 1

    for valor in vetor:
        combinacoes *= valor

    produto = 1

    for i in range(z):
        somatorio = 0
        posicao = vetor[i]

        for j in range(posicao):
            somatorio += e**((j+1)*t)

        produto = produto * somatorio
        demonstracao = expand(produto)
        print(demonstracao)

    print("\n")

    produto_expandido = expand(produto)

    print(produto_expandido)

    # Chamada da função para contar as repetições e somar os valores de e
    soma_valores_e, contagem = contar_repeticoes_e_somar(str(produto_expandido), w)

    duracao = time.time() - inicio  # Calcula a duração da execução
    print(f"\nTempo necessário para calcular: {duracao:} segundos")

    # Imprime a soma dos valores de e
    print(f"Soma dos valores de e cujo expoente excede {w}: {soma_valores_e}")

    # Imprime o resultado da contagem
    print("Contagem de repetições para valores e expoentes:")
    for valores, quantidade in contagem.items():
        valor_e, expoente_t = valores
        print(f"Valor de e: {valor_e} - Expoente de t: {expoente_t}")

    print(f"Probabilidade da combinação desejada = {(soma_valores_e / combinacoes) * 100:} %")

def main():
    while True:
        x = int(input("Os dados são considerados iguais?\n [0] sim\n [1] não\n"))

        if x == 0:
            z = int(input("Quantos dados estão sendo comparados?\n"))
            w = int(input("Qual o valor desejado nos dados?\n"))
            y = int(input("Quantos lados tem os dados a serem comparados?\n"))

            calcular_combinacoes_iguais(w, y, z)

        elif x == 1:
            z = int(input("Quantos dados estão sendo comparados?\n"))
            w = int(input("Qual o valor desejado nos dados?\n"))
            vetor = []

            for i in range(z):
                valor_dado = int(input(f"Digite o número de lados do dado {i+1}: "))
                vetor.append(valor_dado)

            calcular_combinacoes_diferentes(z, w, vetor)

        else:
            print("Opção inválida. Por favor, escolha 0 ou 1.")
            continue

        continuar = input("Deseja continuar testando? (sim/não): ")
        if continuar.lower() not in ["sim", "s"]:
            break

if __name__ == "__main__":
    main()
