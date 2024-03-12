#import numpy as np

x = int(input("Digite o tipo de dados a serem somados: "))
y = int(input("Digite o número de dados a serem somados: "))
z = int(input("Digite o valor resultante desejado: "))

c = 0
cont = 0

while c < y - 1:

  # variável do resultado da potencia
  p = x ** (c+1)

  # Inicializando a matriz
  matriz = [[0 for _ in range(x**(c+1))] for _ in range(x)]

  if c == 0:
    # Inicializando a variável a
    a = 0

    while a < x:
        # Inicializando a variável b
        b = 0
        while b < p:
          matriz[a][b] = a+1 + b+1
          if matriz[a][b] >= z:
           cont += 1
          b += 1
        a += 1

  if c > 0:
    cont = 0
    a = 0

    while a < x:

      b = 0
      while b < p:
        matriz[a][b] = vetor[b] + a+1

        if matriz[a][b] >= z:
          cont += 1
        b += 1
      a += 1
  c += 1

  for linha in matriz:
      print("\t".join(map(str, linha)))

  vetor = []

  vetor = [elemento for linha in matriz for elemento in linha]

  vetor = sorted(vetor)

  print("\n", vetor, "\n")

print("\nA probabilidade de o valor desejado acontecer é de:\n", (cont / (x**y)) * 100, "%")

  #matriz = np.array([vetor, vetor_comp])

  #for linha in matriz:
      #print("\t".join(map(str, linha)))