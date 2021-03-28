

#region somme
class Sum:
    def __init__(self, *args):
        self.components = args

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = sum(self.components)
            return Exp(r)
        else:
            a = self.components[0]
            for b in self.components[1:]:
                a = Sum(a, b)
            return Exp(a)

    def __str__(self):
        a = self.components[0]
        if not type(a.value()) in [int, float, str]:
            aa = "(" + str(a) + ")"
        for b in self.components[:1]:
            if not type(b.value()) in [int, float, str]:
                aa += " + (" + str(b) + ")"
            else:
                aa += " + " + str(b)
        return aa

#endregion


#region multiplication

class Mul:
    def __init__(self, *args):
        self.components = args

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = self.components[0]
            # TODO: Il faudra s'arreter de diviser comme ca si on a un nombre irrationnel
            for c in self.components[1:]:
                r*=c
            return Exp(r)
        else:
            a = self.components[0]
            for b in self.components[1:]:
                a = Mul(a, b)
            return Exp(a)

    def __str__(self):
        a = self.components[0]
        if not type(a.value()) in [int, float, str]:
            aa = "(" + str(a) + ")"
        for b in self.components[:1]:
            if not type(b.value()) in [int, float, str]:
                aa += " * (" + str(b) + ")"
            else:
                aa += " * " + str(b)
        return aa

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
            a = self.components[0]
            for b in self.components[1:]:
                a = Div(a, b)
            return Exp(a)

    def __str__(self):
        a = self.components[0]
        if not type(a.value()) in [int, float, str]:
            aa = "(" + str(a) + ")"
        for b in self.components[:1]:
            if not type(b.value()) in [int, float, str]:
                aa += " / (" + str(b) + ")"
            else:
                aa += " / " + str(b)
        return aa

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

#region tests :

def tests():
    a = Exp(5)
    b = Exp("a")
    d = Exp(1)
    c = a + b +d
    print(c)

if __name__ == "__main__":
    tests()

#endregion