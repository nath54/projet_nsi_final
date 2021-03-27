
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


class Mul:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def value(self):
        if type(self.a.value()) in [int, float] and type(self.b.value()) in [int, float]:
            return Exp(self.a.value()*self.b.value())
        else:
            for c in self.a.components:
                print(c)   
                if type(c) == Div:
                    if c.b == self.b:
                        return Exp(c.b)
            return Exp(Mul(self.a, self.b))

    def __str__(self):
        aa = self.a.__str__()
        bb = self.b.__str__()
        if not type(self.a.value()) in [int, float, str]:
            aa = "(" + aa + ")"

        if not type(self.b.value()) in [int, float, str]:
            bb = "(" + bb + ")"
        return aa + " * " + bb


class Div:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def value(self):
        if type(self.a.value()) in [int, float] and type(self.b.value()) in [int, float]:
            return Exp(self.a.value()/self.b.value())
        else:
            for c in self.a.components:
                print(c)   
                if type(c) == Mul:
                    if c.a == self.b:
                        return Exp(c.b)
                    if c.b == self.b:
                        return Exp(c.a)
            # for c in self.b.components:
            #     print(c)   
            #     if type(c) == Mul:
            #         if c.a == self.a:
            #             return Exp(c.b)
            #         if c.b == self.a:
            #             return Exp(c.a)
            return Exp(Div(self.a, self.b))

    def __str__(self):
        aa = self.a.__str__()
        bb = self.b.__str__()
        if not type(self.a.value()) in [int, float, str]:
            aa = "(" + aa + ")"

        if not type(self.b.value()) in [int, float, str]:
            bb = "(" + bb + ")"
        return aa + " / " + bb


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

def tests():
    a = Exp(5)
    b = Exp("a")
    d = Exp(1)
    c = (a / b) * (b / a)
    print(c)


if __name__ == "__main__":
    tests()
