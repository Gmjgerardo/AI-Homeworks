import copy
import numpy as np

class Individuo:
    def __init__(self, alelos, longitud_gen, cromosoma):
        self._alelos = alelos
        self._longitud_gen = longitud_gen
        self._cromosoma = cromosoma
        self._fitness = 0

class AG:
    def __init__(self, cantidad_individuos, alelos, tamano_gen, generaciones, p, problema):
        self._cantidad_individuos = cantidad_individuos
        self._alelos = alelos
        self._tamano_gen = tamano_gen
        self._generaciones = generaciones
        self._p = p
        self._problema = problema
        self._individuos = np.array([])

    def run(self):
        self.crearIndividuos()
        self._mejor_historico = self._individuos[0]
        generacion = 0
        while generacion < self._generaciones:
            nuevoMejorHistorico = self.evaluaIndividuos()
            hijos = np.array([])
            while len(hijos) < len(self._individuos):
                padre1 = self.ruleta()
                padre2 = self.ruleta()
                attempts = 0
                while padre1 == padre2 and attempts < 10:
                    padre2 = self.ruleta()
                    attempts += 1
                h1, h2 = self.cruza(self._individuos[padre1], self._individuos[padre2])
                hijos = np.append(hijos, [h1])
                hijos = np.append(hijos, [h2])
            self.mutacion(hijos)
            self._individuos = np.copy(hijos)
            self._individuos[np.random.randint(len(self._individuos))] = copy.deepcopy(self._mejor_historico)
            if(nuevoMejorHistorico):
                print("Generación: ", generacion, 'Mejor Histórico: ', self._mejor_historico._cromosoma, self._mejor_historico._fitness, '\n')
                
            generacion += 1

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            cromosoma = np.random.randint(1, size = self._alelos)
            individuo = Individuo(self._alelos, self._tamano_gen, cromosoma)
            self._individuos = np.append(self._individuos, [individuo])

    def evaluaIndividuos(self):
        for i in self._individuos:
            i._fitness = self._problema.f(i._cromosoma)
            if i._fitness > self._mejor_historico._fitness:
                self._mejor_historico = copy.deepcopy(i)
                return True

    def ruleta(self):
        f_sum = np.sum([i._fitness for i in self._individuos])
        if f_sum == 0:
            return np.random.randint(len(self._individuos))
        else:
            r = np.random.randint(f_sum + 1)
            k = 0
            F = self._individuos[k]._fitness
            while F < r:
                k += 1
                F += self._individuos[k]._fitness
            return k

    def cruza(self, i1, i2):
        h1 = copy.deepcopy(i1)
        h2 = copy.deepcopy(i2)

        s = self._alelos - 1
        punto_cruza = np.random.randint(s) + 1
        for i in range(punto_cruza, self._alelos):
            h1._cromosoma[i], h2._cromosoma[i] = h2._cromosoma[i], h1._cromosoma[i]
        return h1, h2

    def mutacion(self, hijos):
        for hijo in hijos:
            for bit in range(len(hijo._cromosoma)):
                if np.random.rand() < self._p:
                    hijo._cromosoma[bit] = int(not hijo._cromosoma[bit])
