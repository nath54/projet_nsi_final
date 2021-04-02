
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

    async def send_to_user(self, id_utilisateur, message):
        ws_u = None
        print(id_utilisateur, self.serveurWebsocket.USERS.items())
        for ws, data in self.serveurWebsocket.USERS.items():
            if data["id_utilisateur"] == id_utilisateur:
                ws_u = ws
                break
        if ws_u is None:
            raise UserWarning("ERREUR !")
        await self.serveurWebsocket.send(ws_u, message)

    ###############  PERSONNAGES ###############

    def load_perso(self, id_utilisateur):
        # res = self.db.requete_db("SELECT * FROM utilisateurs WHERE id_utilisateur=?", (id_utilisateur,))
        perso = Personnage(self, id_utilisateur)
        self.personnages[id_utilisateur] = perso

    async def bouger_perso(self, id_utilisateur, deplacement):
        await self.personnages[id_utilisateur].bouger(deplacement)

    ###############  MONSTRE ###############

    def load_monstre(self, id_monstre):
        # res = self.db.requete_db("SELECT * FROM monstre WHERE id_monstre=?", (id_monstre,))
        monstre = Monstre(self, id_monstre)
        self.monstres[id_monstre] = monstre

if __name__=='__main__':
    # On lance le serveur ici
    server = Serveur()
    server.start()
