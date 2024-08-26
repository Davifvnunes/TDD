def retangulos_colidem(rect1, rect2):
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

    # Validando os retângulos
    if not validar_retangulo(rect1) or not validar_retangulo(rect2):
        return None
    
    # Extraindo as coordenadas dos vértices na ordem especificada
    (x1_min, y1_max), (x1_max, _), (_, y1_min), (_, _) = rect1
    (x2_min, y2_max), (x2_max, _), (_, y2_min), (_, _) = rect2
    
    # Verificando a colisão:
    colidem = not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)
    
    return colidem

# Exemplo de uso:
rect1 = ((1, 3), (4, 3), (4, 1), (1, 1))
rect2 = ((2, 5), (6, 5), (6, 2), (2, 2))

print(retangulos_colidem(rect1, rect2))
