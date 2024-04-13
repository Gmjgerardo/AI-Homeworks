# Importación de módulos para operaciones numéricas y graficación
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def main() -> None:
    # Creamos una figura
    fig = plt.figure()
    # Definimos los ejes para que sean una proyección 3d
    ax = fig.add_subplot(projection='3d')

    b = 100
    def f(x, y): return b*((x)**4 + (y)**4)

    # Generamos el rango para la función según los valores indicados por la función. Como tercer parámetro definimos cada cuanto queremos que haya un punto, mientras más pequeño el valor más fina la gráfica.
    # Para graficar en volumen necesitamos dos dimensiones x, y
    X = np.arange(-1.28, 1.28, 0.1)
    Y = np.arange(-1.28, 1.28, 0.1)
    # Generamos una maya con los valores de x, y
    X, Y = np.meshgrid(X, Y)
    # Calculamos el valor de la altura (la tercer dimensión) según lo descrito por la función esfera, es decir la suma del cuadrado de cada dimensión
    Z = f(X, Y)

    # Creamos la superficie a graficar
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=1)
    # Agregamos una barra de color como indicativo de los valores en la función
    fig.colorbar(surf)

    # Graficamos el resultado
    plt.show()


if __name__ == '__main__':
    main()
