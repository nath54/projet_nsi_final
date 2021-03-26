
from websocket_serveur import ServeurWebsocket
from carte import Carte
from dbclient import dbClient
from personnage import Personnage

class Serveur:
    def __init__(self):
        # TODO : init du serveur
        self.serveurWebsocket = ServeurWebsocket(self)
        self.db = dbClient() # On voudrait un accès à la base de donnée
        self.carte = Carte(self)
        self.personnages = {} # dictionnaire : key : l'id du compte utilisateur, value : l'instance de la classe perso reliée à l'utilisateur

    def start(self):
        # TODO : lancer les autres elements serveur

        # Maintenant, on peut gerer les websockets
        self.serveurWebsocket.start()

    ############### WEBSOCKET ###############

    def send_to_user(self, id_utilisateur, message):
        ws_u = None
        for ws, id_u in self.serveurWebsocket.USERS.items():
            if id_u == id_utilisateur:
                ws_u = ws
                break
        if ws_u is None:
            raise UserWarning("ERREUR !")
        self.serveurWebsocket.send(ws_u, message)


    ###############  PERSONNAGES ###############

    def load_perso(self, id_utilisateur):
        print("LOAD PERSO ", id_utilisateur)
        res = self.db.requete_db("SELECT * FROM utilisateurs WHERE id=?", (id_utilisateur,))
        print(res)
        perso = Personnage(self, id_utilisateur)
        self.personnages[id_utilisateur] = perso

    def bouger_perso(self, id_utilisateur, deplacement):
        self.personnages[id_utilisateur].bouger(deplacement)



if __name__=='__main__':
    # On lance le serveur ici
    server = Serveur()
    server.start()
