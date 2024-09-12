estudantes = [{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
		{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
		{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]

def filtrar_aprovados(estudante):
    nota_soma = 0
    for nota in estudante["notas"]:
        nota_soma += nota    
    return nota_soma/  len(estudante["notas"]) >= 7