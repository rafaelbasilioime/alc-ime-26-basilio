# -*- coding: utf-8 -*-
# LISTA 1, QUESTAO 5 - robo planar de dois elos.
# Pedido em: Lista de Exercicios I, 5a questao, itens a) e b).
import numpy as np

L1, L2 = 20.0, 15.0


def posicao_efetuador(theta1_graus, theta2_graus):
    # Cinematica direta do manipulador planar de dois elos.
    # Recebe os angulos em graus e devolve (X, Y) em cm,
    # com 1 casa decimal.
    t1 = np.radians(theta1_graus)
    t2 = np.radians(theta2_graus)

    x = L1 * np.cos(t1) + L2 * np.cos(t1 + t2)
    y = L1 * np.sin(t1) + L2 * np.sin(t1 + t2)
    return round(float(x), 1), round(float(y), 1)


def matriz_transformacao(theta1_graus, theta2_graus):
    # Transformacao homogenea 3x3 do referencial da ponta
    # para o da base.
    t1 = np.radians(theta1_graus)
    t2 = np.radians(theta2_graus)
    s = t1 + t2
    return np.array([
        [np.cos(s), -np.sin(s), L1*np.cos(t1) + L2*np.cos(s)],
        [np.sin(s),  np.cos(s), L1*np.sin(t1) + L2*np.sin(s)],
        [0.0, 0.0, 1.0],
    ])


if __name__ == "__main__":
    for t1, t2 in [(0, 0), (90, 0), (0, 90), (45, 45), (30, 60), (90, 90)]:
        print(t1, t2, posicao_efetuador(t1, t2))

    print()
    print(np.round(matriz_transformacao(30, 60), 4))
