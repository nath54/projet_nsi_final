
class Exp:
    def __init__(self, *components):
        self.components = components
    
    def value(self):
        if len(self.components)==0:
            return None
        elif len(self.components)==1:
            return self.components[0]
        else:
            return self.components

    def __add__(self, other):
        if type(other) in [int, float]:
            other = Exp(other)
        return Sum(self, other).value()

    def __mul__(self, other):
        if type(other) in [int, float]:
            other = Exp(other)
        return Mul(self, other).value()

    def __truediv__(self, other):
        return self.__div__(other)

    def __div__(self, other):
        if type(other) in [int, float]:
            other = Exp(other)
        return Div(self, other).value()

    def __str__(self):
        return " ".join([str(c) for c in self.components])

    def __repr__(self):
        return self.__str__()
    
    def __print__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return str(self)==str(other)
