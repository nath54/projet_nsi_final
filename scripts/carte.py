
class Region:
    def __init__(self, server, carte, id_region, nom):
        self.id_region = id_region
        self.carte = carte
        self.server = server
        self.cases_terrains = {} # key "x_y": type du terrain
                                 # comme ca, on y accede cases_terrains[f"{x}_{y}"] => le type de la case
        self.cases_objets = {}   # key "x_y": type de l'objet
                                 # comme ca, on y accede ca[f"{x}_{y}"] => le type de l'objet
        # on charge les terrains

        sql = "SELECT x , y, id_terrain FROM regions_terrains WHERE id_region=?"
        ters = self.server.db.requete_db(sql, (self.id_region, ))
        for t in ters:
            self.cases_terrains[str(t[0])+"_"+str(t[1])] = int(t[2])

    def get_case(self, x, y):
        if f"{x}_{y}" in self.cases_terrains.keys():
            return self.cases_terrains[f"{x}_{y}"]
        else:
            return 0

class Carte:
    def __init__(self, server):
        self.server = server
        self.db = server.db
        self.regions = {}
        self.terrains = {}

    def load(self):
        sql = "SELECT id,nom FROM regions";
        regs = self.server.db.requete_db(sql)
        for r in regs:
            print(r[1])
            self.regions[r[0]]=Region(self, self.server, r[0], r[1])
        sql = "SELECT id_terrain, nom, peut_marcher, cultivable, objet_dessus FROM terrains"
        ters = self.server.db.requete_db(sql)
        for t in ters:
            self.terrains[t[0]] = {
                "nom": t[1],
                "peut_marcher": bool(t[2]),
                "cultivable": bool(t[3]),
                "objet_dessus": bool(t[4])
            }
