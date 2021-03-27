
from div import Div
from sum_ import Sum
from exp import Exp

class Mul:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def value(self):
        if type(self.a.value()) in [int, float] and type(self.b.value()) in [int, float]:
            return Exp(self.a.value()*self.b.value())
        else:
            return Exp(Mul(self.a, self.b))

    def __str__(self):
        aa = self.a.__str__()
        bb = self.b.__str__()
        if not type(self.a.value()) in [int, float, str]:
            aa = "(" + aa + ")"

        if not type(self.b.value()) in [int, float, str]:
            bb = "(" + bb + ")"
        return aa + " * " + bb

