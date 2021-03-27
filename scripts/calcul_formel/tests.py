from calcul_formel import *

def tests():
    a = Exp(5)
    b = Exp("a")
    d = Exp(1)
    c = (a / b) * (b / a)
    print(c)


if __name__ == "__main__":
    tests()
