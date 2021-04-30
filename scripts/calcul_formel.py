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
            if isinstance(arg, list):
                for elt in arg:
                    self.components.append(Expr(elt))
            if type(arg) in [str, int, float]:
                self.components.append(Expr(arg))
                i += 1

    def value(self):
        # Si tous les nombres sont des int ou float, on les simplifie.
        if all([type(c.value()) in [int, float] for c in self.components]):
            r = sum(terme.value() for terme in self.components)
            return Expr(r)
        # Sinon, on simplifie au maximum
        else:
            total_constantes = sum([terme.value() for terme in self.components\
                                    if type(terme.value()) in [int, float]])
            reste = [terme.value() for terme in self.components\
                     if type(terme.value()) not in [int, float]]
            variables = {}
            vars_facto = []
            for terme in reste:
                # Dans le cas où le terme est un str, donc une variable
                if isinstance(terme, str):
                    if terme in variables:
                        variables[terme] += 1
                    else:
                        variables[terme] = 1
                # Dans le cas où le terme est une Multiplication
                if isinstance(terme, Mul):
                    coeff = [const.value() for const in terme.components\
                             if type(const.value()) in [int, float]][0]
                    var = [variable.value() for variable in terme.components\
                           if isinstance(variable.value(), str)][0]
                    if var in variables:
                        variables[var] += coeff
                    else:
                        variables[var] = coeff
                # Dans le cas où le terme est une Division
                if isinstance(terme, Div):
                    # But : séparer les variables des constantes
                    pass  # TODO
            for var in variables:
                if variables[var] == 0:
                    continue
                elif variables[var] == 1:
                    vars_facto.append(var)
                else:
                    vars_facto.append(Mul(Expr(variables[var]), Expr(var)).value())
            if total_constantes == 0:
                return Expr(Sum(*vars_facto))
            e = Expr(Sum(total_constantes, *vars_facto))
            return e

    def __add__(self, other):
        new_comp = self.components
        return Sum(*new_comp, other)

    def __str__(self):
        expressions = []
        for terme in self.components:
            if type(terme.value()) in [int, float, str, Mul]:
                expressions.append(str(terme))
            else:
                expressions.append("(" + str(terme) + ")")
        return " + ".join(expressions)

    def __print__(self):
        return str(self)


def test_somme():
    print("DEBUT DU TEST : Sum")

    # TEST SIMPLIFICATION DE CONSTANTES
    var = str(Sum(18, 24, 22).value())
    assert var == "64", f"Mauvaise valeur : {var} au lieu de '64'"

    # TEST SIMPLIFICATION DE CONSTANTES AVEC VARIABLE (1 VAR)
    var = str(Sum(18, 24, 22, "a").value())
    assert var == "64 + a", f"Mauvaise valeur : {var} au lieu de '64 + a'"

    # TEST SIMPLIFICATION DE CONSTANTES AVEC VARIABLES (PLUSIEURS VARS)
    var = str(Sum(1, 5, Sum("a", "b")).value())
    assert var == "6 + a + b",\
        f"Mauvaise valeur : {var} au lieu de '6 + a + b'"

    # FACTORISATION D'UNE SOMME AVEC PLUSIEURS ITÉRATIONS DE VARIABLES (1 VAR)
    var = str(Sum(1, 5, "a", "a").value())
    assert var == "6 + 2 × a",\
        f"Mauvaise valeur : {var} au lieu de '6 + 2 × a'"

    # FACTORISATION D'UNE SOMME AVEC PLUSIEURS ITÉRATIONS DE VARIABLES (PLUSIEURS VARS)
    var = str(Sum(1, 5, "a", "a", "a", "b", "b", "b").value())
    assert var == "6 + 3 × a + 3 × b",\
        f"Mauvaise valeur : {var} au lieu de '6 + 3 × a + 3 × b'"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE MULTIPLICATION (1 VAR)
    var = str(Sum("a", Mul(3, "a").value()).value())
    assert var == "4 × a", f"{var}"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE MULTIPLICATION (PLUSIEURS VARS)
    var = str(Sum("a", Mul(3, "a").value(), "b", "b", Mul(40, "b").value()).value())
    assert var == "4 × a + 42 × b", f"{var}"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE DIVISION (1 VAR)
    var = str(Sum(Div("a", 4).value(), "a").value())
    assert var == "(5 / 4) × a", f"{var}"

    print("FIN DU TEST : Sum")
# endregion


# region multiplication
class Mul:
    def __init__(self, *args):
        self.components = []
        for arg in args:
            if not isinstance(arg, Expr):
                self.components.append(Expr(arg))
            else:
                self.components.append(arg)

    def value(self):
        if all([type(c.value()) in [int, float] for c in self.components]):
            r = self.components[0].value()
            # TODO: Il faudra s'arrêter de diviser comme ça si on a un nombre
            #       irrationnel ?????
            for c in self.components[1:]:
                r *= c.value()
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
    def __init__(self, numerateur, denominateur):
        self.num = Expr(numerateur)
        self.denom = Expr(denominateur)
        assert self.denom != 0,\
            "Diviser par 0 : 2U"

    def value(self):
        if isinstance(self.num, int) and isinstance(self.denom, int):
            if self.num % self.denom == 0:
                return Expr(self.num // self.denom)
            else:
                # TODO: Insérer simplification ici
                return Expr(Div(self.num, self.denom))
        else:
            return Expr(self)

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
        """Renvoie la valeur de l'expression"""
        if len(self.components) == 0:
            return None
        else:
            value = None
            try:
                value = int(self.components[0])
            except:
                value = self.components[0]
            return value

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

    def __mod__(self, other):
        if type(other) in [int, float]:
            other = Expr(other)
        return self.value() % other.value()

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

def substituer_expr(expression,variable,remplacement):
    """Prend une expression pour substituer sa variable et l'interpréter

    Args:
        expression (str):
            Expression à interpréter (exemple : "5+2*x")
        variable (str):
            Nom de la variable (exemple : "x")
        remplacement (int):
            Entier par lequel remplacer la variable (exemple : 4)

    Return:
        Expr: Résultat de l'expression
    """
    assert isinstance(expression, str)
    assert isinstance(variable, str)
    assert isinstance(remplacement, int)
    if expression == "":
        return None

    expression = expression.replace(variable, str(remplacement))
    liste_terme = expression.split("+")
    for terme_indice in range(len(liste_terme)):
        mult = liste_terme[terme_indice].split("*")
        if len(mult) == 2:
            liste_terme[terme_indice] = Mul(*mult).value()
            print(liste_terme[terme_indice])
    return Sum(*liste_terme).value()

def test_str_to_expr():
    assert substituer_expr("5+2*x", "x", 4) == 13
    assert substituer_expr("11037+53*x", "x", 12) == 11673

if __name__ == "__main__":
    test_str_to_expr()
    # test_somme()
