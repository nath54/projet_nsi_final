from calcul_formel import *

class Monstre:
    def __init__(self, server, id_monstre):
        self.server = server
        self.id_monstre = id_monstre
        self.nom = "" # changer les valeurs depuis la bdd lors du chargement du monstre
        self.pv = 0
        self.dgt =  0
        self.position = {"x": 0, "y": 0}
        self.id_region = 1
        self.etat = 0
        self.loot = ""
        self.load_monstre()


    def load_monstre(self): ## On charge le monstre en lui attribuant ses capacités à partir de la BDD
        sql = """" SELECT nom_monstre, pv, niveau, dgt, loot FROM monstre WHERE id_monstre =?"""
        res = self.server.db.requete_db(sql, (self.id_monstre,))[0]

        self.nom = res[0]
        self.pv = str(dict("forme": "random between", "values": [1,5] ))
        self.niveau = int(res[2])
        self.dgt = int(res[3])
        self.loot = res[4]

    def emplacement(self): ## Retourne la position du monstre
        return self.position

    def bouger(self, dep):  # Le serveur s'occupera des déplacements

        assert (isinstance(dep, tuple) or isinstance(dep, list)) and len(dep)==2, "Le déplacement n'est pas un tuple."
        assert isinstance(dep[0], int) and isinstance(dep[1], int),\
            "Les positions ne sont pas des entiers."

        npx, npy = self.position["x"]+dep[0], self.position["y"]+dep[1]

        if self.server.carte.est_case_libre(self.id_region, npx, npy):
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]

        position_ini = self.position

        if self.server.personnage.region_actu == self.id_region :   #Faire en sorte que le monstre suive le personnage
            if self.server.personnage.position == self.position["x"] + 2 and self.server.personnage.position == self.position["y"] + 2: # si l'utilisateur se situe à 2 cases du monstre
                while self.position != self.server.personnage.position :
                    self.position["x"] += dep[0]
                    self.position["y"] += dep[1]
                    if self.position["x"] == self.position["x"] + 6 and self.position["y"] == self.position["y"] + 6 :
                        self.position = position_ini  # Limite la distance que parcourt le monstre en suivant le joueur, le fait retourner à sa position initiale

    def modif_vie(self ,valeur_modif , fct=Sum):
        self.pv = fct(self.pv, valeur_modif)

        if self.pv > 0 :
            # Le monstre est positif
            pass

        if self.pv == 0 :
            # TODO: Monstre doit mourir et loot un item
            #self.remove()
            #return self.loot
            pass

        if self.pv < 0 :
            # Le monstre devient négatif, pensez a ajouter des changements de stats etc
            pass


##if __name__ = "__name__":
    #m = Monstre()

