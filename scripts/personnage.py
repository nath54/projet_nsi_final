
class personnage:
    """Classe du personnage

    Attributes:
        nom(str):
            Nom du personnage
        sexe(str):
            Genre du personnage
        classe(str):
            Classe du personnage (TODO: changer stats en fonction des
                                        classes)
        position(dict<str: int>):
            Décrit la position du personnage avec :
                "x": La position x du personnage sur la map
                "y": la position y du personnage sur la map
                "region": ID de la région dans laquelle est le perso
        sprite_fixe(str):
            Nom de l'image du personnage fixe
        sprite_droite(str):
            Nom de l'image du personnage allant vers la droite
        sprite_gauche(str):
            Nom de l'image du personnage allant vers la gauche
        sprite_haut(str):
            Nom de l'image du personnage allant vers la haut
        sprite_bas(str):
            Nom de l'image du personnage allant vers la bas
        vie(int):
            Vie actuelle du personnage
            TODO: Où on respawn si ça tombe à zéro ?
        vie_max(int):
            Vie maximale du personnage
        niveau(int):
            Niveau actuelle des compétences
            TODO: Apprendre compétences en fonction de la classe
                  Augmentation stats en fonction de la classe
        xp(int):
            Nombre de point d'XP actuel
            TODO: Déterminer combien d'XP avant de level up (coût augmentant)
        stamina(int):
            TODO: Utilité ?
        mana(int):
            Quantité actuelle de mana
        mana_max(int):
            Quantité maximale de mana
        armor(int):
            Défense de base du personnage ?
            TODO: Utilité ?

    TODO: Ajouter attaque
    TODO: Si le personnage existe, le charger depuis la DB, sinon créer son
          entrée dans la base de données et le charger
    TODO: Permettre le stockage de l'animation du personnage dans les variables
          `sprite_`
    """
    def __init__(self, nom, classe, sexe):
        self.nom = nom
        self.sexe = sexe
        self.classe = classe
        self.region = 0
        self.position = {"x": 0, "y": 0}
        self.sprite_fixe_droite = "TODO: sprite perso immobile qui regarde à droite"
        self.sprite_fixe_gauche = "TODO: sprite perso immobile qui regarde à gauche"
        self.sprite_droite_pied_droit = "TODO: sprite perso à droite appui sur pied droit"
        self.sprite_droite_pied_gauche = "TODO: sprite perso à droite appui sur pied gauche"
        self.sprite_gauche_pied_droit = "TODO: sprite perso à gauche appui sur pied droit"
        self.sprite_gauche_pied_gauche = "TODO: sprite perso à gauche appui sur pied gauche"
        self.sprite_haut = "TODO: sprite perso en haut"
        self.sprite_bas = "TODO: sprite perso en bas"
        self.vie = 20
        self.vie_max = 20
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
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]
        
        else:
            pass 

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

    def modifier_vie(self, vie):
        """Modifie la vie du personnage et check s'il est mort

        Parameters:
            vie(int):
                Vie à ajouter/enlever
        """
        pass

def test():
    print("début des tests")
    p = personnage("Lance", "mage", "homme")

    p.bouger((25, 25))
    assert p.position == {"x": 25, "y": 25}
    p.bouger((25, 25))
    assert p.position == {"x": 50, "y": 50}
    print("fin des tests")
