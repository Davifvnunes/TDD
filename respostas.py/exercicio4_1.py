separador = ("=========================")
divisoria = ("_________________________")

def obter_retangulo():
    while True:
        print("Por favor, insira as coordenadas dos 4 vértices do retângulo na seguinte ordem:")
        print("1. Vértice Superior Esquerdo")
        print("2. Vértice Superior Direito")
        print("3. Vértice Inferior Direito")
        print("4. Vértice Inferior Esquerdo")
        print(separador)
        
        nomes_vertices = [
            "Vértice Superior Esquerdo",
            "Vértice Superior Direito",
            "Vértice Inferior Direito",
            "Vértice Inferior Esquerdo"
        ]
        
        vertices = []
        for nome in nomes_vertices:
            while True:
                try:
                    vertice = input(f"{nome} (formato: x,y): ")
                    print(separador)
                    x, y = map(float, vertice.split(","))
                    vertices.append((x, y))
                    break
                except ValueError:
                    print("Entrada inválida! Certifique-se de usar o formato correto (x,y) e que x e y sejam números reais.")
                    print(separador)
        
        print(f"Retângulo inserido: {vertices}")
        confirmacao = input("Este é o retângulo que você queria? (s/n): ").strip().lower()
        
        if confirmacao == 's':
            return tuple(vertices)
        else:
            print("Vamos tentar novamente.\n")

# Obter os dois retângulos do usuário
retangulo1 = obter_retangulo()
print(f"Retângulo 1 confirmado: {retangulo1}")
print(divisoria)

retangulo2 = obter_retangulo()
print(f"Retângulo 2 confirmado: {retangulo2}")
print(divisoria)

# Função para verificar se os retângulos colidem
def retangulos_colidem(rect1, rect2):
    def validar_retangulo(ret):
        # Verifica se o retângulo é válido: 4 vértices, cada um como tupla de 2 valores numéricos.
        if len(ret) != 4:
            print(f"Erro: Retângulo {ret} não possui 4 vértices.")
            return False
        for vertice in ret:
            if not (isinstance(vertice, tuple) and len(vertice) == 2 and all(isinstance(coord, (int, float)) for coord in vertice)):
                print(f"Erro: Vértice {vertice} no retângulo {ret} é inválido.")
                return False
        return True

    # Validando os retângulos
    if not validar_retangulo(rect1) or not validar_retangulo(rect2):
        return None
    
    # Extraindo as coordenadas dos vértices
    (x1_min, y1_max), (x1_max, _), (_, y1_min), (_, _) = rect1
    (x2_min, y2_max), (x2_max, _), (_, y2_min), (_, _) = rect2
    
    # Verificando a colisão:
    colidem = not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)
    
    return colidem

# Verificar colisão entre os retângulos e imprimir o resultado booleano
print(retangulos_colidem(retangulo1, retangulo2)) 

