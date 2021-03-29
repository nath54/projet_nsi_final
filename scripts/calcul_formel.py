"""Module de calcul formel

Classes:
    Sum: Traite les éléments de type somme
    Mul: Traite les éléments de type multiplication
    Div: Traite les éléments de division
    Expr: Permet de gérer les interactions entre différentes expressions
"""
# region Somme
class Sum:
    """Classe d'un monstre de type somme.

    Attributes:
        components(list<Expr>):
            Liste des termes de la somme.

    """
    def __init__(self, *args):
        self.components = args

    def value(self):
        """Simplifie la valeur de la somme."""
        # Si tous les nombres sont des int ou float, on les simplifie.
        if all([type(c.value()) in [int, float] for c in self.components]):
            r = sum(terme.value() for terme in self.components)
            return Expr(r)
        else:
            # Permet de simplifier au maximum une somme
            a = self.components[0]
            for b in self.components[1:]:
                a = Sum(a, b)
            return Expr(a)

    def __str__(self):
        expressions = []
        for terme in self.components:
            if type(terme.value()) in [int, float, str]:
                expressions.append(str(terme))
            else:
                expressions.append("(" + str(terme) + ")")
        return " + ".join(expressions)


def test_somme():
    a = Expr(5)
    b = Expr("a")
    d = Expr(1)
    e = a + d
    c = a + b + d
    print(c)
    print(e)
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
                r *= c
            return Expr(r)
        else:
            a = self.components[0]
            for b in self.components[1:]:
                a = Mul(a, b)
            return Expr(a)

    def __str__(self):
        expressions = []
        for terme in self.components:
            if type(terme.value()) in [int, float, str]:
                expressions.append(str(terme))
            else:
                expressions.append(f"({str(terme)})")
        return " × ".join(expressions)
#endregion


#region division
class Div:
    def __init__(self, *args):
        self.components = args
        assert len(self.components) >= 2,\
            "Il n'y a pas assez de nombres à diviser !"

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = self.components[0]
            # TODO: Il faudra s'arreter de diviser comme ca si on a un nombre irrationnel
            for c in self.components[1:]:
                r/=c
            return Expr(r)
        else:
            a = self.components[0]
            for b in self.components[1:]:
                a = Div(a, b)
            return Expr(a)

    def __str__(self):
        a = self.components[0]
        if not type(a.value()) in [int, float, str]:
            aa = "(" + str(a) + ")"
        else:
            aa = str(a)
        for b in self.components[:1]:
            if not type(b.value()) in [int, float, str]:
                aa += " / (" + str(b) + ")"
            else:
                aa += " / " + str(b)
        return aa
#endregion


#region expression mathématique
class Expr:
    def __init__(self, *components):
        self.components = components

    def value(self):
        if len(self.components) == 0:
            return None
        elif len(self.components) == 1:
            return self.components[0]
        else:
            return self.components

    def __add__(self, other):
        if type(other) in [int, float]:
            other = Expr(other)
        return Sum(self, other).value()

    def __mul__(self, other):
        if type(other) in [int, float]:
            other = Expr(other)
        return Mul(self, other).value()

    def __truediv__(self, other):
        return self.__div__(other)

    def __div__(self, other):
        if type(other) in [int, float]:
            other = Expr(other)
        return Div(self, other).value()

    def __str__(self):
        return " ".join([str(c) for c in self.components])

    def __repr__(self):
        return self.__str__()

    def __print__(self):
        return self.__str__()

    def __eq__(self, other):
        return str(self) == str(other)

#endregion

#region tests :


if __name__ == "__main__":
    print("Début des tests : Somme")
    test_somme()
    print("Fin des tests : Somme")

#endregion