from monedas import Monedas
from sabio import AG

def main():
    pesos = [1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20, 20, 20, 5, 1,
             1, 20, 20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1, 20, 10, 5, 5, 20, 2, 10,
             1, 2, 5, 10, 20, 10, 2, 5, 5, 20, 1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2,
             10, 20, 2, 10, 10, 20, 5, 10, 1, 2, 1, 5, 20, 2, 5, 1, 5, 10, 2, 5, 10,
             2, 1, 1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2]
    
    filaMonedas = Monedas(pesos)
    ag = AG((len(pesos) + 1), len(pesos), 1, 1200, 0.01, filaMonedas)
    ag.run()

if __name__ == '__main__':
    main()

