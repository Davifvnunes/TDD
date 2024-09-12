import module
import unittest

"""
LIST em module main

estudantes = [{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
		{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
		{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]
"""

# RECEBIDOS EM DICT
class FiltarEstudantes(unittest.TestCase):
    def test_estudate_aprovado(self):
        self.assertEqual(module.filtrar_aprovados(module.estudantes[2]), True)

unittest.main()   