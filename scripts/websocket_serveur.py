
import wss as ws
# Pour ne pas le confondre avec les variables websocket que l'on utilisera

import json
import random
from datetime import datetime


class ServeurWebsocket:
    """Communique avec le client websocket javascript

    Attributes:
        IP(str)
            IP/Information réseau pour la connexion WebSocket
        PORT(int)
            Port utilisé pour la connexion websocket
        USERS(dict<WebSocket, int>)
            Utilisateurs actuellement connectés au serveur websocket
            Format {Instance WebSocket: ID de l'utilisateur}
        server(Serveur)
            Référence au serveur
        DEBUG(bool)
            True  -> Affiche des messages d'erreur pour le débuggage
            False -> Cache les messages d'erreur
    """

    # \=~=~=~=~=~=~=~=~=~=~=~=~= INITIALISATION =~=~=~=~=~=~=~=~=~=~=~=~=/

    def __init__(self, server):
        """Constructeur de la classe ServeurWebsocket

        Author : Nathan
        """
        config = self.load_config("../includes/config.json")
        """Fichier de configuration"""

        self.IP = config["host_websocket"]
        self.PORT = config["port_websocket"]
        self.USERS = dict()
        self.WEBSOCKETS = {}
        self.server = server
        self.DEBUG = True
        self.ws_server = None

    def load_config(self, path):
        """Récupère la config du serveur enregistrée dans un fichier json

        Arguments:
            path (str): chemin utilisé pour lire le fichier de configuration

        Returns:
            dict<str, str|int>
                Renvoie un dictionnaire contenant les infos du fichier
                de configuration

        Author : Nathan
        """
        data = json.load(open(path, "r"))
        return data

    def debug(self, *message):
        """Affiche des messages en mode débug

        Arguments:
            *message (list): La liste des informations à afficher

        Author : Nathan
        """
        if self.DEBUG:
            now = datetime.now().time()  # time object
            print(now, ":", *message)  # Affiche le message

    # \=~=~=~=~=~=~=~=~=~ REGISTER / UNREGISTER CONNECTION -=~=~=~=~=~=~=~=~=/

    def register(self, websocket):
        """Enregistre un client websocket lorsqu'il se connecte

        Arguments:
            websocket(websocket)
                Client websocket à enregistrer

        Author : Nathan

        """
        self.debug("Client connected !", websocket)
        self.USERS[websocket['id']] = {"id_utilisateur": None}
        self.WEBSOCKETS[websocket['id']] = websocket
        """On stocke des infos relatives au client websocket ici"""

    def unregister(self, websocket):
        """Enlève un client websocket lorsqu'il se déconnecte

        Arguments:
            websocket (websocket)
                Client websocket à déconnecter

        Author : Nathan
        """
        self.debug("Client disconnected !", websocket)
        del(self.USERS[websocket['id']])  # On enlève l'utilisateur
        del(self.WEBSOCKETS[websocket['id']])

    # \=~=~=~=~=~=~=~=~=~=~= INTERACTION CLIENT/SERVEUR =~=~=~=~=~=~=~=~=~=~=/

    def get_ws(self, id_ws):
        return self.WEBSOCKETS[id_ws]

    def wsFromId(self, id_):
        for ws_id, data in self.USERS.items():
            if id_ == data["id_utilisateur"]:
                return self.get_ws(ws_id)
        return None

    def send(self, websocket, message):
        """Envoie un message au websocket

        S'utilise de la manière suivante :
            self.send(websocket, {"exemple": "ex",\
                                        "encore_exemple": "ex"})

        Arguments:
            websocket(websocket)
                Client websocket auquel on envoie le message
            message (dict|str)
                Message à envoyer
                dict -> Objet json à envoyer
                str  -> Message à envoyer

        Author : Nathan
        """
        message = json.dumps(message)  # On convertit en json
        if self.DEBUG:
            self.debug("send to ", websocket, " message : ", message)
        self.ws_server.send_message(websocket, message)

    def send_all(self, message, excepts_ids=[]):
        """Envoie un message à tous les clients

        Arguments:
            message(dict|str)
                Message à envoyer
                dict -> Objet json à envoyer
                str  -> Message à envoyer
            excepts_ids(list<int>)
                ID des utilisateurs auquel on enverra pas le messages
        """
        for id_ws, data in self.USERS.items():
            if data["id_utilisateur"] not in excepts_ids:
                self.send(self.get_ws(id_ws), message)

    def send_infos_persos(self, websocket):
        """Envoie un dictionnaire contenant toutes les infos d'un perso

        Arguments:
            websocket(websocket)
                Client websocket auquel on envoie les infos

        Author: Nathan
        """
        p = self.server.personnages[self.USERS[websocket['id']]["id_utilisateur"]]
        infos = {"action": "infos_perso",
                 "id_perso": p.id_utilisateur,
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
        self.send(websocket, infos)

    def gere_messages(self, websocket, ws_server, message):
        """Analyse les messages reçus et effectue les actions sur le serveur.

        Arguments:
            websocket(websocket)
                Client websocket dont on reçoit le message.
            message (str):
                Message reçu sous forme json contenant les instructions.

        Author : Nathan
        """
        data = json.loads(message)
        self.debug("get from ", websocket, " : ", data)
        if "action" in data.keys():
            if data["action"] == "connection":  # Un exemple d'action possible
                id_utilisateur = int(data["id_utilisateur"])
                for _, donnees in self.USERS.items():
                    if id_utilisateur == donnees["id_utilisateur"]:
                        self.send(websocket, {"action":"prob_connection", "message":"qqun a déjà le meme id connecté"})
                        raise UserWarning("Probleme de connection, faudra trouver une facon plus 'propre' de quitter cette connexion")
                self.USERS[websocket['id']]["id_utilisateur"] = id_utilisateur
                # self.send(websocket, {"action": "debug", "message": f"id {id_utilisateur}"})
                self.server.load_perso(id_utilisateur)
                self.send_infos_persos(websocket)
                #
                infos = self.server.carte.get_infos_monstres(self.server.personnages[id_utilisateur].region_actu)
                self.send(websocket, {"action":"infos_monstres", "infos":infos})
            elif data["action"] == "deplacement":  # Un autre exemple d'action
                # TODO : mettre des vérifs ici ou dans la fonction utilisée
                user = self.USERS[websocket['id']]["id_utilisateur"]
                self.server.bouger_perso(user, data["deplacement"])
            elif data["action"] == "stats_persos":  # Un autre exemple
                self.send_infos_persos(websocket)
        else:
            # Il faudra faire attention aux types d'event
            print("Unsupported event : ", data)

    def nouveau_client(self, websocket, ws_server):
        self.register(websocket)

    def client_part(self, websocket, ws_server):
        print("Client(%d) disconnected" % websocket['id'])
        id_perso = self.USERS[websocket['id']]["id_utilisateur"]
        if id_perso is not None:
            p = self.server.personnages[id_perso]
            # On vérifie si un monstre l'avait détecté
            for monstre in self.server.carte.regions[p.region_actu].ennemis.values():
                if monstre.joueur_detecte == p:
                    monstre.joueur_detecte = None
            # on va enregistrer sa derniere position dans la bdd
            self.server.db.action_db("UPDATE utilisateurs SET position_x = ?, position_y = ? WHERE id_utilisateur = ?;", ( p.position["x"], p.position["y"], id_perso))
            #
            del self.server.personnages[id_perso]
            mes_parti = {"action":"j_leave", "id_perso": id_perso}
            # On supprime l'utilisateur
            self.unregister(websocket)
            # on dit a tt le monde que le joueur a quitté
            self.send_all(mes_parti)

    # \=~=~=~=~=~=~=~=~=~=~=~=~= START SERVER =~=~=~=~=~=~=~=~=~=~=~=~=/

    def start(self):
        """Lance le serveur websocket, à appeler dans le serveur.py.

        Author: Nathan
        """
        print("Server starting...")
        print(f"aaaaaaaa '{self.IP}'")

        self.ws_server = ws.WebsocketServer(self.PORT, host=self.IP)
        self.ws_server.set_fn_new_client(self.nouveau_client)
        self.ws_server.set_fn_client_left(self.client_part)
        self.ws_server.set_fn_message_received(self.gere_messages)
        # On initialise le serveur

        print(f"Server listening on {self.IP}:{self.PORT}")
        self.ws_server.run_forever()
        # Le serveur tourne tant qu'on ne l'arrête pas
        # Utiliser Ctrl+C pour l'arrêter
