# -*- coding: utf-8 -*-
# P1 de Algebra Linear Computacional, QUESTAO 5.
# Resolve A x = b pela decomposicao A = L U, sem pivoteamento.
# Do numpy so uso np.array, np.eye e np.zeros, como manda o enunciado.
import numpy as np


def decomposicao_lu(A, tol=1e-12, mostrar=False):
    # Monta L e U pela eliminacao de Gauss.
    # U comeca como uma copia de A e vai sendo zerada abaixo da diagonal.
    # L comeca como a identidade (1 na diagonal) e guarda os multiplicadores.
    # tol: pivo menor que isso conta como zero (erro de arredondamento).
    # mostrar=True imprime cada multiplicador e onde ele entra em L.
    n = len(A)
    U = np.array(A, dtype=float)
    L = np.eye(n)

    for k in range(n):                      # k = coluna que estou zerando
        if abs(U[k, k]) < tol:
            raise Exception(
                "Pivo nulo na posicao (%d, %d). A decomposicao LU sem "
                "pivoteamento nao funciona para esta matriz: use uma funcao "
                "alternativa, com pivoteamento, para resolver o sistema."
                % (k + 1, k + 1))

        for i in range(k + 1, n):           # i = cada linha abaixo do pivo
            m = U[i, k] / U[k, k]           # multiplicador
            L[i, k] = m                     # o multiplicador vai para L
            if mostrar:
                print("m = %g / %g = %g  ->  L[%d,%d] = %g"
                      % (U[i, k], U[k, k], m, i + 1, k + 1, m))
            U[i, k] = 0.0                   # a posicao abaixo do pivo vira zero
            for j in range(k + 1, n):       # linha i = linha i - m * linha k
                U[i, j] = U[i, j] - m * U[k, j]

    return L, U


def substituicao_progressiva(L, b):
    # Resolve L y = b de cima para baixo.
    # A diagonal de L e toda 1, entao nao precisa dividir.
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        soma = 0.0
        for j in range(i):                  # so o que ja foi calculado
            soma = soma + L[i, j] * y[j]
        y[i] = b[i] - soma
    return y


def substituicao_regressiva(U, y):
    # Resolve U x = y de baixo para cima.
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, n):           # so o que ja foi calculado
            soma = soma + U[i, j] * x[j]
        x[i] = (y[i] - soma) / U[i, i]
    return x


def resolve_lu(A, b):
    # A = L U, depois L y = b, depois U x = y.
    L, U = decomposicao_lu(A)
    y = substituicao_progressiva(L, b)
    x = substituicao_regressiva(U, y)
    return L, U, x


if __name__ == "__main__":
    A = np.array([[2.0, 1.0, 1.0],
                  [4.0, 3.0, 3.0],
                  [8.0, 7.0, 9.0]])
    b = np.array([4.0, 10.0, 24.0])

    print("Multiplicadores da eliminacao:")
    decomposicao_lu(A, mostrar=True)

    L, U, x = resolve_lu(A, b)
    print("L =")
    print(L)
    print("U =")
    print(U)
    print("x =", x)
