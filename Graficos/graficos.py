import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
import matplotlib.pyplot as plt

from amigos_refactorizado import amigos as amigos
from amigos_refactorizado import amigos_sin as amigos_nativo
# from amigos import amigos as amigos_original


def medir_rendimiento(config_funciones, n_values):
    resultados = {nombre: [] for nombre in config_funciones.keys()}

    for n in n_values:
        print(f"Procesando n={n}...", end="\r")
        for nombre, func in config_funciones.items():
            t_inicio = time.perf_counter()
            func(n)
            t_final = time.perf_counter()
            resultados[nombre].append(t_final - t_inicio)

    return resultados


def configurar_estetica_grafico(ax, y_max):
    ax.set_title("Tiempos de Ejecución: Números Amigos", fontsize=14, pad=15)
    ax.set_xlabel("Valor de MAX (n)", fontsize=12)
    ax.set_ylabel("Tiempo (segundos)", fontsize=12)

    margin = y_max * 0.15
    ax.set_ylim(0, y_max + margin)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()


def graficar_resultados(n_values, resultados):
    # Usamos un estilo limpio
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(12, 7))

    colores = {"numpy": "#1f77b4", "nativo": "#2ca02c"}
    marcadores = {"numpy": "o", "nativo": "s"}

    y_max = 0
    for nombre, tiempos in resultados.items():
        color = colores.get(nombre, "black")
        marker = marcadores.get(nombre, "o")

        ax.plot(
            n_values,
            tiempos,
            marker=marker,
            color=color,
            label=f"Algoritmo {nombre}",
            linewidth=2,
            markersize=8,
        )

        es_nativo = nombre == "nativo"

        for i, (n, t) in enumerate(zip(n_values, tiempos)):
            if n > 10000 and n < 500000 and i % 2 != 0:
                continue

            ax.annotate(
                f"{t:.3f}s",
                (n, t),
                textcoords="offset points",
                xytext=(0, 12 if es_nativo else -20),
                ha="center",
                va="bottom" if es_nativo else "top",
                fontsize=8,
                color=color,
                fontweight="bold",
                rotation=90,
            )

        y_max = max(y_max, max(tiempos))

    ax.set_title("Comparativa de Tiempos de Ejecución", fontsize=14, pad=20)
    ax.set_xlabel("Valor de MAX (n)", fontsize=12)
    ax.set_ylabel("Tiempo (segundos)", fontsize=12)

    ax.set_ylim(0, y_max * 1.2)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend(loc="upper left")

    plt.tight_layout()
    plt.show()


def main():
    N_VALUES = [10000, 50000, 100000, 150000, 200000, 250000, 500000, 1000000, 2000000]

    FUNCIONES_A_TESTEAR = {"numpy": amigos}

    print("Iniciando benchmark...")
    tiempos_obtenidos = medir_rendimiento(FUNCIONES_A_TESTEAR, N_VALUES)

    print("\nGenerando gráfico...")
    graficar_resultados(N_VALUES, tiempos_obtenidos)
    print("Proceso finalizado.")


if __name__ == "__main__":
    main()
