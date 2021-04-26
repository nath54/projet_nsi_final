# region Imports :
import json

# endregion


class Personnage:
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
    def __init__(self, server, id_utilisateur):
        self.id_utilisateur = id_utilisateur
        self.nom = ""  # a mettre en place dans la bdd
        self.sexe = ""  # a mettre en place dans la bdd
        self.classe = ""  # a mettre en place dans la bdd
        self.region_actu = 1
        self.position = {"x": 0, "y": 0}
        self.vie = 20
        self.vie_max = 20
        self.niveau = 0
        self.xp = 0
        self.stamina = 20
        self.mana = 20
        self.mana_max = 20
        self.armor = 0
        self.argent = 0
        self.inventaire = []
        self.quetes = {}
        self.equipements = {}
        self.server = server
        self.load_perso()

    def load_perso(self):
        """Charge les données d'un personnage

        Parameters:
            id(int):
                ID du personnage dans la base de données
            db(DB):
                Instance de la base de données

        """
        sql = """SELECT pseudo, sexe, classe, vie, stamina, mana, armor, niveau, argent, experience, experience_tot, competence, quetes, region_actu, position_x, position_y
                 FROM utilisateurs
                 WHERE id_utilisateur = ?"""
        res = self.server.db.requete_db(sql, (self.id_utilisateur,))[0]

        self.nom = res[0]
        self.sexe = res[1]
        self.classe = res[2]
        self.vie = int(res[3])
        self.vie_max = int(res[3])
        self.stamina = int(res[4])
        self.stamina_max = int(res[4])
        self.mana = int(res[5])
        self.mana_max = int(res[5])
        self.armor = res[6]
        self.niveau = int(res[7])
        self.argent = int(res[8])
        self.xp = int(res[9])
        self.xp_tot = int(res[10])
        self.competence = res[11]
        self.quetes = res[12]
        self.region_actu = int(res[13])
        self.position = {"x": int(res[14]), "y": int(res[15])}
        # TODO: faire que si un perso est deja sur la case, on le décale

    def bouger(self, dep):
        """S'assure que le personnage peut se déplacer et le déplace

        Parameters:
            dep(tuple<int, int>): Déplacement du personnage sous forme (x, y)

        TODO: Ajouter tests de collision

        """
        assert (isinstance(dep, tuple) or isinstance(dep, list)) and len(dep)==2, "Le déplacement n'est pas un tuple."
        assert isinstance(dep[0], int) and isinstance(dep[1], int),\
            "Les positions ne sont pas des entiers."

        npx, npy = self.position["x"]+dep[0], self.position["y"]+dep[1]

        if self.server.carte.est_case_libre(self.region_actu, npx, npy):
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]
            print("perso ",self.id_utilisateur)
            self.server.send_to_user(self.id_utilisateur, {"action": "position_perso", "x":self.position["x"], "y":self.position["y"]})
            self.server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":self.id_utilisateur, "x":self.position["x"], "y":self.position["y"], "region":self.region_actu}, [self.id_utilisateur])

    def emplacement(self):
        """Renvoie la position du personnage"""
        return self.position

    def prendre_objet(self, id_objet):
        """Ajoute un objet à l'inventaire du personnage

        TODO: Revoir format de la fonction

        """
        est_ramassable = True
        if est_ramassable:
            self.inventaire.append(self.inventaire)

    def attaquer(self):
        pass

    def interagir(self, touche):
        pass

    def gagner_xp(self, xp, niv_monstre, vie_monstre):
        """Permet de donner de l'XP au personnage

        Parameters:
            xp(int): Nombre de point d'XP à donner.

        TODO: Appel à la fonction `self.level_up()` depuis cette fonction après
              avoir fait vérification. (trouver suite définissant l'XP
              nécessaire pour le level_up)

        """
        if niv_monstre < self.niveau :
            self.xp = self.xp

        if vie_monstre == 0 :
            self.xp = self.xp + xp
            self.level_up()

    def level_up(self):
        """Augmente le niveau du personnage

        TODO: Augmenter stats de base

        """
        # TODO: Condition jamais remplie
        L = 100
        if self.xp == L :
            self.xp = 0
            self.niveau = self.niveau + 1
            L = L + 100  ## Valeur de la limite pour augmenter de niveau à changer si besoin
            self.vie_max = self.vie_max + 50     ## Valeur de l'augmentation des stats à voir
            self.mana_max = self.mana_max + 50

        if self.xp > L :
            self.xp = self.xp - L
            self.niveau = self.niveau + 1
            L = L + 100  ## Valeur de la limite pour augmenter de niveau à changer si besoin
            self.vie_max = self.vie_max + 50     ## Valeur de l'augmentation des stats à voir
            self.mana_max = self.mana_max + 50

        else:
            pass

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

    def changement_region(self):
        if not self.server.carte.cases_terrains :  # si le joueur marche sur une case noir ou un élément qui va trigger le passage
            self.region_actu = self.server.Region.id_region
            self.server.carte.load()
            # TODO : définir une nouvelle position à la suite du changement
            self.load_perso()
        pass


# if __name__ == "__main__":
#     print("début des tests")
#     p = personnage("Lance", "mage", "homme")

#     p.bouger((25, 25))
#     pos = p.emplacement()
#     assert pos["x"] == 25 and pos["y"] == 25, "Les positions sont fausses"
#     p.bouger((25, 25))

#     pos = p.emplacement()
#     assert pos["x"] == 50 and pos["y"] == 50, "Positions fausses"

#     p.modifier_vie(-10)
#     assert p.vie == 10, f"Vie fausse : {p.vie} au lieu de 10"
#     p.modifier_vie(20)
#     assert p.vie == 20, f"Vie fausse : {p.vie} au lieu de 20"
#     print("fin des tests")
