# region Imports :
import json
import time

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
        self.competences = {}
        self.quetes = {}
        self.equipements = {}
        self.id_tete = 1
        self.id_cheveux = 1
        self.id_barbe = 1
        self.id_haut = 1
        self.id_bas = 1
        self.id_pied = 1
        self.server = server
        self.divers = {
            "cooldowns": {}
        }
        self.load_perso()

    def load_perso(self):
        """Charge les données d'un personnage

        Parameters:
            id(int):
                ID du personnage dans la base de données
            db(DB):
                Instance de la base de données

        """
        sql = """SELECT pseudo, sexe, classe, vie, stamina, mana, armor, niveau, argent, experience, experience_tot, competence, quetes, region_actu, position_x, position_y, id_tete, id_cheveux, id_barbe, id_haut, id_bas, id_pieds
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
        comp = json.loads(res[11])
        self.competences = {}
        # for k,v in comp.items():
        #     self.competences[int(k)] = v;
        self.quetes = res[12]
        self.region_actu = int(res[13])
        self.position = {"x": int(res[14]), "y": int(res[15])}
        self.id_tete = int(res[16])
        self.id_cheveux = int(res[17])
        self.id_barbe = int(res[18])
        self.id_haut = int(res[19])
        self.id_bas = int(res[20])
        self.id_pied = int(res[21])
        #
        self.tp_bouger = 0.1
        self.dernier_bouger = 0
        # TODO: faire que si un perso est deja sur la case, on le décale

        #
        sql = """SELECT competences.id_competence FROM competences INNER JOIN classes_competences ON classes_competences.id_competence = competences.id_competence WHERE nom_classe = ? AND niv_min <= ?;"""
        res = self.server.db.requete_db(sql, (self.classe, self.niveau))

        for compteur in range(len(res)):
            self.competences[compteur+1] = res[compteur][0]
        
        print(self.competences)


    def bouger(self, dep, cooldown=False):
        """S'assure que le personnage peut se déplacer et le déplace

        Parameters:
            dep(tuple<int, int>): Déplacement du personnage sous forme (x, y)
        """
        assert (isinstance(dep, tuple) or isinstance(dep, list)) and len(dep)==2, "Le déplacement n'est pas un tuple."
        assert isinstance(dep[0], int) and isinstance(dep[1], int),\
            "Les positions ne sont pas des entiers."

        if cooldown:
            if time.time() - self.dernier_bouger < self.tp_bouger:
                return
            self.dernier_bouger = time.time()

        npx, npy = self.position["x"]+dep[0], self.position["y"]+dep[1]

        if self.server.carte.est_case_libre(self.region_actu, npx, npy):
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]
            self.server.send_to_user(self.id_utilisateur, {"action": "position_perso", "x":self.position["x"], "y":self.position["y"]})
            self.server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":self.id_utilisateur, "x":self.position["x"], "y":self.position["y"], "region":self.region_actu}, [self.id_utilisateur])

    def emplacement(self):
        """Renvoie la position du personnage"""
        return self.position

    def prendre_objet(self, id_objet):
        """Ajoute un objet à l'inventaire du personnage

        TODO: Revoir format de la fonction

        """
        #objet = self.server.carte.cases_objets
        est_ramassable = False

        if not est_ramassable:
            sql = """ INSERT INTO inventaire('id_objet', 'id_utilisateur', 'quantite') VALUES ('id_objet', 'id_utilisateur' = ?, 'quantite')"""
            res = self.server.db.action_db(sql, (self.id_utilisateur,))[0]

        else:
            pass

    def attaquer(self):

        npx, npy = self.position["x"]+1, self.position["y"]+1 # Permet de regarder la case qui suit (Pour voir si il y a un éventuel monstre)
        dgt = -1 ## Dégat de base si pas d'arme

        if self.equipements != {"arme": None}:
            dgt = self.server.arme.dgt

        if self.server.monstre.position == {'x': npx, 'y': npy}: # Si le monstre se situe a proximité du joueur
            self.server.monstre.modif_vie(dgt)
            pass

    def interagir(self):
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

    def subit_degats(self, degats):
        if "bouclier" in self.divers.keys():
            if self.divers["bouclier"] >= degats:
                self.divers["bouclier"] -= degats
                degats = 0
            else:
                self.divers["bouclier"] = 0
                degats -= self.divers["bouclier"]
            #TODO: envoyer self.divers au client
            self.server.send_to_user(self.id_utilisateur, {"action":"divers", "value":self.divers})
            self.server.serveurWebsocket.send_all({"action": "divers_joueur", "id_joueur":self.id_utilisateur, "value":self.divers_joueur}, [self.id_utilisateur])



        self.vie -= degats
        if self.vie <= 0:
            self.vie = 0
            self.meurt()
        else:
            self.server.send_to_user(self.id_utilisateur, {"action":"vie", "value":self.vie, "max_v": self.vie_max})
            self.server.serveurWebsocket.send_all({"action": "vie_joueur", "id_joueur":self.id_utilisateur, "value":self.vie, "max_v": self.vie_max}, [self.id_utilisateur])

    def change_mana(self, delta):
        self.mana += delta
        if self.mana > self.mana_max:
            self.mana = self.mana_max
        if self.mana < 0:
            self.mana = 0
        self.server.send_to_user(self.id_utilisateur, {"action":"mana", "value":self.mana, "max_v": self.mana_max})
        self.server.serveurWebsocket.send_all({"action": "mana_joueur", "id_joueur":self.id_utilisateur, "value":self.mana, "max_v": self.mana_max}, [self.id_utilisateur])

    def update_cooldown(self, nom_comp):
        # Ici, le but est d'envoyer l'information que la compétence a été utilisée
        self.server.send_to_user(self.id_utilisateur, {"action":"cooldown_comp", "nom_comp":nom_comp, "time": self.divers["cooldowns"][nom_comp]})

    def meurt(self):
        self.position["x"] = 0
        self.position["y"] = 0
        self.vie = int(self.vie_max * 0.8)
        self.mana = self.mana_max
        self.server.send_to_user(self.id_utilisateur, {"action": "position_perso", "x":self.position["x"], "y":self.position["y"]})
        self.server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":self.id_utilisateur, "x":self.position["x"], "y":self.position["y"], "region":self.region_actu}, [self.id_utilisateur])
        self.server.send_to_user(self.id_utilisateur, {"action":"vie", "value":self.vie, "max_v": self.vie_max})
        self.server.serveurWebsocket.send_all({"action": "vie_joueur", "id_joueur":self.id_utilisateur, "value":self.vie, "max_v": self.vie_max}, [self.id_utilisateur])
        self.server.send_to_user(self.id_utilisateur, {"action":"mana", "value":self.mana, "max_v": self.mana_max})
        self.server.serveurWebsocket.send_all({"action": "mana_joueur", "id_joueur":self.id_utilisateur, "value":self.mana, "max_v": self.mana_max}, [self.id_utilisateur])

    def changement_region(self):
        pass

