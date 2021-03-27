from mul import Mul
from div import Div
from exp import Exp

class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def value(self):
        if type(self.a.value()) in [int, float] and type(self.b.value()) in [int, float]:
            return Exp(self.a.value()+self.b.value())
        else:
            return Exp(Sum(self.a, self.b))

    def __str__(self):
        return self.a.__str__() + " + " + self.b.__str__()
