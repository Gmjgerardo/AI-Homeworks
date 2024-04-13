import os
# Importar algoritmo genetico
from AlgoritmoGeneticoBinario import AlgoritmoGeneticoBinario as AG
# Importar problema
from PTamanios import PTamanios

def main() -> None:
    # Inicialización de variables para el problema
    listaTamanios = [13, 8, 25, 4, 18, 6, 33, 22, 45, 11, 76, 10, 1]
    limiteSuperior = 211

    # Inicialización de variables para el algoritmo genético
    cantIndividuos = len(listaTamanios)
    tamanioGen = 1
    generaciones = 100
    factorMutacion = 0.1
    problema = PTamanios(listaTamanios, limiteSuperior) # Instanciación del problema

    # Instanciación del algoritmo genético binario
    ag = AG(cantIndividuos + 1, cantIndividuos,  tamanioGen, generaciones, factorMutacion, problema)

    # Mostrar mensajes por consola
    os.system('Color F9')
    print('\t---- Inteligencia Artificial 1: Segundo Examen Parcial ----')

    # Iniciar el funcionamiento del algoritmo
    indicesSolucion = ag.run()

    # Mostrar solución
    print('Se deben seleccionar los objetos con pesos:')
    for i in range(cantIndividuos):
        if indicesSolucion[i]:
            print(listaTamanios[i], end=' ')

    input('\n\nPresione cualquier tecla para salir...')

if __name__ == "__main__":
    main()