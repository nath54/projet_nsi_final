"""Calcul formel

Classes:
---
    Sum: Traite les éléments de type somme
    Mul: Traite les éléments de type multiplication
    Div: Traite les éléments de division
    Expr: Permet de gérer les interactions entre différentes expressions
"""

from math import gcd
from traceback import print_stack


def lcm(*liste):
    """Retourne le plus grand commun diviseur"""
    lcm = 1
    for i in liste:
        lcm *= i//gcd(lcm, i)
    return lcm


class Operation:
    def value(self):
        """Retourne la valeur simplifiée d'une opération"""
        pass

    def is_const(self):
        """Retourne False si l'Opération contient une variable"""
        for terme in self.components:
            if isinstance(terme, Expr):
                if not is_int(terme):
                    return False
            elif isinstance(terme, Operation):
                if not terme.is_const():
                    return False
        return True


# region Somme
class Sum(Operation):
    """Classe d'un monstre de type somme.

    Attributes:
    ---
        components(list<Expr>):
            Liste des termes de la somme.

    """
    def __init__(self, *args):
        """Créé une somme

        Arguments:
        ---
            args(tuple(int|str|Operation|Expr))

                Liste des termes de la somme
        """
        self.components = []
        for arg in args:
            if type(arg) == Expr and len(arg.components) == 1:
                self.components.append(Expr(arg.components[0]))
            elif type(arg) == Sum:
                termes = arg.components
                self.components += termes
                self = Sum(self.components)
            elif isinstance(arg, list):
                for elt in arg:
                    self.components.append(Expr(elt))
            elif type(arg) in [str, int]:
                self.components.append(Expr(arg))
            elif isinstance(arg, Div):
                self.components.append(arg.value())
            else:
                self.components.append(Expr(arg))

    def value(self):
        # Si tous les nombres sont des int ou float, on les additionne.
        if all([isinstance(c.value(), int) for c in self.components]):
            r = sum(terme.value() for terme in self.components)
            return Expr(r)
        # Si c'est tous des Div, on met tout sur le même dénominateur
        elif all([isinstance(c.value(), Div) and c.value().is_const()
                  for c in self.components]):
            all_denom = [comps.value().denom.value()
                         for comps in self.components]
            denom_final = lcm(*all_denom)
            num_final = sum([comps.value().num.value() * denom_final //
                             comps.value().denom.value()
                             for comps in self.components])
            return Expr(Div(num_final, denom_final))
        # Sinon, on simplifie au maximum
        else:
            return self.__simplifie_addition()

    def __simplifie_addition(self):
        total_constantes = sum([terme.value() for terme in self.components
                                if isinstance(terme.value(), int)])
        reste = [terme.value() for terme in self.components
                 if not isinstance(terme.value(), int)]
        variables = {}
        vars_facto = []
        for terme in reste:
            # Dans le cas où le terme est un str, donc une variable
            if isinstance(terme, str):
                if terme in variables:
                    if isinstance(variables[terme], Div):
                        variables[terme].num += variables[terme].denom
                    else:
                        variables[terme] += 1
                else:
                    variables[terme] = 1
            # Dans le cas où le terme est une Multiplication
            if isinstance(terme, Mul):
                variables = self.__traite_Mul(terme, variables)
            if isinstance(terme, Div):
                variables = self.__traite_Div(terme, variables)
        for var in variables:
            if variables[var] == 0:
                continue
            elif variables[var] == 1:
                vars_facto.append(var)
            else:
                vars_facto.append(Mul(Expr(variables[var]), Expr(var)).value())
        new_vars = []
        for var in vars_facto:
            if type(vars_facto[0]) == Expr:
                new_vars.append(var.value())
            else:
                new_vars.append(var)
        if total_constantes == 0:
            return Expr(Sum(*new_vars))
        e = Expr(Sum(*new_vars, total_constantes))
        return e

    def __traite_Mul(self, terme, variables):
        """Traite le cas où un terme est une Mul.

        Arguments:
        ---
        terme(Mul)
            La multiplication à traiter.

        variables(dict<str: int|Div>)
            Dict contenant les coefficients associés à chaques variables.

        Return:
        ---
            dict<str: int|Div>
                Le dictionnaire des coefficients complété par le terme.
        """
        lcoeff = [const.value() for const in terme.components
                  if isinstance(const.value(), int)]
        coeff = 0
        if len(lcoeff) != 0:
            coeff = lcoeff[0]
        divs = [c for c in terme.components if isinstance(c.value(), Div)]
        if len(divs) != 0:
            n_coeff = 0
            if len(divs) == 1:
                n_coeff = divs[0].value()
            else:
                n_coeff = Sum(*divs).value()
            n_coeff.num += (coeff * n_coeff.denom.value())
            coeff = n_coeff
        var = [variable.value() for variable in terme.components
               if isinstance(variable.value(), str)][0]
        if var in variables:
            variables[var] += coeff
            if isinstance(variables[var], Expr):
                variables[var] = variables[var].value()
        else:
            variables[var] = coeff
        return variables

    def __traite_Div(self, terme, variables):
        pass  # TODO:

    def __add__(self, other):
        """Ajoute de nouveaux termes à une Sum"""
        new_comp = self.components
        return Sum(*new_comp, other)

    def __str__(self):
        expressions = []
        for terme in self.components:
            if type(terme.value()) in [int, str, Mul]:
                expressions.append(str(terme))
            else:
                expressions.append("(" + str(terme) + ")")
        return " + ".join(expressions)

    def __print__(self):
        return str(self)
# endregion


# region multiplication
class Mul(Operation):
    """Permet de traiter les multiplications

    Attributes
    ---
    components(list<Expr>)
        Composants du produit

    """
    def __init__(self, *args):
        """Instancie la Mul

        Arguments
        ---
        args(list<int|Expr|Operation>)
            Liste des termes de la multiplication
        """
        self.components = []
        for arg in args:
            if not isinstance(arg, Expr):
                self.components.append(Expr(arg))
            else:
                self.components.append(arg)

    def value(self):
        # Si tous les termes sont des int, on les multiplie entre eux
        if all([is_int(c) for c in self.components]):
            r = self.components[0].value()
            for c in self.components[1:]:
                r *= c.value()
            return Expr(r)
        # TODO: Batterie de test pour ça
        else:
            a = self.components[0]
            for b in self.components[1:]:
                a = Mul(a, b)
            return Expr(a)

    def __str__(self):
        const = [k for k in self.components if isinstance(k, int)]
        reste = [k for k in self.components if not isinstance(k, int)]
        expressions = []
        for terme in reste:
            if type(terme.value()) in [int, str, Div]:
                expressions.append(str(terme))
            else:
                expressions.append(f"({str(terme)})")
        return " × ".join(const + expressions)

    def __print__(self):
        return str(self)
# endregion


# region division
class Div(Operation):
    """Traite les divisions.

        Attributes:
        ---

        numerateur(Expr):
            Expression du numérateur sous forme d'Expr
        denominateur(Expr):
            Expression du dénominateur sous forme d'Expr
    """
    def __init__(self, numerateur, denominateur):
        """Instancie une Div

        Arguments:
        ---
        numerateur(str|int|Expr|Operation):
            Partie du numérateur, sera convertie en Expr
        denominateur(str|int|Expr|Operation):
            Partie du dénominateur, sera convertie en Expr

        Raise:
        ---
        AssertError:
            * Si `numerateur` est `None`
            * Si `denominateur` est `None`
            * Si `denominateur` vaut `0`
        """
        assert numerateur is not None, "Le numérateur ne devrait pas être None"
        assert denominateur is not None,\
            "Le dénominateur ne devrait pas être None"
        assert denominateur != 0, "Diviser par zéro : 2U"
        if not (isinstance(denominateur, int) or
                isinstance(denominateur, str)):
            assert denominateur.value() != 0

        self.num = Expr(numerateur)
        self.denom = Expr(denominateur)

    def is_const(self):
        num = self.num.value()
        denom = self.denom.value()
        return isinstance(num, int) and isinstance(denom, int)

    def simplifie(self):
        num = self.num
        denom = self.denom
        # D'abord, on regarde si le numérateur et le dénominateur sont entiers
        if isinstance(num.value(), int) and isinstance(denom.value(), int):
            return self.__simplifie_ints(num, denom)

        # Si le numérateur et le dénominateur sont des `Opération`
        elif isinstance(num, Operation) and isinstance(denom, Operation):
            # S'ils sont simplifiables en tant qu'`int`
            if is_int(num.value()) and is_int(denom.value()):
                nval = num.value()
                dval = denom.value()
                return self.__simplifie_ints(int(nval), int(dval))
            # S'ils ne sont pas simplifiables en `int`
            return self.__simplifie_vars(num, denom)
        else:
            return self.__simplifie_vars(num, denom)

    def value(self):
        return Expr(self.simplifie())

    def __simplifie_vars(self, num, denom):
        """Simplifie la fraction s'il y a une ou plusieurs variables

        Arguments:
        ---
        num(`str`|`Operation`):
            Partie du numérateur pré-simplifiée (avec `value()`)
        denom(`str`|`Operation`):
            Partie du dénominateur pré-simplifiée (avec `value()`)

        Return:
        ---
        (Mul|Div): Opération simplifiée

        Raise:
        ---
        UserWarning:
            * Si num n'est ni un `str`, ni un `Sum`, ni un `Mul`, ni un `int`
        """
        num = num.value()
        if isinstance(num, int):
            return Div(num, denom)
        # Si c'est une simple variable, on renvoie 1/denom * num
        if isinstance(num, str):
            return Mul(Div(1, denom), num)
        # Si c'est une Sum, on pourrait factoriser
        if isinstance(num, Sum):
            # TODO: Insert factorisation
            return Div(num, denom)
        # Si c'est une Mul, on extrait les variables et on simplifie
        if isinstance(num, Mul):
            variables = ""
            for i in range(len(num.components)):
                if isinstance(num.components[i].value(), str):
                    variables += num.components[i].value()
                    del num.components[i]
            return Mul(Div(num.value(), denom).value(), variables)
        raise(UserWarning(f"num est d'une classe non supportée : {type(num)}"))

    def __simplifie_ints(self, num, denom):
        """Simplifie une fraction avec un `int` au numérateur et dénominateur.

        Arguments:
        ---
            num(int):
                Numérateur de la fraction
            denom(int):
                Dénominateur de la fraction

        Raise:
        ---
            AssertError:
                * Si les paramètres passés ne sont pas des `int`
        """
        num = num.value()
        denom = denom.value()
        assert isinstance(num, int),\
            f"""Le numérateur de la fraction n'est pas un entier :
                type: {type(num)} ; value: {num}"""
        assert isinstance(denom, int),\
            f"""Le dénominateur de la fraction n'est pas un entier :
                type: {type(denom)} ; value: {denom}"""

        if num % denom == 0:
            return num // denom
        else:
            commun_diviseur = gcd(num, denom)
            num = num // commun_diviseur
            denom = denom // commun_diviseur
            return Div(num, denom)

    def __str__(self):
        return f"({str(self.num.value())} / {str(self.denom.value())})"

    def __print__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, Div):
            return Sum(self, other).value()
        return
# endregion


# region expression mathématique
class Expr:
    """Expression mathématique, unité de base des Opérations

    Attributes:
    ---
        components(list<int|str|Operation|Expr>)
    """
    def __init__(self, *components):
        self.components = components

    def value(self):
        """Renvoie la valeur de l'expression"""
        if len(self.components) == 0:
            return None
        else:
            if is_int(self.components[0]):
                return int(self.components[0])
            return self.components[0]

    def __int__(self):
        return int(self.components[0])

    def __add__(self, other):
        if is_int(self) and is_int(other):
            return Expr(int(self) + int(other))
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

    Arguments:
    ---
    expression (str):
        Expression à interpréter (exemple : "5+2*x")

    variable (str):
        Nom de la variable (exemple : "x")

    remplacement (int):
        Entier par lequel remplacer la variable (exemple : 4)

    Return:
    ---
    (None|int):
        * None: Si l'expression est vide
        * Expr: Résultat de l'expression

    Raise:
    ---
    AssertError:
        * Si `expression` n'est pas un `str`
        * Si `variable` n'est pas un `str`
        * Si `remplacement` n'est pas un `int`
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
    return sum([int(i) for i in liste_terme])


def is_int(nb):
    """Vérifie si on peut cast un objet en int

    Arguments:
    ---
    nb(any):
        Nombre à cast en int

    """
    try:
        int(nb)
        return True
    except (ValueError, TypeError):
        return False


# region Tests
def test_somme():
    print("DEBUT DU TEST : Classe Sum")

    # TEST SIMPLIFICATION DE CONSTANTES
    var = str(Sum(18, 24, 22).value())
    assert var == "64", f"Mauvaise valeur : {var} au lieu de '64'"

    # TEST SIMPLIFICATION DE FRACTIONS CONSTANTES
    var = str(Sum(Div(1, 4), Div(1, 2)).value())
    assert var == "(3 / 4)", f"{var}"

    # TEST SIMPLIFICATION DE CONSTANTES AVEC VARIABLE (1 VAR)
    var = str(Sum(18, 24, 22, "a").value())
    assert var == "a + 64", f"Mauvaise valeur : {var} au lieu de 'a + 64'"

    # TEST SIMPLIFICATION DE CONSTANTES AVEC VARIABLES (PLUSIEURS VARS)
    var = str(Sum(1, 5, Sum("a", "b")).value())
    assert var == "a + b + 6",\
        f"Mauvaise valeur : {var} au lieu de 'a + b + 6'"

    # FACTORISATION D'UNE SOMME AVEC PLUSIEURS ITÉRATIONS DE VARIABLES (1 VAR)
    var = str(Sum(1, 5, "a", "a").value())
    assert var == "2 × a + 6",\
        f"Mauvaise valeur : {var} au lieu de '2 × a + 6'"

    # FACTORISATION D'UNE SOMME AVEC PLUSIEURS ITÉRATIONS DE VARIABLES
    # (PLUSIEURS VARS)
    var = str(Sum(1, 5, "a", "a", "a", "b", "b", "b").value())
    assert var == "3 × a + 3 × b + 6",\
        f"Mauvaise valeur : {var} au lieu de '3 × a + 3 × b + 6'"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE MULTIPLICATION (1 VAR)
    var = str(Sum("a", Mul(3, "a")).value())
    assert var == "4 × a", f"{var}"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE MULTIPLICATION
    # (PLUSIEURS VARS)
    var = str(Sum("a", Mul(3, "a"), "b", "b", Mul(40, "b")).value())
    assert var == "4 × a + 42 × b", f"{var}"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE DIVISION (1 VAR)
    s = Sum(Div("a", 4), "a").value()
    var = str(s)
    assert var == "(5 / 4) × a", f"{var}"

    var = str(Sum(Div("a", 4), "a", Div("a", 8), Div("a", 2), 18).value())
    assert var == "(15 / 8) × a + 18", f"{var}"

    # FACTORISATION D'UNE SOMME AVEC UN COMPOSANT DE DIVISION (PLUSIEURS VARS)
    var = str(Sum(Div("a", 4), "a", Div("b", 2), "b", 7).value())
    assert var == "(5 / 4) × a + (3 / 2) × b + 7", f"{var}"

    print("FIN DU TEST : Classe Sum")


def test_mul():
    print("DEBUT DU TEST : Classe Mul")

    # TEST MULTIPLICATION BASIQUE
    var = str(Mul(6, 7).value())
    assert var == "42", f"{var}"

    print("FIN DU TEST : Classe Mul")
    pass


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


def test_str_to_expr():
    print("Début du test : Fonction substituer_expr")

    var = substituer_expr("5+2*x", "x", 4)
    assert var == 13, f"{var}"
    var = substituer_expr("11037+53*x", "x", 12)
    assert var == 11673, f"{var}"

    print("Fin du test : Fonction substituer_expr")
# endregion


if __name__ == "__main__":
    test_somme()
    test_mul()
    test_div()
    test_str_to_expr()
