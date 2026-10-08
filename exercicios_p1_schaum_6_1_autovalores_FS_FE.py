# -*- coding: utf-8 -*-
# EXERCICIOS PARA A P1 (folha do professor), [Schaum] 6.1, item c):
# "Utilize o Python para notar que [F]_S e [F]_E tem os mesmos autovalores"
# F(x, y) = (2x + 3y, 4x - 5y), S = {(1, 2), (2, 5)}, E = base usual.
import numpy as np

# [F]_E: as imagens de e1 e e2 viram as COLUNAS
# F(1,0) = (2, 4)   e   F(0,1) = (3, -5)
F_E = np.array([[2.0, 3.0],
                [4.0, -5.0]])

# P: os vetores da base S nas colunas
P = np.array([[1.0, 2.0],
              [2.0, 5.0]])

# [F]_S = P^-1 [F]_E P
F_S = np.linalg.inv(P) @ F_E @ P

print("[F]_E =\n", F_E)
print("[F]_S =\n", np.round(F_S, 10))
print("autovalores de [F]_E:", np.sort(np.linalg.eigvals(F_E)))
print("autovalores de [F]_S:", np.sort(np.linalg.eigvals(F_S)))
print("sao os mesmos?",
      np.allclose(np.sort(np.linalg.eigvals(F_E)),
                  np.sort(np.linalg.eigvals(F_S))))
