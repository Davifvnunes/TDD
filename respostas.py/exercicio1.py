def achar_triangulos_com_perimetro(p):
    triangulos = []
    # Iterar sobre possíveis valores de a, b e c
    for a in range(1, p // 3):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                triangulos.append((a, b, c))
    return triangulos

def achar_o_maximo_de_triangulos(n):
    if not isinstance(n, int):
        print("A função só recebe inteiros.")
        return None

    max_contavel = 0
    max_p = 0
    max_triangulos = []

    for p in range(1, n + 1):
        triangulos = achar_triangulos_com_perimetro(p)
        triangulos_contavel = len(triangulos)
        if triangulos_contavel > max_contavel:
            max_contavel = triangulos_contavel
            max_p = p
            max_triangulos = triangulos

    return max_p, max_triangulos

def Obter_n():
    while True:
        try:
            x = int(input("Digite um número inteiro positivo: "))
            if x <= 0:
                print(f"O valor {x} não é positivo. Tente novamente.")
            else:
                return x
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# Obtém o valor de n
x = Obter_n()

# Encontra o perímetro com o maior número de triângulos retângulos e os triângulos correspondentes
max_p, triangulos = achar_o_maximo_de_triangulos(x)
print(f"Perímetro com o maior número de triângulos retângulos: {max_p}")
print("Triângulos retângulos encontrados (a, b, c):")
for triangulo in triangulos:
    print(triangulo)



