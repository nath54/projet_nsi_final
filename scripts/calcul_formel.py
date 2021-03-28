

#region somme
class Sum:
    def __init__(self, *args):
        self.components = args

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = sum(self.components)
            return Exp(r)
        else:
            return Exp(*[Sum(c) for c in self.components])

    def __str__(self):
        return self.a.__str__() + " + " + self.b.__str__()

#endregion


#region multiplication

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

#endregion


#region division

class Div:
    def __init__(self, *args):
        self.components = args
        assert len(self.components)>=2, "Il n'y a pas assez de nombres à diviser !"

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = self.components[0]
            # TODO: Il faudra s'arreter de diviser comme ca si on a un nombre irrationnel
            for c in self.components[1:]:
                r/=c
            return Exp(r)
        else:
            return Exp(Div(self.a, self.b))

    def __str__(self):
        aa = self.a.__str__()
        bb = self.b.__str__()
        if not type(self.a.value()) in [int, float, str]:
            aa = "(" + aa + ")"

        if not type(self.b.value()) in [int, float, str]:
            bb = "(" + bb + ")"
        return aa + " / " + bb

#endregion



#region expression mathématique

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

#endregion
