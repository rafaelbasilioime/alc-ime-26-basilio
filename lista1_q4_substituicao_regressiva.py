# -*- coding: utf-8 -*-
# LISTA 1, QUESTAO 4 - substituicao regressiva.
# Pedido em: Lista de Exercicios I, 4a questao (e exercicio do slide 11 da Parte IV, Equacoes Lineares).
import numpy as np


class DiagonalNulaError(Exception):
    # Levantada se a diagonal da triangular tem um zero.
    pass


def substituicao_regressiva(U, b, tol=1e-12):
    # Resolve U x = b, com U triangular superior,
    # percorrendo as linhas de baixo para cima.
    U = np.asarray(U, dtype=float)
    b = np.asarray(b, dtype=float).reshape(-1)
    n = U.shape[0]

    if U.shape[0] != U.shape[1]:
        raise ValueError("U precisa ser quadrada.")
    if b.shape[0] != n:
        raise ValueError(
            "b precisa ter o mesmo numero de linhas de U.")
    if np.any(np.abs(np.tril(U, -1)) > tol):
        raise ValueError("U nao e triangular superior.")

    # exigencia do enunciado: zero na diagonal -> exception
    for i in range(n):
        if abs(U[i, i]) <= tol:
            raise DiagonalNulaError(
                "Elemento nulo na diagonal, linha %d: "
                "o sistema nao tem solucao unica." % i)

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = float(U[i, i + 1:] @ x[i + 1:])
        x[i] = (b[i] - soma) / U[i, i]
    return x


if __name__ == "__main__":
    U = [[2.0, 1.0, 1.0],
         [0.0, 3.0, 2.0],
         [0.0, 0.0, 4.0]]
    b = [8.0, 11.0, 8.0]

    print(substituicao_regressiva(U, b))

    U[2][2] = 0.0
    try:
        print(substituicao_regressiva(U, b))
    except DiagonalNulaError as e:
        print(e)
