# Lista 2 - 4a Questao - [FORD] Exercicio 7.32 em Python
# Rafael Tadeu Basilio Gomes - ED 26205
import numpy as np

# I - bloco de processos sobre as dimensoes
ms = [5, 15, 25]
np.random.seed(2026)  # repete os mesmos numeros

print(f"{'m':>3} | {'rank(A)':>7} | {'|u|.|v|':>10} | "
      f"{'|A|2':>10} | {'rank=1':>6} | {'iguais':>6}")
print("-" * 58)

for m in ms:
    # II - dois vetores coluna aleatorios de tamanho (m, 1)
    u = np.random.rand(m, 1)
    v = np.random.rand(m, 1)

    # III - matriz do produto externo A = u.v^T, de ordem m x m
    A = u @ v.T

    # IV - posto da matriz A (espera-se 1)
    posto = np.linalg.matrix_rank(A)

    # V - 2-norma de u e de v, e o produto das duas normas
    prod_normas = np.linalg.norm(u) * np.linalg.norm(v)

    # VI - 2-norma espectral de A: raiz do maior autovalor
    #      de A^T.A
    lam_max = np.max(np.linalg.eigvalsh(A.T @ A))
    norma_A = np.sqrt(lam_max)

    # VII - tabela comparativa
    igual = np.isclose(norma_A, prod_normas)
    print(f"{m:>3} | {posto:>7} | {prod_normas:>10.6f} | "
          f"{norma_A:>10.6f} | {str(posto == 1):>6} | "
          f"{str(igual):>6}")
