import time
import numpy as np


def amigos(MAX):
    t1 = time.time()

    tabla_sumas = np.ones(MAX + 1, dtype=np.int64)
    tabla_sumas[0] = 0
    tabla_sumas[1] = 0

    for divisor in range(2, MAX // 2 + 1):
        tabla_sumas[divisor * 2 :: divisor] += divisor

    numeros = np.arange(MAX + 1)
    es_candidato = (tabla_sumas > numeros) & (tabla_sumas <= MAX)
    lista_candidatos = np.where(es_candidato)[0]

    for n in lista_candidatos:
        suma_n = tabla_sumas[n]
        if tabla_sumas[suma_n] == n:
            print(n, suma_n)

    print(time.time() - t1)

amigos(100000)
