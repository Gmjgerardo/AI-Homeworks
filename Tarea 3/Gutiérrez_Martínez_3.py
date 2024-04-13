# Importación de módulos para operaciones numéricas y graficación
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # Funciones de la tarea a evaluar
    listaFunciones = [[1, -4, 1, 6], [6, -12, 5, -2], [(1/3), 8, 63, 7]]

    for i in range(3):
        # Obtener el polinomio a resolver, iterando la lista de funciones de la tarea
        polinomio = listaFunciones[i]

        # Convertir la lista a un objeto polinomial para trabajar con el
        poly = np.poly1d(polinomio)
        primer_derivada = np.polyder(poly, 1)
        segunda_derivada = np.polyder(poly, 2)
        raices = np.roots(primer_derivada)
        # Evaluar el polinomio con las raíces
        valores = np.polyval(poly, raices)
        # Evaluar la segunda derivada (Obtener máximo y mínimo)
        valores2d = np.polyval(segunda_derivada, raices)

        # Obtener rango para x en base a las raíces obtenidas
        mayor = np.max(raices) + 0.5
        menor = np.min(raices) - 0.5
        # 100 puntos en x para evaluar
        x = np.linspace(menor, mayor, 120)
        # Valores de en la función
        y = np.polyval(poly, x)

        # Crear cadena con los datos de función actual
        mostrarFuncion = '{0}x³{1:+}x²{2:+}x{3:+}'.format(*polinomio)

        # Muestra de las gráficas
        plt.figure(i + 1)                   # Crear una nueva figura
        plt.title(mostrarFuncion)           # Título: Función original
        # Función evaluada en 100 puntos (rojo)
        plt.plot(x, y, 'r')
        # Puntos estacionarios (asterisco verde)
        plt.plot(raices, valores, '*g')

        plt.annotate(("Máximo" if valores2d[0] < 0 else "Mínimo") + " ({:.2f}, {:.2f})".format(raices[0], valores[0]),
                     xy=[raices[0], valores[0]])

        plt.annotate(("Máximo" if valores2d[1] < 0 else "Mínimo") + " ({:.2f}, {:.2f})".format(raices[1], valores[1]),
                     xy=[raices[1], valores[1]])

    plt.show()


if __name__ == '__main__':
    main()
