# -*- coding: utf-8 -*-
# AULA - Parte VII (Aritmetica de ponto flutuante), slide 7:
# "A precisao da maquina (eps) e 2^-52. Em Python:" (codigo do slide)

# Import numpy
import numpy as np

# Print the machine epsilon
print("Machine epsilon:\n", np.finfo(float).eps)

# Conferencia: eps = 2^-52, e 1 + eps e o primeiro numero depois de 1
print("eps == 2**-52 ?", np.finfo(float).eps == 2.0 ** -52)
print("1 + eps > 1 ?", 1.0 + 2.0 ** -52 > 1.0)
print("1 + eps/2 > 1 ?", 1.0 + 2.0 ** -53 > 1.0)
