
from monstres import Monstre

class Region:
    def __init__(self, server, carte, id_region, nom):
        self.id_region = id_region
        self.carte = carte
        self.server = server
        self.cases_terrains = {} # key "x_y": type du terrain
                                 # comme ca, on y accede cases_terrains[f"{x}_{y}"] => le type de la case
        self.cases_objets = {}   # key "x_y": type de l'objet
                                 # comme ca, on y accede ca[f"{x}_{y}"] => le type de l'objet
        self.spawn_monstres = {} # key id_monstre_spawn
                                 # value : "x_y"
        self.monstres_pos = {}   # key : "x_y"
                                 # value : id_monstre_spawn
        self.ennemis = {}  # key id_monstre_spawn
                            # value : Ennemi
        self.pnjs = {}

        # on charge les terrains
        sql = "SELECT x , y, id_terrain FROM regions_terrains WHERE id_region=?"
        ters = self.server.db.requete_db(sql, (self.id_region, ))
        for t in ters:
            self.cases_terrains[str(t[0])+"_"+str(t[1])] = int(t[2])

        # on charge les objets
        sql = "SELECT x , y, id_objet FROM regions_objets WHERE id_region=?"
        objs = self.server.db.requete_db(sql, (self.id_region, ))
        for t in objs:
            self.cases_objets[str(t[0])+"_"+str(t[1])] = int(t[2])

        # on charge les monstres
        sql = "SELECT id_x, y, id_monstre FROM regions_monstres WHERE id_region=?"
        objs = self.server.db.requete_db(sql, (self.id_region, ))
        for t in objs:
            # self.spawn_monstres[str(t[0])+"_"+str(t[1])] = int(t[2])
            self.spawn_monstres[int(t[2])] = str(t[0])+"_"+str(t[1])
        #

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

    def get_case_monstre(self, x, y):
        i = f"{x}_{y}"
        if i in self.monstres_pos.keys():
            return self.monstres_pos[i]
        else:
            return 0

    def launch_monstres(self):
        # les pos sont de la forme "x_y"
        for id_monstre_spawn, pos in self.spawn_monstres.items():
            id_monstre = self.carte.type_monstres_spawns[id_monstre_spawn]
            lst = pos.split("_")
            position = {"x":int(lst[0]), "y":int(lst[1])}
            monstre = Monstre(self.server,id_monstre_spawn, id_monstre, self.id_region, position)
            self.ennemis[id_monstre_spawn]

class Carte:
    """Gère toutes les régions, les collisions..."""
    def __init__(self, server):
        self.server = server
        self.db = server.db
        self.regions = {}
        self.terrains = {}
        self.objets = {}
        self.type_monstres_spawns = {}
        self.load()
        #

    def est_case_libre(self, region,x, y):
        if region not in self.regions.keys():
            raise UserWarning("Erreur ! Région inconnue")

        k = str(x)+"_"+str(y)

        # on regarde les terrains
        tp_case = self.regions[region].get_case(x,y)
        if tp_case not in self.terrains.keys():
            raise UserWarning("Erreur !")
        if not self.server.carte.terrains[tp_case]["peut_marcher"]: ## Si une case est occupée par un arbre ou autre,
            return False

        # on regarde les objets
        tp_objet = self.regions[region].get_case_obj(x,y)
        if tp_objet not in self.objets.keys():
            raise UserWarning("Erreur !")
        # S'il n'y a pas d'objets, on regardera les données de "rien"
        if self.objets[tp_objet]["collision"]: ## Si une case est occupée par un arbre ou autre,
            return False                                  ## alors le déplacement est impossible


        # on regarde les persos
        for p in self.server.personnages.values():
            if p.position["x"]==x and p.position["y"]==y:
                return False

        # on regarde les monstres
        monstre = self.regions[region].get_case(x,y)
        if monstre != None:
            if monstre.etat == "vivant":
                return False

        # ca devrait être bon la
        return True

    def get_infos_monstres(self):
        infos = {}
        for id_spawn, monstre in self.ennemis.items():
            infos[id_spawn] = {
                "id_monstre": monstre.id_monstre,
                "vie": monstre.pv,
                "position": monstre.position
            }
        return infos

    def load(self):
        # on récupère les id des régions
        sql = "SELECT id_region,nom FROM regions";
        regs = self.server.db.requete_db(sql)
        for r in regs:
            self.regions[r[0]]=Region(self, self.server, r[0], r[1])
        # on récupère les terrains (les données, pas chaque cases)
        sql = "SELECT id_terrain, nom, peut_marcher, cultivable, objet_dessus FROM terrain"
        ters = self.server.db.requete_db(sql)
        for t in ters:
            self.terrains[t[0]] = {
                "nom": t[1],
                "peut_marcher": bool(t[2]),
                "cultivable": bool(t[3]),
                "objet_dessus": bool(t[4])
            }
        # on récupère les données des objets
        sql = "SELECT id_objet, nom, collision FROM objets"
        objs = self.server.db.requete_db(sql)
        for o in objs:
            self.objets[o[0]] = {
                "nom": o[1],
                "collision": bool(o[2])
            }
        # On va juste avoir besoin d'avoir une correspondance
        # entre id_spaw_monstre et id_monstre
        sql = "SELECT id_mosntre_spawn,id_monstre FROM regions_monstres"
        res = self.server.db.requete_db(sql)
        for r in res:
            self.type_monstres_spawns[r[0]] = r[1]
