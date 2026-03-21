# Trabajo Práctico 0 - Teoría de Algoritmos

Este proyecto contiene la implementación y el análisis de algoritmos para la resolución del problema de **Números Amigos**, comparando una versión nativa de Python frente a una versión optimizada.

## Requisitos previos

* **Python 3.10+**
* **Make**
* **pdfLaTeX**

## Informe
Podés leer el análisis detallado de complejidad y performance en el siguiente enlace:
* [Ver Informe Final (PDF)](./Informe/informe.pdf)

## Instalación y Configuración

El proyecto utiliza un entorno virtual (`venv`) para gestionar las dependencias de forma aislada. Para configurar el entorno e instalar las librerías necesarias (`numpy` y `matplotlib`), ejecutá:

```bash
make install
```
Este comando:

- Crea la carpeta `venv/`.
- Actualiza `pip`.
- Instala `numpy` y `matplotlib`.

## Comandos disponibles
```bash
make run
```
Ejecuta la lógica principal en `amigos.py` (código optimizado)

```bash
make graphics
```
Genera los gráficos de performance en la carpeta `Graficos/`
```bash
make pdf
```
Compila el informe LaTeX

```bash
make clean
```
Borra el venv, la carpeta build del informe y los archivos __pycache__.
