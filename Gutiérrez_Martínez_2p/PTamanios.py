class PTamanios:
    def __init__(self, lista, limite):
        self._tamaniosObjetos = lista
        self._limite = limite

    def fitness(self, cromosoma):
        f = 0

        for i in range(len(self._tamaniosObjetos)):
            if cromosoma[i]:
                f += self._tamaniosObjetos[i]

            if f > self._limite:
                f = 0
                break
        return f