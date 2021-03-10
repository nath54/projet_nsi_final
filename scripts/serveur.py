
from websocket_serveur import ServeurWebsocket


class Serveur:
    def __init__(self):
        # TODO : init du serveur

        self.serveurWebsocket = ServeurWebsocket()

    def start(self):
        # TODO : lancer le serveur

        # Maintenant, on peut gerer les websockets
        self.serveurWebsocket.start()


if __name__=='__main__':
    # On lance le serveur ici
    server = Serveur()
    server.start()
