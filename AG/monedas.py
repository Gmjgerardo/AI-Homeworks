class Monedas:
    def __init__(self, lista):
        self._listaMonedas = lista

    def f(self, cromosoma):
        f = 0
        indice = 0
        
        while indice < len(cromosoma) - 1:
            if cromosoma[indice]:
                f = f + self._listaMonedas[indice]
                
                if(cromosoma[indice + 1]):
                    break
                
            indice += 1
                
        if indice == len(cromosoma) - 1:
            return f
        else:
            return 0