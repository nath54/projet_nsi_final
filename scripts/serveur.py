from websocket_serveur import ServeurWebsocket
from carte import Carte
from dbclient import dbClient
from personnage import Personnage


class Serveur:
    """Serveur du jeu

    Attributes:
        serveurWebsocket(ServeurWebsocket)
            Instance du serveur Websocket utilisé
        db(dbClient)
            Instance de la BDD
        carte(Carte)
            Instance de la carte du jeu (des différentes régions)
        personnages(dict<int, Personnage>)
            Dictionnaire stockant des infos sur les personnages:
                key   -> ID du compte de l'utilisateur
                value -> Instance de la classe perso reliée à l'utilisateur
    """
    def __init__(self):
        # TODO : init du serveur
        self.serveurWebsocket = ServeurWebsocket(self)
        self.db = dbClient()  # On voudrait un accès à la base de donnée
        self.carte = Carte(self)
        self.personnages = {}

    def start(self):
        """Lance le serveur et tous les éléments utiles"""
        # TODO : lancer les autres éléments serveur

        # Maintenant, on peut gérer les websockets
        self.serveurWebsocket.start()

    # \=~=~=~=~=~=~=~=~= WEBSOCKET =~=~=~=~=~=~=~=~=/

    async def send_to_user(self, id_utilisateur, message):
        """Envoie un message à un utilisateur avec son id

        Arguments:
            id_utilisateur(int)
                ID de l'utilisateur cible du message
            message(str|dict)
                Message à envoyer
                dict -> Objet JSON du message
                str  -> Message à envoyer

        Raise:
            UserWarning
                Si data['id_utilisateur'] ne contient pas id_utilisateur
        """
        ws_u = None
        print(id_utilisateur, self.serveurWebsocket.USERS.items())
        for ws, data in self.serveurWebsocket.USERS.items():
            if data["id_utilisateur"] == id_utilisateur:
                ws_u = ws
                break
        if ws_u is None:
            raise UserWarning("L'ID de l'utilisateur n'est pas dans data")
        await self.serveurWebsocket.send(ws_u, message)

    # \=~=~=~=~=~=~=~=~=  PERSONNAGES =~=~=~=~=~=~=~=~=/

    def load_perso(self, id_utilisateur):
        """Charge un personnage et l'associe dans self.personnages"""
        """
        res = self.db.requete_db(\"""SELECT * FROM utilisateurs\
                                    WHERE id_utilisateur=?\""",\
                                    (id_utilisateur,))
        """
        perso = Personnage(self, id_utilisateur)
        self.personnages[id_utilisateur] = perso

    async def bouger_perso(self, id_utilisateur, deplacement):
        await self.personnages[id_utilisateur].bouger(deplacement)

    # \=~=~=~=~=~=~=~=~= MONSTRE =~=~=~=~=~=~=~=~=/

    """
    def load_monstre(self, id_monstre):
        res = self.db.requete_db("SELECT * FROM monstre WHERE id_monstre=?",\
                (id_monstre,))
        monstre = Monstre(self, id_monstre)
        self.monstres[id_monstre] = monstre
    """


if __name__ == '__main__':
    # On lance le serveur ici
    server = Serveur()
    server.start()
