
class Region:
    def __init__(self, id, carte):
        self.id = id
        self.carte = carte
        self.cases_terrains = {} # key "x_y": type du terrain
                                 # comme ca, on y accede cases_terrains[f"{x}_{y}"] => le type de la case
        self.cases_objets = {}   # key "x_y": type de l'objet
                                 # comme ca, on y accede ca[f"{x}_{y}"] => le type de l'objet

    def get_case(self, x, y):
        pass

class Carte:
    def __init__(self, server):
        self.server = server
        self.db = server.db
        self.regions = {}
        self.terrains = {}

    def load(self):
        pass
