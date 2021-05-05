from math import gcd

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


class Operation:
    def value(self):
        pass


# region Somme
class Sum(Operation):
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
            total_constantes = sum([terme.value() for terme in self.components
                                    if type(terme.value()) in [int, float]])
            reste = [terme.value() for terme in self.components
                     if type(terme.value()) not in [int, float]]
            variables = {}
            vars_facto = []
            # S'il y a une division
            elt = [elt for elt in reste if isinstance(elt, Div)]
            if len(elt) != 0:
                for terme in reste:
                    if isinstance
            for terme in reste:
                # Dans le cas où le terme est un str, donc une variable
                if isinstance(terme, str):
                    if terme in variables:
                        variables[terme] += 1
                    else:
                        variables[terme] = 1
                # Dans le cas où le terme est une Multiplication
                if isinstance(terme, Mul):
                    coeff = [const.value() for const in terme.components
                             if type(const.value()) in [int, float]]
                    if len(coeff) == 0:
                        coeff = 1
                    else:
                        coeff = coeff[0]
                    var = [variable.value() for variable in terme.components
                           if isinstance(variable.value(), str)][0]
                    if var in variables:
                        variables[var] += coeff
                    else:
                        variables[var] = coeff
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
# endregion


# region multiplication
class Mul(Operation):
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
            if type(terme.value()) in [int, str, Div]:
                expressions.append(str(terme))
            else:
                expressions.append(f"({str(terme)})")
        return " × ".join(expressions)

    def __print__(self):
        return str(self)
# endregion


# region division
class Div(Operation):
    def __init__(self, numerateur, denominateur):
        assert numerateur is not None, "Le numérateur ne devrait pas être None"
        assert denominateur is not None,\
            "Le dénominateur ne devrait pas être None"
        assert denominateur != 0, "Diviser par zéro : 2U"

        self.num = Expr(numerateur)
        self.denom = Expr(denominateur)

    def value(self):
        num = self.num
        denom = self.denom
        # D'abord, on regarde si le numérateur et le dénominateur sont entiers
        if isinstance(num, int) and isinstance(denom, int):
            return self.__simplifie_ints(num, denom)

        # Si le numérateur et le dénominateur sont des `Opération`
        elif not isinstance(num, str) and\
                not isinstance(denom, str):
            # S'ils sont simplifiables en tant qu'`int`
            try:
                if isinstance(num, Operation):
                    num_int = int(num.value())
                else:
                    num_int = int(num)

                if isinstance(denom, Operation):
                    denom_int = int(denom.value())
                else:
                    denom_int = int(denom)
                return self.__simplifie_ints(num_int, denom_int)
            # S'ils ne sont pas simplifiables en `int`
            except (ValueError, TypeError):
                # TODO: S'ils ne sont pas simplifiables en `int`
                return self.__simplifie_vars(num, denom)
        else:
            return self.__simplifie_vars(num, denom)

    def __simplifie_vars(self, num, denom):
        num = num.value()
        if isinstance(num, str):
            return Expr(Mul(Div(1, denom), num))
        if isinstance(num, Sum):
            # TODO: Insert factorisation
            return Expr(Div(num, denom))
        if isinstance(num, Mul):
            variables = ""
            for i in range(len(num.components)):
                if isinstance(num.components[i].value(), str):
                    variables += num.components[i].value()
                    del num.components[i]
            return Expr(Mul(Div(num.value(), denom).value(), variables))

    def __simplifie_ints(self, num, denom):
        """Simplifie une fraction avec un int au numérateur et dénominateur.

        Args:
            num(int):
                Numérateur de la fraction
            denom(int):
                Dénominateur de la fraction

        Errors:
            AssertError:
                Si les paramètres passés ne sont pas des ints
        """
        assert isinstance(num, int),\
            f"Le numérateur de la fraction n'est pas un entier : {num}"
        assert isinstance(denom, int),\
            f"Le dénominateur de la fraction n'est pas un entier : {denom}"

        if num % denom == 0:
            return Expr(num // denom)
        else:
            commun_diviseur = gcd(num, denom)
            num = num // commun_diviseur
            denom = denom // commun_diviseur
            return Expr(Div(num, denom))

    def __str__(self):
        return f"({str(self.num.value())} / {str(self.denom.value())})"

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
            except (TypeError, ValueError):
                value = self.components[0]
            return value

    def __int__(self):
        return int(self.components[0])

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


def substituer_expr(expression, variable, remplacement):
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
    return Sum(*liste_terme).value()

# region Tests
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


def test_str_to_expr():
    print("Début du test : Fonction substituer_expr")

    assert substituer_expr("5+2*x", "x", 4) == 13
    assert substituer_expr("11037+53*x", "x", 12) == 11673

    print("Fin du test : substituer_expr")


def test_div():
    print("Début du test : Classe Div")

    # Fraction irréductible
    d = Div(4, 3).value()
    assert d == "(4 / 3)", f"{d}"

    # Simplification de fraction
    d = Div(8, 4).value()
    assert d == 2, f"{d}"

    # Extraction de variable
    d = Div("a", 4).value()
    assert d == "(1 / 4) × a", f"{d}"

    # Extraction de variable ET simplification
    d = Div(Mul(2, "a"), 4).value()
    assert d == "(1 / 2) × a", f"{d}"

    # Extraction de variable ET simplification (transformation en Mul)
    d = Div(Mul(4, "a"), 2).value()
    assert d == "2 × a", f"{d}"

    print("Fin du test : Classe Div")
# endregion


if __name__ == "__main__":
    test_div()
    test_str_to_expr()
    test_somme()
