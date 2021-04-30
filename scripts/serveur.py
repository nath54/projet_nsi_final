#!bin/python3
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

    def send_to_user(self, id_utilisateur, message):
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
        for id_ws, data in self.serveurWebsocket.USERS.items():
            if data["id_utilisateur"] == id_utilisateur:
                ws_u = self.serveurWebsocket.get_ws(id_ws)
                break
        if ws_u is None:
            raise UserWarning("L'ID de l'utilisateur n'est pas dans data")
        self.serveurWebsocket.send(ws_u, message)

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
        # on envoie a tout le monde les infos du joueur
        infos = {"action": "joueur",
                 "id_perso": id_utilisateur,
                 "nom": perso.nom,
                 "x": perso.position["x"],
                 "y": perso.position["y"],
                 "vie": perso.vie,
                 "vie_max": perso.vie_max,
                 "mana": perso.mana,
                 "mana_max": perso.mana_max,
                 "xp": perso.xp,
                 "xp_tot": perso.xp_tot,
                 "region_actu": perso.region_actu}
        print(id_utilisateur)
        self.serveurWebsocket.send_all(infos, [id_utilisateur])
        ws_base = self.serveurWebsocket.wsFromId(id_utilisateur)
        #on va récuperer toutes les infos des autres joueurs
        for ws_id, data in self.serveurWebsocket.USERS.items():
            if id_utilisateur != data["id_utilisateur"]:
                print("aaaa", id_utilisateur, data["id_utilisateur"])
                id_perso = data["id_utilisateur"]
                p = self.personnages[id_perso]
                infos = {"action": "joueur",
                         "id_perso": id_perso,
                         "nom": p.nom,
                         "x": p.position["x"],
                         "y": p.position["y"],
                         "vie": p.vie,
                         "vie_max": p.vie_max,
                         "mana": p.mana,
                         "mana_max": p.mana_max,
                         "xp": p.xp,
                         "xp_tot": p.xp_tot,
                         "region_actu": p.region_actu}
                self.serveurWebsocket.send(ws_base, infos)


    def bouger_perso(self, id_utilisateur, deplacement):
        self.personnages[id_utilisateur].bouger(deplacement)


if __name__ == '__main__':
    # On lance le serveur ici
    server = Serveur()
    server.start()
