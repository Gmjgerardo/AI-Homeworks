import sphere
import AGC

def main():
    s = sphere.Sphere()
    ag = AGC.AGC(64, 2 , 2000, 0.02, s, False)
    ag.run()

if __name__ == '__main__':
    main()
