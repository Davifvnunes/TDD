def todos_retangulos_colidem(**kwargs):
    def validar_retangulo(ret):
        """Verifica se o retângulo é válido: 4 vértices, cada um como tupla de 2 valores numéricos."""
        if len(ret) != 4:
            print(f"Erro: Retângulo {ret} não possui 4 vértices.")
            return False
        for vertice in ret:
            if not (isinstance(vertice, tuple) and len(vertice) == 2 and all(isinstance(coord, (int, float)) for coord in vertice)):
                print(f"Erro: Vértice {vertice} no retângulo {ret} é inválido.")
                return False
        return True

    def retangulos_colidem(rect1, rect2):
        """Verifica se dois retângulos colidem."""
        # Extraindo as coordenadas dos vértices na ordem especificada
        (x1_min, y1_max), (x1_max, _), (_, y1_min), (_, _) = rect1
        (x2_min, y2_max), (x2_max, _), (_, y2_min), (_, _) = rect2
        
        # Verificando a colisão:
        return not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)

    # Lista para armazenar os pares de retângulos que colidem
    colisoes = []

    # Verificando se o número de retângulos é adequado
    if len(kwargs) < 2:
        return colisoes

    # Validando todos os retângulos
    for nome, retangulo in kwargs.items():
        if not validar_retangulo(retangulo):
            return []

    # Comparando todos os pares de retângulos
    nomes_retangulos = list(kwargs.keys())
    for i in range(len(nomes_retangulos)):
        for j in range(i + 1, len(nomes_retangulos)):
            nome1 = nomes_retangulos[i]
            nome2 = nomes_retangulos[j]
            if retangulos_colidem(kwargs[nome1], kwargs[nome2]):
                colisoes.append((nome1, nome2))

    return colisoes

# Exemplo de uso:
rect1 = ((1, 3), (4, 3), (4, 1), (1, 1))
rect2 = ((2, 5), (6, 5), (6, 2), (2, 2))
rect3 = ((5, 6), (8, 6), (8, 4), (5, 4))
rect4 = ((7, 8), (9, 8), (9, 7), (7, 7))

result = todos_retangulos_colidem(ret1=rect1, ret2=rect2, ret3=rect3, ret4=rect4)
print(result)  # [('ret1', 'ret2'), ('ret3', 'ret4')]

