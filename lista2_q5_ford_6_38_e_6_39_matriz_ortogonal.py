# Lista 2 - 5a Questao - [FORD] Exercicios 6.38 e 6.39
# Rafael Tadeu Basilio Gomes - ED 26205
import numpy as np

# margem de tolerancia: as matrizes do livro tem 5 casas
TOL = 1e-4


def is_orthogonal_by_definition(A):
    """Funcao 1 - definicao matricial: A^T.A = I."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    produto = A.T @ A
    identidade = np.eye(n)
    return bool(np.allclose(produto, identidade,
                            rtol=0, atol=TOL))


def is_orthogonal_by_vectors(A):
    """Funcao 2 - ortonormalidade das colunas."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            prod = A[:, i] @ A[:, j]
            # regra 1: comprimento unitario (i = j)
            if i == j and abs(prod - 1) > TOL:
                return False
            # regra 2: perpendicularidade (i != j)
            if i != j and abs(prod) > TOL:
                return False
    return True


exercicios = {
    "6.38 P1": [[-0.40825,  0.43644,  0.80178],
                [-0.81650,  0.21822, -0.53452],
                [-0.40825, -0.87287,  0.26726]],
    "6.38 P2": [[-0.51450,  0.48507,  0.70711],
                [-0.68599, -0.72761,  0.00000],
                [ 0.51450, -0.48507,  0.70711]],
    "6.39 P1": [[-0.58835,  0.70206,  0.40119],
                [-0.78446, -0.37524, -0.49377],
                [-0.19612, -0.60523,  0.77152]],
    "6.39 P2": [[-0.47624, -0.42640,  0.30151],
                [ 0.087932, 0.86603, -0.40825],
                [-0.87491, -0.26112,  0.86164]],
}

print(f"{'matriz':<8} | {'by_definition':>13} | "
      f"{'by_vectors':>10}")
print("-" * 38)
for nome, M in exercicios.items():
    d = is_orthogonal_by_definition(M)
    v = is_orthogonal_by_vectors(M)
    print(f"{nome:<8} | {str(d):>13} | {str(v):>10}")
