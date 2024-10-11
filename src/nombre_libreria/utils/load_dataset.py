from os.path import join
import sys
import numpy as np


"""
Objetivos del script:
- A partir de la lista de nombres de archivos (.npy) para características (features) y etiquetas (labels),
  cargar los datos en un TensorFlow Dataset.
- Realizar pruebas simples sobre el dataset cargado.
- Calcular el tamaño en memoria de los datasets cargados.
"""


def load_dataset(max_files, home):
    return 0


if __name__ == "__main__":
    home = join("..","..","..", "data")
    print(home)
    dataset = load_dataset(max_files=MAX_FILES, home=home)

    # Imprimir información básica del dataset para verificar
    for X, Y in dataset.take(5):  # Solo mostrar los primeros 5 elementos
        print("X:", X.numpy())
        print("Y:", Y.numpy())
