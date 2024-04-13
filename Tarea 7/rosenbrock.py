class Rosenbrock:
    MIN_VALUE = -2.048
    MAX_VALUE = 2.048
    
    def __init__(self):
        pass
    
    def fitness(self, cromosoma):
        z = 0
        for i in range(len(cromosoma) - 1):
            x = cromosoma[i]
            y = cromosoma[i + 1]

            z += 100 * ((y - x**2)**2) + (x - 1)**2
        return z
