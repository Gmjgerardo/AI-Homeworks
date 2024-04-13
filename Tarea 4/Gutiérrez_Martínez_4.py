# Importación de módulos para operaciones numéricas y graficación
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from os import system   # Función para limpiar la consola
from time import sleep  # Función para hacer pausas en la ejecución del programa


def sphere() -> None:
    # Creamos una figura
    fig = plt.figure('Función Sphere')
    # Definimos los ejes para que sean una proyección 3d
    ax = fig.add_subplot(projection='3d')

    # Generamos el rango para la función según los valores indicados por la función. Como tercer parámetro definimos cada cuanto queremos que haya un punto, mientras más pequeño el valor más fina la gráfica.
    # Para graficar en volumen necesitamos dos dimensiones x, y
    X = np.arange(-5.12, 5.12, 0.1)
    Y = np.arange(-5.12, 5.12, 0.1)
    # Generamos una maya con los valores de x, y
    X, Y = np.meshgrid(X, Y)
    # Calculamos el valor de la altura (la tercer dimensión) según lo descrito por la función esfera, es decir la suma del cuadrado de cada dimensión
    Z = X**2 + Y**2

    # Creamos la superficie a graficar
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=1)
    # Agregamos una barra de color como indicativo de los valores en la función
    fig.colorbar(surf)

    # Graficamos el resultado
    plt.show()


def rosenbrock() -> None:
    # Creamos una figura
    fig = plt.figure('Función Rosenbrock')
    # Definimos los ejes para que sean una proyección 3d
    ax = fig.add_subplot(projection='3d')

    # Generamos el rango para la función según los valores indicados por la función. Como tercer parámetro definimos cada cuanto queremos que haya un punto, mientras más pequeño el valor más fina la gráfica.
    # Para graficar en volumen necesitamos dos dimensiones x, y
    X = np.arange(-2.048, 2.048, 0.1)
    Y = np.arange(-2.048, 2.048, 0.1)
    # Generamos una maya con los valores de x, y
    X, Y = np.meshgrid(X, Y)
    # Calculamos el valor de la altura (la tercer dimensión) según lo descrito por la función esfera, es decir la suma del cuadrado de cada dimensión
    Z = (100 * (Y - (X**2))**2) + (X - 1)**2

    # Creamos la superficie a graficar
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
    # Agregamos una barra de color como indicativo de los valores en la función
    fig.colorbar(surf)

    # Graficamos el resultado
    plt.show()


def rastrigin():
    # Creamos una figura
    fig = plt.figure('Función Rastrigin')
    # Definimos los ejes para que sean una proyección 3d
    ax = fig.add_subplot(projection='3d')

    # Generamos el rango para la función según los valores indicados por la función. Como tercer parámetro definimos cada cuanto queremos que haya un punto, mientras más pequeño el valor más fina la gráfica.
    # Para graficar en volumen necesitamos dos dimensiones x, y
    X = np.arange(-5.12, 5.12, 0.1)
    Y = np.arange(-5.12, 5.12, 0.1)
    pi = np.pi  # Constante PI

    # Generamos una maya con los valores de x, y
    X, Y = np.meshgrid(X, Y)
    # Calculamos el valor de la altura (la tercer dimensión) según lo descrito por la función esfera, es decir la suma del cuadrado de cada dimensión
    Z = 20 + X**2 - 10 * np.cos(2 * pi * X)  # X1
    Z += Y**2 - 10 * np.cos(2 * pi * Y)     # X2

    # Creamos la superficie a graficar
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
    # Agregamos una barra de color como indicativo de los valores en la función
    fig.colorbar(surf)

    # Graficamos el resultado
    plt.show()


def quartic():
    # Creamos una figura
    fig = plt.figure('Función Quartic')
    # Definimos los ejes para que sean una proyección 3d
    ax = fig.add_subplot(projection='3d')

    # Generamos el rango para la función según los valores indicados por la función. Como tercer parámetro definimos cada cuanto queremos que haya un punto, mientras más pequeño el valor más fina la gráfica.
    # Para graficar en volumen necesitamos dos dimensiones x, y
    X = np.arange(-1.28, 1.28, 0.05)
    Y = np.arange(-1.28, 1.28, 0.05)

    # Generamos una maya con los valores de x, y
    X, Y = np.meshgrid(X, Y)
    # Calculamos el valor de la altura (la tercer dimensión) según lo descrito por la función esfera, es decir la suma del cuadrado de cada dimensión
    Z = X**4 + (2 * (Y**4))

    # Creamos la superficie a graficar
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
    # Agregamos una barra de color como indicativo de los valores en la función
    fig.colorbar(surf)

    # Graficamos el resultado
    plt.show()


def main() -> None:
    # Diccionario con las funciónes cargadas
    funciones = {0: sphere, 1: rosenbrock, 2: rastrigin, 3: quartic}

    while True:
        # Limpiar la consola
        system('cls')

        # Menú de opciones
        print('\t---- Tarea 4: Funciones para probar algoritmos ----')
        print('0) Función Sphere')
        print('1) Función Rosenbrock')
        print('2) Función Rastrigin')
        print('3) Función Quartic')
        ejecutar = int(
            input('Ingresa el valor de la función que deseas ejecutar: \n'))

        # Validar que se haya ingresado un número valido
        if (ejecutar >= 0 and ejecutar < 4):
            # Ejecutar la función que se haya seleccionado
            funciones[ejecutar]()

            # Validar si se desea continuar con la ejecución
            if (int(input('¿Deseas probar otra función? 0) NO \t 1) SI  \n')) == 0):
                break   # En caso de que no, terminar el ciclo y con ello el programa
        else:
            print('Opción NO valida, intente de nuevo')
            sleep(1)    # Agregar un delay para que se pueda ver el mensaje


if (__name__ == '__main__'):
    main()
