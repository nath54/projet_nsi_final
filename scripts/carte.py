
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

        sql = "SELECT x , y, id_objet FROM regions_objets WHERE id_region=?"
        objs = self.server.db.requete_db(sql, (self.id_region, ))
        for t in objs:
            self.cases_objets[str(t[0])+"_"+str(t[1])] = int(t[2])

        #

        self.ennemis = {}
        self.pnjs = {}

    def get_case(self, x, y):
        i = f"{x}_{y}"
        if i in self.cases_terrains.keys():
            return self.cases_terrains[i]
        else:
            return 0

    def get_case_obj(self, x, y):
        i = f"{x}_{y}"
        if i in self.cases_objets.keys():
            return self.cases_objets[i]
        else:
            return 0

class Carte:
    def __init__(self, server):
        self.server = server
        self.db = server.db
        self.regions = {}
        self.terrains = {}
        self.objets = {}
        self.load()
        #

    def est_case_libre(self, region,x, y):
        if region not in self.regions.keys():
            raise UserWarning("Erreur ! Région inconnue")

        k = str(x)+"_"+str(y)
        tp_case = self.regions[region].get_case(x,y)
        if tp_case not in self.terrains.keys():
            raise UserWarning("Erreur !")

        tp_objet = self.regions[region].get_case_obj(x,y)
        if tp_objet not in self.objets.keys():
            raise UserWarning("Erreur !")

        if self.objets[tp_objet]["collision"]: ## Si une case est occupée par un arbre ou autre,
            return False                                  ## alors le déplacement est impossible

        if not self.server.carte.terrains[tp_case]["peut_marcher"]: ## Si une case est occupée par un arbre ou autre,
            return False

        for p in self.server.personnages.values():
            if p.position["x"]==x and p.position["y"]==y:
                return False

        # ca devrait être bon la
        return True

    def load(self):
        sql = "SELECT id_region,nom FROM regions";
        regs = self.server.db.requete_db(sql)
        for r in regs:
            self.regions[r[0]]=Region(self, self.server, r[0], r[1])
        sql = "SELECT id_terrain, nom, peut_marcher, cultivable, objet_dessus FROM terrain"
        ters = self.server.db.requete_db(sql)
        for t in ters:
            self.terrains[t[0]] = {
                "nom": t[1],
                "peut_marcher": bool(t[2]),
                "cultivable": bool(t[3]),
                "objet_dessus": bool(t[4])
            }

        sql = "SELECT id_objet, nom, collision FROM objets"
        objs = self.server.db.requete_db(sql)
        for o in objs:
            self.objets[o[0]] = {
                "nom": o[1],
                "collision": bool(o[2])
            }
