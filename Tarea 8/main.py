# Importación de módulos para operaciones numéricas y graficación
import numpy as np
import matplotlib.pyplot as plt
from os import system   # Función para limpiar la consola
from time import sleep  # Función para hacer pausas en la ejecución del programa

# Importación de módulos con los problemas a resolver
from sphere import Sphere
from rosenbrock import Rosenbrock
from rastrigin import Rastrigin
from quartic import Quartic
import AGC

def main() -> None:
    # Diccionario con las funciónes cargadas
    problemas = {0: [Sphere, 'Sphere'], 1: [Rosenbrock, 'Rosenbrock'], 2: [Rastrigin, 'Rastrigin'], 3: [Quartic, 'Quartic']}

    while True:
        # Limpiar la consola
        system('cls')

        # Menú de opciones
        print('\t---- Tarea 6: Algoritmo Genético Continuo ----')
        print('0) Función Sphere')
        print('1) Función Rosenbrock')
        print('2) Función Rastrigin')
        print('3) Función Quartic')
        ejecutar = int(
            input('Ingresa el valor del problema que deseas ejecutar: \n'))

        # Validar que se haya ingresado un número valido
        if (ejecutar >= 0 and ejecutar < 4):
            # Instanciar un nuevo objeto problema a resolver
            problema = problemas[ejecutar][0]()
            promediosGeneracionales = []    # Lista de promedios generacionales

            # Rango para el eje X (graficar generaciones)
            generaciones = np.array(list(range(0, 2000 + 1, 100)))
            
            for i in range(1, 4):
                # Dimensión actual
                dimension = 2**i
                print(f'\n\nDimensión {dimension}: ')
                resultados = []

                for ejecucion in range(5):
                    print(f'Ejecución {ejecucion + 1}:')

                    # Instanciar el algoritmo genético con el problema seleccionado
                    ag = AGC.AGC(64, dimension, 2000, 0.2, problema, maxim=False)

                    # Obtener soluciones para el problema y almacenarlos en una lista
                    resultados.append(ag.run())

                # Obtener promedios, sumando los elementos de las ejecuciones y diviendolas entre 5 (n ejecuciones)
                # Multiplicar por -1 para que la graficación sea descendente
                promediosGeneracionales.append(((np.add.reduce(resultados)) / 5) * -1)

                # Figura a mostrar
                plt.figure(i)

                # Nombre de la figura
                plt.title(f'Función {problemas[ejecutar][1]} ({dimension} dimensiones)')

                # Graficar en 2D
                plt.plot(generaciones, promediosGeneracionales[i - 1])

            # Cuarta figura (mostrar las 3 dimensiones anteriores)
            fig, ax = plt.subplots()
            plt.title(f'{problemas[ejecutar][1]}')
            ax.plot(generaciones, promediosGeneracionales[0], label='2 Dimensiones')
            ax.plot(generaciones, promediosGeneracionales[1], label='4 Dimensiones')
            ax.plot(generaciones, promediosGeneracionales[2], label='8 Dimensiones')
            ax.legend()

            plt.show()

            # Validar si se desea continuar con la ejecución
            if (int(input('¿Deseas probar otra función? 0) NO \t 1) SI  \n')) == 0):
                break   # En caso de que no, terminar el ciclo y con ello el programa
        else:
            print('Opción NO valida, intente de nuevo')
            sleep(1)    # Agregar un delay para que se pueda ver el mensaje

    """ s = Sphere()
    ag = AGC.AGC(256, 8 , 2000, 0.8, s, False) """

    """ s = Quartic()
    ag = AGC.AGC(64, 2, 2000, 0.2, s, maxim=False)
    ag.run() """

if __name__ == '__main__':
    main()
