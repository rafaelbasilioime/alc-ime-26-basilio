# alc-ime-26-basilio
Algebra Linear Computacional - PGED/IME 2026.2 - Prof. Maj Azevedo
Rafael Tadeu Basilio Gomes (ED 26205)

Codigos em Python pedidos na disciplina. O nome de cada arquivo diz de onde veio o pedido.

| arquivo | onde foi pedido | o que faz |
|---|---|---|
| `Questao 5 - P1 ALC 2026.2/alc-p1-Q5-basilio.py` + `alc-p1-Q5-basilio.mp4` (video, 1min27) | P1, 5a questao (para casa) | `resolve_lu`: decomposicao A = LU sem pivoteamento, substituicao progressiva e regressiva |
| `lista1_q4_substituicao_regressiva.py` | Lista I, 4a questao (e Parte IV, slide 11) | resolve Ux = b com U triangular superior; exception se houver zero na diagonal |
| `lista1_q5_robo_planar_dois_elos.py` | Lista I, 5a questao | posicao do efetuador final (L1 = 20 cm, L2 = 15 cm) e a matriz de transformacao 3x3 |
| `lista2_q4_ford_7_32_posto_e_norma_de_uvT.py` | Lista II, 4a questao ([FORD] 7.32) | A = u v^T tem posto 1 e norma 2 igual a norma(u) * norma(v) |
| `lista2_q5_ford_6_38_e_6_39_matriz_ortogonal.py` | Lista II, 5a questao ([FORD] 6.38 e 6.39) | `is_orthogonal_by_definition` e `is_orthogonal_by_vectors` |
| `aula03_matrizes_inversa_de_5_3_3_2.py` | Parte III (Matrizes), slide 11 | inversa de [[5, 3], [3, 2]] a mao, confirmada no numpy |
| `aula03_rotacao_e_linear.py` | Parte III (Matrizes), slide 9 | confere que a rotacao e uma transformacao linear |
| `aula07_epsilon_da_maquina.py` | Parte VII (Ponto flutuante), slide 7 | epsilon da maquina, eps = 2^-52 |
| `exercicios_p1_schaum_6_1_autovalores_FS_FE.py` | Exercicios para a P1, [Schaum] 6.1 c) | [F]_S e [F]_E tem os mesmos autovalores |

Para rodar: `python <arquivo>.py` (Python 3.11 com numpy).
