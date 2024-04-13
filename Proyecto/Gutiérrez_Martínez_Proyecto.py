# Importación de módulos para operaciones numéricas y graficación
import numpy as np
import matplotlib.pyplot as plt
from os import system   # Función para limpiar la consola
from time import sleep  # Función para hacer pausas en la ejecución del programa

# Importación de módulos con los problemas a resolver
import DE
from rosenbrock import Rosenbrock

def main() -> None:
    # Instanciar el problema a solucionar
    problema = Rosenbrock()

    while True:
        # Limpiar la consola
        system('cls')

        # Menú de opciones
        print('\t---- Inteligencia Artificial I: Proyecto ----')
        # Rango para el eje X (graficar generaciones)
        generaciones = np.array(list(range(0, 2000 + 1, 100)))
        
        # Dimensión actual
        dimension = 8
        print(f'\n\nDimensión {dimension}: ')
        resultados = []

        for ejecucion in range(5):
            print(f'Ejecución {ejecucion + 1}:')

            # Instanciar el algoritmo genético con el problema seleccionado
            de = DE.DE(30, dimension, F=0.4, c=0.1, problema=problema, generaciones=2000)

            # Obtener soluciones para el problema y almacenarlos en una lista
            resultados.append(de.run())

        # Obtener promedios, sumando los elementos de las ejecuciones y diviendolas entre 5 (n ejecuciones)
        # Multiplicar por -1 para que la graficación sea descendente
        promediosGeneracionales = (np.add.reduce(resultados)) / 5

        # Figura a mostrar
        plt.figure(1)

        # Nombre de la figura
        plt.title('Función Rosenbrock')

        # Graficar en 2D
        plt.plot(generaciones, promediosGeneracionales)

        plt.show()

        # Validar si se desea continuar con la ejecución
        if (int(input('¿Deseas probar otra función? 0) NO \t 1) SI  \n')) == 0):
            break   # En caso de que no, terminar el ciclo y con ello el programa

if __name__ == '__main__':
    main()
