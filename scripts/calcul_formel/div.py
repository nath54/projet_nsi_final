

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
