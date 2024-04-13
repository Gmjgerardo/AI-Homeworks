import copy
import random
import numpy as np

class Individuo:
    def __init__(self, solucion, velocidad):
        self._solucion = solucion
        self._velocidad = velocidad
        self._b = copy.deepcopy(solucion)
        self._b_fitness = np.inf

class DE:
    def __init__(self,
    cantidad_individuos,
    dimensiones,
    ro, #Tamaño de vecindad
    phi1_max,
    phi2_max,
    v_max,
    problema,
    generaciones):
        self._cantidad_individuos = cantidad_individuos
        self._dimensiones = dimensiones
        self._ro = ro
        self._phi1_max = phi1_max
        self._phi2_max = phi2_max
        self._v_max = v_max
        self._problema = problema
        self._generaciones = generaciones
        self._individuos = []
        self._rango = self._problema.MAX_VALUE - self._problema.MIN_VALUE
        self._mejor = np.inf
        self._mejoresFitness = np.array([])

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            solucion = np.random.random(size = self._dimensiones) * self._rango + self._problema.MIN_VALUE
            velocidad = np.random.random(size = self._dimensiones) * self._v_max * 2 + self._v_max
            individuo = Individuo(solucion, velocidad)
            individuo._b_fitness = self._problema.fitness(individuo._solucion)
            self._individuos.append(individuo)

    def mejorIndividuo(self):
        for i in self._individuos:
            fitness = self._problema.fitness(i._solucion)
            if fitness < self._mejor:
                self._mejor = fitness

    def run(self):
        self.crearIndividuos()
        self.mejorIndividuo()
        generacion = 0
        while (generacion <= self._generaciones):
            for idx in range(len(self._individuos)):
                # Quitar idx de la lista de posibles selecciones
                rangoR = [i for i in range(len(self._individuos))]
                del rangoR[idx]
                # Obteniendo los valores aleatorios r1, r2 y r3
                r1, r2, r3 = random.sample(rangoR, 3)
            
            if generacion % 100 == 0:
                #print(f'Generación {generacion}: {self._mejor : 5f}')
                self._mejoresFitness = np.append(self._mejoresFitness, [self._mejor])
                
            generacion += 1
            
        return self._mejoresFitness
