
class personnage:
    def __init__(self, nom, classe, sexe):
        self.nom = nom
        self.sexe = sexe
        self.classe = classe
        self.position = {"x": 0, "y": 0}
        self.sprite_fixe = "TODO: sprite perso immobile"
        self.sprite_droite = "TODO: sprite perso à droite"
        self.sprite_gauche = "TODO: sprite perso à gauche"
        self.sprite_haut = "TODO: sprite perso en haut"
        self.sprite_bas = "TODO: sprite perso en bas"
        self.vie = 20
        self.max_vie = 20
        self.niveau = 0
        self.xp = 0
        self.stamina = 20
        self.mana = 20
        self.mana_max = 20
        self.armor = 0

    def afficher(self):
        self.sprite_fixe

    def bouger(self, dep):  # déplacement sous la forme de dict (dep x, dep y)
        """S'assure que le personnage peut se déplacer et le déplace

        Parameters:
            dep(tuple<int, int>): Déplacement du personnage sous forme (x, y)

        TODO: Ajouter tests de collision

        """
        peut_se_depl = True
        if peut_se_depl:
            self.position["x"] += dep["x"]
            self.position["y"] += dep["y"]

    def emplacement(self):
        return self.position

    def prendre_objet(self, touche):
        if touche == "e" or touche == "E":

            pass

    def attaquer(self, touche):
        pass

    def interagir(self, touche):
        if touche == "e" or touche == "E":
            pass

    def gagner_xp(self, xp):
        pass

    def level_up(self):
        # TODO: Condition jamais remplie
        if self.xp == self.xp + 100:
            self.niveau = self.niveau + 1

    def perdre_vie(self, dgt_monstre):
        pass

    def gagner_vie(self):
        pass

def test():
    print("début des tests")
    p = personnage("Lance", "mage", "homme")

    p.bouger("up")
    assert p.position == {"x": 0, "y": 1}
    p.bouger("left")
    assert p.position == {"x": -1, "y": 1}
    p.bouger("right")
    assert p.position == {"x": 0, "y": 1}
    p.bouger("up")
    assert p.position == {"x": 0, "y": 2}

    print("fin des tests")
