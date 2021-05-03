class arme:
    def __init__(self, server, id_arme):
        self.server =server 
        self.id_arme = id_arme
        self.nom = ""
        self.classe = ""
        self.dgt = 0
        self.niveau = 0
        self.style = ""  ## cac ou distance
        self.portee = "" ## portée d'un projectile, surtout pour le style de combat a distance
        self.position = {"x" : 0 , "y" : 0}
        self.id_region = 1
        self.load_arme()

    def load_arme(self):

        sql = """SELECT nom, classe, dgt, niveau, style, portee FROM arme WHERE id_arme=? """

        res = self.server.db.requete_db(sql, (self.id_arme,))[0]

        self.nom = res[0]
        self.classe = res[1]
        self.dgt = res[2]
        self.niveau = res[3] 
        self.style = res[4]
        self.portee = res[5]
