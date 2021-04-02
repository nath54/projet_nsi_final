"""Module de calcul formel

Classes:
    Sum: Traite les éléments de type somme
    Mul: Traite les éléments de type multiplication
    Div: Traite les éléments de division
    Expr: Permet de gérer les interactions entre différentes expressions
"""


def trie(components):
    groups = {
        "nbs": [],  # Quand il n'y a pas de variables
        # les variables se rajouteront ici
        # TODO: Compléter les variables ?
        # la on met le reste pour l'instant
        "reste": []
    }
    for expression in components:
        if type(expression.value()) in [int, float]:
            groups["nbs"].append(expression)
            continue
        if type(expression) == Mul:
            # TODO: Regarder s'il y a une variable dans les composants
            #       de l'expression
            for e in expression.components:
                val = e.value()
                if type(val) == str:
                    if val not in groups.keys():
                        groups[val] = []
                    groups[val].append(expression)
                    continue
        # Si on est toujours là, c'est qu'on ne l'a pas ajouté
        groups["reste"].append(expression)
    return groups


# region Somme
class Sum:
    """Classe d'un monstre de type somme.

    Attributes:
        components(list<Expr>):
            Liste des termes de la somme.

    """
    def __init__(self, *args):
        """Créé une somme

        Arguments:
            *args(tuple(int|str|Sum|Expr))
                Liste des termes de la somme
        """
        self.components = []
        i = 0
        for arg in args:
            if type(arg) == Expr and len(arg.components) == 1:
                self.components.append(Expr(arg.components[0]))
            if type(arg) == Sum:
                termes = arg.components
                self.components += termes
                self = Sum(self.components)
            if type(arg) in [str, int, float]:
                self.components.append(Expr(arg))
                i += 1

    def value(self):
        """Simplifie la valeur de la somme.

        Returns:
            Expr
                Résultat de la somme sous forme d'Expr
        """
        # Si tous les nombres sont des int ou float, on les simplifie.
        if all([type(c.value()) in [int, float] for c in self.components]):
            r = sum(terme.value() for terme in self.components)
            return Expr(r)
        else:
            # Permet de simplifier au maximum une somme
            expression_nombres = None
            expressions_variables = []
            expression_reste = None
            # on récupère les groupes triés
            groupes_tries = trie(self.components)
            # on fait déjà la somme des nombres faciles
            somme_nbs = sum([e.value() for e in groupes_tries["nbs"]])
            if somme_nbs != 0:
                expression_nombres = Expr(somme_nbs)
            # variables
            variables = {}
            for tp_groupe in groupes_tries.keys():
                if tp_groupe != "nbs" and tp_groupe != "reste":
                    variables[tp_groupe] = groupes_tries[tp_groupe]
            """TODO: Faire la factorisation, et rajouter les expressions
                     dans la liste expressions_variables
            for variable, liste in variables.items():
                lst_coefficients = []
                for expression in liste:
                    autres_coef = []
                    for coef in expression.components:
                        if coef.value() != variable:
                            autres_coef.append(coef)
                    lst_coefficients += autres_coef
                print(lst_coefficients)
                expressions_variables.append(Mul(Expr(variable),\
                    Sum(*lst_coefficients)))
            """
            # restes
            reste = groupes_tries["reste"]
            if len(reste) == 1:
                expression_reste = reste[0]
            elif len(reste) >= 2:
                expression_reste = Sum(reste[0], reste[1])
                for x in range(2, len(reste)):
                    expression_reste = Sum(expression_reste, reste[x])
            # on fait la somme de ce qui nous reste
            liste = []
            if expression_nombres is not None:
                liste.append(expression_nombres)
            liste += expressions_variables
            if expression_reste is not None:
                liste.append(expression_reste)
            if len(liste) == 0:
                return Expr(0)
            elif len(liste) == 1:
                return Expr(liste[0])
            else:
                a = Sum(liste[0], liste[1])
                for x in range(2, len(liste)):
                    a = Sum(a, liste[x])
                return Expr(a)

    def __str__(self):
        expressions = []
        for terme in self.components:
            if type(terme.value()) in [int, float, str]:
                expressions.append(str(terme))
            else:
                expressions.append("(" + str(terme) + ")")
        return " + ".join(expressions)

    def __print__(self):
        return str(self)


def test_somme():
    print("DEBUT DU TEST : Sum")
    var = str(Sum(18, 24, 22, "a").value())
    assert var == "64 + a", f"Mauvaise valeur : {var} au lieu de '64 + a'"
    var = str(Sum(1, 5, Sum("a", "b")).value())
    assert var == "6 + a + b",\
        f"Mauvaise valeur : {var} au lieu de '6 + a + b'"
    print(Sum(1, 5, "a", "a"))
    print("FIN DU TEST : Sum")
# endregion


# region multiplication
class Mul:
    def __init__(self, *args):
        self.components = list(args)

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = self.components[0]
            # TODO: Il faudra s'arrêter de diviser comme ça si on a un nombre
            #       irrationnel ?????
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

    def __print__(self):
        return str(self)
# endregion


# region division
class Div:
    def __init__(self, *args):
        self.components = args
        assert len(self.components) >= 2,\
            "Il n'y a pas assez de nombres à diviser !"

    def value(self):
        if all([type(c) in [int, float] for c in self.components]):
            r = self.components[0]
            # TODO: Il faudra s'arrêter de diviser comme ça si on a un nombre
            #       irrationnel
            for c in self.components[1:]:
                r /= c
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

    def __print__(self):
        return str(self)
# endregion


# region expression mathématique
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
        """Teste l'égalité entre deux expressions

        TODO: Faudra avoir une syntaxe bien définie pour éviter qu'on ait des :
              '2 × a' == 'a × 2' -> False
        """
        return str(self) == str(other)
# endregion


if __name__ == "__main__":
    test_somme()
