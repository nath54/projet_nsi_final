from calcul_formel import * # pour les pv et les attaques
import random # pour les pv et les attaques
import time # pour les temps des etats
import json # pour les formes

class Monstre:
    def __init__(self, server, id_monstre_spawn, id_monstre, id_region, pos):
        self.server = server
        self.id_monstre_spawn = id_monstre_spawn
        self.id_monstre = id_monstre
        self.nom = "" # changer les valeurs depuis la bdd lors du chargement du monstre
        self.pv = {}
        self.dgt =  {}
        self.position = {"x": 0, "y": 0}
        self.id_region = 1
        self.etat = "vivant" # il sera vivant quand il aura spawn
        self.dernier_etat = time.time()
        self.loot = ""
        self.load_monstre(id_region, pos)

    def get_value_from_formes(self, forme):
        if forme["forme"] == "value":
            return forme["value"]
        elif forme["forme"] == "random between":
            return random.randint(*forme["values"])
        elif forme["forme"] == "random forme between":
            val = random.randint(*forme["values"])
            return substituer_expr(forme["expr"],"x",val)

    def set_position(self):
        k = str(self.position["x"])+"_"+str(self.position["y"])
        self.server.carte.regions[self.id_region].monstres_pos[self] = k
        #TODO : envoyer la nouvelle position aux joueurs
        self.server.serveurWebsocket.send_all({"action":"new_monstre_pos", "id_spawn":self.id_monstre_spawn, "x": self.position["x"], "y": self.position["y"]})

    def load_monstre(self, id_region, position): ## On charge le monstre en lui attribuant ses capacités à partir de la BDD
        sql = "SELECT nom, pv, niveau, dgt, loot FROM monstre WHERE id_monstre = ?;"
        res = self.server.db.requete_db(sql, args = tuple([self.id_monstre]))[0]

        self.nom = res[0]

        self.pv = json.loads(res[1])
        self.pv = self.get_value_from_formes(self.pv)

        self.niveau = int(res[2])

        self.dgt = json.loads(res[3])
        # on va guarder les dégats sous la forme de dictionnaire

        self.etat= "vivant"
        self.loot = res[4]
        #

        self.position = position
        self.id_region = id_region
        # on update la position dans la region
        self.set_position()

        #
        self.joueur_detecte = None
        self.detection_joueur = 3 # Rayon de détection des joueurs proches
        self.perte_joueur = 5 # Si le joueur s'éloigne trop, le monstre le perd
        self.portee_attaque = 1 # La portée d'attaque du monstre

        # Compteurs déplacements
        self.dernier_bouger = 0
        self.tp_bouger = 1
        self.nb_bloque = 0
        self.patiente_bloque = 5

        # Compteur deplacements retours
        self.position_base = self.position
        self.compteur_deplacements_retour = 0
        self.max_compteur_deplacement_retour = 5


    def emplacement(self): ## Retourne la position du monstre
        return self.position

    def bouger(self, dep, test_est_libre_fait=None):  # Le serveur s'occupera des déplacements

        assert (isinstance(dep, tuple) or isinstance(dep, list)) and len(dep)==2, "Le déplacement n'est pas un tuple."
        assert isinstance(dep[0], int) and isinstance(dep[1], int),\
            "Les positions ne sont pas des entiers."

        est_libre = test_est_libre_fait
        if est_libre == None:
            npx, npy = self.position["x"]+dep[0], self.position["y"]+dep[1]
            est_libre = self.server.carte.est_case_libre(self.id_region, npx, npy)

        if est_libre:
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]

            # on update la position dans la region
            self.set_position()

        """
        position_ini = self.position

        if self.server.personnage.region_actu == self.id_region :   #Faire en sorte que le monstre suive le personnage
            if self.server.personnage.position == self.position["x"] + 2 and self.server.personnage.position == self.position["y"] + 2: # si l'utilisateur se situe à 2 cases du monstre
                while self.position != self.server.personnage.position :
                    self.position["x"] += dep[0]
                    self.position["y"] += dep[1]
                    if self.position["x"] == self.position["x"] + 6 and self.position["y"] == self.position["y"] + 6 :
                        self.position = position_ini  # Limite la distance que parcourt le monstre en suivant le joueur, le fait retourner à sa position initiale
        """


    def modif_vie(self ,valeur_modif , fct=Sum):
        self.pv = fct(self.pv, valeur_modif)
        est_lootable = False

        if self.pv > 0 : # Le monstre est positif
            pass

        if self.pv == 0 :
            # TODO: Monstre doit mourir et loot un item
            self.etat = "mort"
            if not est_lootable:
                self.server.objet.load_objet()

            pass

        if self.pv < 0 : # Le monstre devient négatif, pensez a ajouter des changements de stats etc
            pass


##if __name__ = "__name__":
    #m = Monstre()

