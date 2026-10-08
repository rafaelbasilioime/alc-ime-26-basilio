# -*- coding: utf-8 -*-
# AULA - Parte III (Matrizes), slide 11, exercicio:
# "Encontrar a inversa de A = [[5, 3], [3, 2]]. (Conseguimos confirmar a
#  resposta no Python/Numpy?)"
import numpy as np

A = np.array([[5.0, 3.0],
              [3.0, 2.0]])

# A mao: det(A) = 5*2 - 3*3 = 1, entao
# A^-1 = (1/det) * [[d, -b], [-c, a]] = [[2, -3], [-3, 5]]
A_inv_mao = np.array([[2.0, -3.0],
                      [-3.0, 5.0]])

# Confirmacao no numpy
A_inv_numpy = np.linalg.inv(A)

print("det(A) =", round(np.linalg.det(A), 10))
print("inversa feita a mao:\n", A_inv_mao)
print("inversa pelo numpy:\n", A_inv_numpy)
print("A @ A^-1 =\n", A @ A_inv_mao)
print("as duas batem?", np.allclose(A_inv_mao, A_inv_numpy))
