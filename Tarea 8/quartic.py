class Quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    
    def __init__(self):
        pass
    
    def fitness(self, cromosoma):
        z = 0
        
        for i in range(len(cromosoma)):
            alelo = cromosoma[i]
            
            z += (i + 1) * (alelo**4)
        return z