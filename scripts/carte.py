from monstres import Monstre
import json


class Region:
    def __init__(self, carte, server, id_region, nom):
        self.id_region = id_region
        self.carte = carte
        self.server = server
        self.cases_terrains = {}
        """
        key "x_y": type du terrain
        Comme ça, on y accède avec cases_terrains[f"{x}_{y}"] => type de case
        """
        self.cases_objets = {}
        """
        key "x_y": type de l'objet
        Comme ça, on y accède avec cases_objets[f"{x}_{y}"] => type de l'objet
        """
        self.cases_objets_parameters = {}
        """
        key "x_y": type de l'objet
        Comme ça, on y accède avec cases_objets[f"{x}_{y}"] => params d'objet
        """
        self.spawn_monstres = {}
        """
        key: id_monstre_spawn
        value : "x_y"
        """
        self.monstres_pos = {}
        """
        key: id_monstre_spawn
        value : "x_y"
        """
        self.ennemis = {}
        """
        key id_monstre_spawn
        value : Ennemi
        """

        self.pnjs = {}

        # On charge les terrains
        sql = "SELECT x, y, id_terrain FROM regions_terrains WHERE id_region=?"
        ters = self.server.db.requete_db(sql, (self.id_region, ))
        for t in ters:
            self.cases_terrains[str(t[0])+"_"+str(t[1])] = int(t[2])

        # on charge les objets
        sql = """SELECT x, y, id_objet, parametres
                 FROM regions_objets
                 WHERE id_region=?"""
        objs = self.server.db.requete_db(sql, (self.id_region, ))
        for t in objs:
            self.cases_objets[str(t[0]) + "_" + str(t[1])] = int(t[2])
            dico = json.loads(t[3].replace("'", '"'))
            self.cases_objets_parameters[str(t[0]) + "_" + str(t[1])] = dico

        # on charge les monstres
        sql = """SELECT id_monstre_spawn, x, y, id_monstre
                 FROM regions_monstres
                 WHERE id_region=?"""
        objs = self.server.db.requete_db(sql, (self.id_region,))
        for t in objs:
            self.spawn_monstres[int(t[0])] = str(t[1]) + "_" + str(t[2])

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
        if i in self.monstres_pos.values():
            for (monstre, case) in self.monstres_pos.items():
                if case == i:
                    return monstre
        else:
            return None

    def launch_monstres(self):
        # les pos sont de la forme "x_y"
        for id_monstre_spawn, pos in self.spawn_monstres.items():
            id_monstre = self.carte.type_monstres_spawns[id_monstre_spawn]
            lst = pos.split("_")
            position = {"x": int(lst[0]), "y": int(lst[1])}
            monstre = Monstre(self.server, id_monstre_spawn, id_monstre,
                              self.id_region, position)
            self.ennemis[id_monstre_spawn] = monstre


class Carte:
    """Gère toutes les régions, les collisions..."""
    def __init__(self, server):
        self.server = server
        self.db = server.db
        self.regions = {}
        self.terrains = {}
        self.objets = {}
        self.type_monstres_spawns = {}
        # self.load()

    def get_case_libre_plus_proche(self, id_region, x, y):
        pass

    def est_case_libre(self, id_region, x, y):
        if id_region not in self.regions.keys():
            raise UserWarning("Erreur ! Région inconnue")
        k = str(x) + "_" + str(y)

        # On regarde les terrains
        tp_case = self.regions[id_region].get_case(x, y)
        if tp_case not in self.terrains.keys():
            raise UserWarning("Erreur !")
        # Si une case est occupée par un arbre ou autre
        if not self.server.carte.terrains[tp_case]["peut_marcher"]:
            return False

        # on regarde les objets
        tp_objet = self.regions[id_region].get_case_obj(x, y)
        if tp_objet not in self.objets.keys():
            raise UserWarning("Erreur !")
        # S'il n'y a pas d'objets, on regardera les données de "rien"
        # Si une case est occupée par un arbre ou autre
        if self.objets[tp_objet]["collision"]:
            return False

        # on regarde les persos
        for p in self.server.personnages.values():
            if p.position["x"] == x and p.position["y"] == y:
                return False

        # on regarde les monstres
        monstre = self.regions[id_region].get_case_monstre(x, y)
        if monstre is not None:
            if monstre.etat == "vivant":
                return False

        # ca devrait être bon la
        return True

    # Fonction qui compte le nombre de joueurs dans une région
    def nb_players_in_region(self, id_region):
        compteur = 0
        for p in self.server.personnages.values():
            if p.region_actu == id_region:
                compteur += 1
        return compteur

    def get_infos_monstres(self, id_region):
        infos = {}  # id_region : ennemis
        for id_spawn, monstre in self.regions[id_region].ennemis.items():
            infos[id_spawn] = {
                "id_monstre_spawn": id_spawn,
                "id_monstre": monstre.id_monstre,
                "nom": monstre.nom,
                "vie": monstre.pv,
                "x": monstre.position["x"],
                "y": monstre.position["y"],
                "etat": monstre.etat
            }
        return infos

    def load(self):
        # on récupère les terrains (les données, pas chaque cases)
        sql = """SELECT id_terrain, nom, peut_marcher, cultivable, objet_dessus
                 FROM terrain"""
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
        # Entre id_spaw_monstre et id_monstre
        sql = "SELECT id_monstre_spawn,id_monstre FROM regions_monstres"
        res = self.server.db.requete_db(sql)
        for r in res:
            self.type_monstres_spawns[r[0]] = r[1]
        # on récupère les id des régions
        sql = "SELECT id_region,nom FROM regions"
        regs = self.server.db.requete_db(sql)
        for r in regs:
            self.regions[r[0]] = Region(self, self.server, r[0], r[1])
        # On lance les monstres
        for r in self.regions.values():
            r.launch_monstres()
