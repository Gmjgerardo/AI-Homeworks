import copy
import random
import numpy as np

class Individuo:
    def __init__(self, solucion):
        self._solucion = solucion           # xi
        self._prueba = np.copy(solucion)    # ui
        self._fitness = np.inf

class DE:
    def __init__(self,
    cantidad_individuos,
    dimensiones,
    F, # Parametro para mutación
    c, # Porcentaje de cruza
    problema,
    generaciones):
        self._cantidad_individuos = cantidad_individuos
        self._dimensiones = dimensiones
        self._f = F
        self._c = c
        self._problema = problema
        self._rango = self._problema.MAX_VALUE - self._problema.MIN_VALUE
        self._generaciones = generaciones
        self._individuos = []
        self._mejor = np.inf

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            solucion = np.random.random(size = self._dimensiones) * self._rango + self._problema.MIN_VALUE
            individuo = Individuo(solucion)
            individuo._fitness = self._problema.fitness(individuo._solucion)
            self._individuos.append(individuo)

            if individuo._fitness < self._mejor:
                self._mejor = individuo._fitness

    def run(self):
        self.crearIndividuos()
        mejoresFitness = np.array([])
        vi = None   # Vector de mutación

        generacion = 0
        while (generacion <= self._generaciones):
            for idx in range(len(self._individuos)):
                # Quitar idx de la lista de posibles selecciones
                rangoR = [i for i in range(len(self._individuos))]
                del rangoR[idx]
                # Obteniendo los valores aleatorios r1, r2 y r3 no repetidos
                r1, r2, r3 = random.sample(rangoR, 3)

                # Obtener el vector mutante (vi)
                vi = self._individuos[r1]._solucion + (self._f * (self._individuos[r2]._solucion - self._individuos[r3]._solucion))

                # Obtener un entero aleatorio para Jr
                Jr = random.randint(1, self._dimensiones)

                # Por cada dimensión j en dimensiones (Proceso de "cruza")
                for j in range(self._dimensiones):
                    # Obtener número flotante aleatorio (entre 0 y 1)
                    rcj = random.random()
                    
                    if (rcj < self._c) or (j == Jr):
                        # uij <- vij
                        self._individuos[idx]._prueba[j] = copy.deepcopy(vi[j])
                    else:
                        # uij <- xij
                        self._individuos[idx]._prueba[j] = copy.deepcopy(self._individuos[idx]._solucion[j])
                # Siguiente dimensión
            # Siguiente individuo

            for idx in range(self._cantidad_individuos):
                # Obtener fitness del vector prueba de cada individuo (ui)
                fitness_ui = self._problema.fitness(self._individuos[idx]._prueba)

                # Evaluar si es mejor que el fitness de la solución originial
                if fitness_ui < self._individuos[idx]._fitness:
                    self._individuos[idx]._solucion = np.copy(self._individuos[idx]._prueba)
                    self._individuos[idx]._fitness = copy.deepcopy(fitness_ui)

                    # Evaluar si es mejor que la mejor solución
                    if fitness_ui < self._mejor:
                        self._mejor = fitness_ui
            # Siguiente indice de "population"

            if generacion % 100 == 0:
                print(f'Generación {generacion}: {self._mejor : 5f}')
                mejoresFitness = np.append(mejoresFitness, [self._mejor])
                
            generacion += 1
            
        return mejoresFitness
