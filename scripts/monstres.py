class monstre:
    def __init__(self, server, id_monstre):
        self.id_monstre = id_monstre
        self.nom = "" # charger depuis la bdd
        self.pv = ""
        self.armor =""
        self.dgt = ""
        pass

    def load_monstre(self):
        sql = """" SELECT nom_monstre, pv, armor, dgt FROM monstre WHERE id_monstre =?"""
        res = self.server.db.requete_db(sql, (self.id_monstre,))[0]

        self.nom = res[0]
        self.pv = int(res[1])
        self.armor = int(res[2])
        self.dgt = int(res[3])
        
        pass

    def bouger(self):
        pass
