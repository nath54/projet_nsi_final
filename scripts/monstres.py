class Monstre: 
    def __init__(self, server, id_monstre):
        self.server = server
        self.id_monstre = id_monstre
        self.nom = "" # changer les valeurs depuis la bdd lors du chargement du monstre
        self.pv = 0
        self.pv_max = 0
        self.armor = 0
        self.dgt =  0
        self.position = {"x": 0, "y": 0}
        self.id_region = 1
        self.loot = ""


    def load_monstre(self): ## On charge le monstre en lui attribuant ses capacités à partir de la BDD
        sql = """" SELECT nom_monstre, pv, niveau, armor, dgt, loot, position_x, position_y, id_region FROM monstre WHERE id_monstre =?"""
        res = self.server.db.requete_db(sql, (self.id_monstre,))[0]

        self.nom = res[0]
        self.pv = int(res[1])
        self.pv_max = int(res[1])
        self.niveau = int(res[2])
        self.armor = int(res[3])
        self.dgt = int(res[4])
        self.loot = res[5]
        self.position = {"x": int(res[6]), "y": int(res[7])}
        self.id_region = int(res[8])
        self.load_monstre()

    def emplacement(self): ## Retourne la position du monstre
        return self.position

    def bouger(self, dep):  # Le serveur s'occupera des déplacements
        ## Ajouter la collision avec les murs ...

        assert (isinstance(dep, tuple) or isinstance(dep, list)) and len(dep)==2, "Le déplacement n'est pas un tuple."
        assert isinstance(dep[0], int) and isinstance(dep[1], int),\
            "Les positions ne sont pas des entiers."

        npx, npy = self.position["x"]+dep[0], self.position["y"]+dep[1]

        if self.server.carte.est_case_libre(self.id_region, npx, npy):
            self.position["x"] += dep[0]
            self.position["y"] += dep[1]

        if self.server.personnage.region_actu == self.id_region :   #Faire en sorte que le monstre suive le personnage
            #if self.server.carte.
            while self.position != self.server.personnage.position :
                self.position["x"] += dep[0]
                self.position["y"] += dep[1]

    def modif_vie(self, pv):
        if self.pv > 0 :
            # Le monstre est positif
            pass 

        if self.pv == 0 :
            # TODO: Monstre doit mourir et loot un item
            pass
        if self.pv < 0 :
            # Le monstre devient négatif, pensez a ajouter des changements de stats etc 
            pass

    
#if __name__ = "__name__":
    #m = Monstre()

