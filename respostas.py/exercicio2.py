import numpy as np
from math import gcd

def criar_matriz_especial(m, n):
    # Verifica se m e n são primos entre si e se m < n
    if gcd(m, n) != 1 or m >= n:
        print("m e n devem ser primos entre si e m deve ser menor que n.")
        return None
    
    # Cria uma matriz vazia de tamanho n x n
    matriz = np.zeros((n, n), dtype=int)
    
    # Preenche a matriz
    num = 1
    i = 0
   
    while num <= n * n:
        # Divisão do indice pelo tamanho da matrz, isso dará a linha em que num vai ficar
        linha = i // n
        #Restante da divisão de i por n dará a coluna
        coluna = i % n   
        matriz[linha, coluna] = num
        num += 1
       # Atualização do indice, primeiro soma  com m e depois tomamos o modulo de n^2 para que o 
       # indice circule dentro do intervalo (0, n^2-1) 
        i = (i + m) % (n * n)

    return matriz

def obter_entradas():
    while True:
        try:
            m = int(input("Digite o valor de m (um número natural): "))
            n = int(input("Digite o valor de n (um número natural): "))

            if m <= 0 or n <= 0:
                print("m e n devem ser números naturais não nulos.")
                continue
            
            if m > n:
                resposta = input(f"m ({m}) é maior que n ({n}). Deseja trocá-los? (s/n): ").strip().lower()
                if resposta == 's':
                    m, n = n, m
                else:
                    print("Insira novos valores para m e n.")
                    continue
            
            if gcd(m, n) != 1:
                print("m e n devem ser primos entre si.")
                continue

            return m, n

        except ValueError:
            print("Por favor, insira números naturais válidos.")

def main():
    while True:
        m, n = obter_entradas()
        matriz = criar_matriz_especial(m, n)
        if matriz is not None:
            print("Matriz gerada com sucesso:")
            print(matriz)
            break  # Sai do loop se a matriz foi gerada com sucesso
        else:
            print("Tente novamente.\n")

# Inicia o programa
main()
