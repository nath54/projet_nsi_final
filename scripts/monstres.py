class monstre:
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

    def emplacement(self): ## Retourne la position du monstre
        return self.position

    def bouger(self):
        pass
