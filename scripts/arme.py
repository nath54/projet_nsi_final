class arme:
    def __init__(self, server, id_arme):
        self.server =server 
        self.id_arme = id_arme
        self.nom = ""
        self.classe = ""
        self.niveau = 0
        self.style = ""  ## cac ou distance
        self.portee = "" ## portée d'un projectile, surtout pour le style de combat a distance
        self.position = {"x" : 0 , "y" : 0}
        self.id_region = 1
        self.load_arme()

    def load_arme(self):

        sql = """SELECT nom, classe, niveau, style, portee FROM arme WHERE id_arme=? """

        res = self.server.db.requete_db(sql, (self.id_arme,))[0]
        pass