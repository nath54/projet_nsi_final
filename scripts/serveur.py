
from websocket_serveur import ServeurWebsocket
from carte import Carte

class Serveur:
    def __init__(self):
        # TODO : init du serveur
        self.serveurWebsocket = ServeurWebsocket(self)
        self.db = None # On voudrait un accès à la base de donnée
        self.carte = None
        self.personnages = {} # dictionnaire : key : l'id du compte utilisateur, value : l'instance de la classe perso reliée à l'utilisateur

    def start(self):
        # TODO : lancer le serveur

        # Maintenant, on peut gerer les websockets
        self.serveurWebsocket.start()
        # TODO : lancer la db
        self.carte = Carte(self.db)


    def load_perso(self, id_utilisateur):
        pass

    def bouger_perso(self, id_utilisateur, deplacement):
        self.personnages[id_utilisateur].bouger(deplacement)



if __name__=='__main__':
    # On lance le serveur ici
    server = Serveur()
    server.start()
