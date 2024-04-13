from math import pi
from numpy import cos

class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    
    def __init__(self):
        pass
    
    def fitness(self, cromosoma):
        z = 10 * len(cromosoma)
        
        for alelo in cromosoma:
            z += alelo**2 - (10 * cos(2 * pi * alelo))
        return z