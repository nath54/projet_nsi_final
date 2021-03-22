# region Imports :

import json

# Méthode 1 : mariadb
try:
    import mariadb  # ignore unresolved-import error
except Exception as e:
    # Méthode 2 : mysql
    try:
        import mysql.connector as mariadb  # ignore unresolved-import error
    except Exception as e:
        # Rien n'est installé
        raise UserWarning("Il faut installer la librairie mariadb ou mysql !")
# endregion


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
        region(int):
            ID de la région dans laquelle se trouve le joueur
        position(dict<str: int>):
            Décrit la position du personnage avec :
                "x": La position x du personnage sur la map
                "y": la position y du personnage sur la map
        sprite_fixe_droite(str):
            Nom de l'image du personnage fixe qui regarde vers la droite
        sprit_fixe_gauche(str):
            Nom de l'image du personnage fixe qui regarde vers la gauche
        sprite_droite_pied_droit(str):
            Nom de l'image du personnage allant vers la droite et qui s'appui sur son pied droit
        sprite_droite_pied_gauche(str):
            Nom de l'image du personnage allant vers la droite et qui s'appui sur son pied gauche
        sprite_gauche_pied_droit(str):
            Nom de l'image du personnage allant vers la gauche et qui s'appui sur son pied droit
        sprite_gauche_pied_gauche(str):
            Nom de l'image du personnage allant vers la gauche et qui s'appui sur son pied gauche
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
            Niveau actuelle du personnage
            TODO: Apprendre compétences en fonction de la classe
                  Augmentation stats en fonction de la classe
        xp(int):
            Nombre de point d'XP actuel
            TODO: Déterminer combien d'XP avant de level up (trouver suite
                  définissant le besoin d'XP avant level up)
        stamina(int):
            TODO: Utilité ?
        mana(int):
            Quantité actuelle de mana
        mana_max(int):
            Quantité maximale de mana
        armor(int):
            Défense de base du personnage ?
            TODO: Utilité ?
        argent(int):
            Argent transporté par le personnage

    TODO: Ajouter stat d'attaque
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
        self.argent = 0

    def load_perso(self, id, db):
        """Charge les données d'un personnage

        Parameters:
            id(int):
                ID du personnage dans la base de données
            db(DB):
                Instance de la base de données
        """
        sql = """SELECT pseudo, sexe, classe, region, position, vie, vie_max,
                        niveau, experience, stamina, mana, mana_max,
                        inventaire, armor, argent
                 FROM utilisateurs
                 WHERE id_utilisateur = """ + id
        curseur = db.cursor()
        curseur.execute(sql)
        res = [ligne for ligne in curseur]

        self.nom = res[0]
        self.sexe = res[1]
        self.classe = res[2]
        self.region = res[3]
        self.position = json.loads(res[4])
        self.vie = res[5]
        self.vie_max = res[6]
        self.niveau = res[7]
        self.xp = res[8]
        self.stamina = res[9]
        self.mana = res[10]
        self.mana_max = res[11]
        self.inventaire = res[12]
        self.armor = res[13]
        self.argent = res[14]

    def afficher(self):
        # self.sprite_fixe
        pass

    def bouger(self, dep):
        """S'assure que le personnage peut se déplacer et le déplace

        Parameters:
            dep(tuple<int, int>): Déplacement du personnage sous forme (x, y)

        TODO: Ajouter tests de collision

        """
        assert isinstance(dep, tuple), "Le déplacement n'est pas un tuple."
        assert isinstance(dep[0], int) and isinstance(dep[1], int),\
            "Les positions ne sont pas des entiers."
        peut_se_depl = True
        if peut_se_depl:
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]
        else:
            pass

    def emplacement(self):
        """Renvoie la position du personnage"""
        return self.position

    def prendre_objet(self, touche):
        """Ajoute un objet à l'inventaire du personnage

        TODO: Revoir format de la fonction
        """
        if touche == "e" or touche == "E":
            pass

    def attaquer(self, touche):
        pass

    def interagir(self, touche):
        if touche == "e" or touche == "E":
            pass

    def gagner_xp(self, xp):
        """Permet de donner de l'XP au personnage

        Parameters:
            xp(int): Nombre de point d'XP à donner.

        TODO: Appel à la fonction `self.level_up()` depuis cette fonction après
              avoir fait vérification. (trouver suite définissant l'XP
              nécessaire pour le level_up)
        """
        pass

    def level_up(self):
        """Augmente le niveau du personnage

        TODO: Augmenter stats de base
        """
        # TODO: Condition jamais remplie
        if self.xp == self.xp + 100:
            self.niveau = self.niveau + 1

    def modifier_vie(self, vie):
        """Modifie la vie du personnage et check s'il est mort

        Parameters:
            vie(int):
                Vie à ajouter/enlever
        """
        self.vie += vie
        if self.vie <= 0:
            # TODO: Perso doit mourir
            pass
        elif self.vie > self.vie_max:
            self.vie = self.vie_max


if __name__ == "__main__":
    print("début des tests")
    p = personnage("Lance", "mage", "homme")

    p.bouger((25, 25))
    pos = p.emplacement()
    assert pos["x"] == 25 and pos["y"] == 25, "Les positions sont fausses"
    p.bouger((25, 25))

    pos = p.emplacement()
    assert pos["x"] == 50 and pos["y"] == 50, "Positions fausses"

    p.modifier_vie(-10)
    assert p.vie == 10, f"Vie fausse : {p.vie} au lieu de 10"
    p.modifier_vie(20)
    assert p.vie == 20, f"Vie fausse : {p.vie} au lieu de 20"
    print("fin des tests")
