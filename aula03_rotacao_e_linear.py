# -*- coding: utf-8 -*-
# AULA - Parte III (Matrizes), slide 9:
# "Exemplo de Transformacao Linear: Rotacoes de vetores n-dimensionais;
#  Outros Exemplos: experimentar no Python..."
# Aqui: confiro no Python que a rotacao no plano respeita a propriedade
# T(a*x1 + b*x2) = a*T(x1) + b*T(x2).
import numpy as np


def rotacao(theta_graus):
    # Matriz que gira um vetor do R^2 de theta graus, sentido anti-horario.
    t = np.radians(theta_graus)
    return np.array([[np.cos(t), -np.sin(t)],
                     [np.sin(t),  np.cos(t)]])


R = rotacao(30)
x1 = np.array([1.0, 2.0])
x2 = np.array([-3.0, 0.5])
a, b = 2.0, -1.5

lado_esquerdo = R @ (a * x1 + b * x2)
lado_direito = a * (R @ x1) + b * (R @ x2)

print("T(a*x1 + b*x2)   =", lado_esquerdo)
print("a*T(x1) + b*T(x2) =", lado_direito)
print("e linear?", np.allclose(lado_esquerdo, lado_direito))
