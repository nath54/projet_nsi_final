import asyncio

import websockets as ws
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
        self.server = server
        self.DEBUG = True

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

    async def register(self, websocket):
        """Enregistre un client websocket lorsqu'il se connecte

        Arguments:
            websocket(websocket)
                Client websocket à enregistrer

        Author : Nathan

        """
        self.debug("Client connected !", websocket)
        self.USERS[websocket] = {"id_utilisateur": None}
        """On stocke des infos relatives au client websocket ici"""

    async def unregister(self, websocket):
        """Enlève un client websocket lorsqu'il se déconnecte

        Arguments:
            websocket (websocket)
                Client websocket à déconnecter

        Author : Nathan
        """
        self.debug("Client disconnected !", websocket)
        del(self.USERS[websocket])  # On enlève l'utilisateur

    # \=~=~=~=~=~=~=~=~=~=~= INTERACTION CLIENT/SERVEUR =~=~=~=~=~=~=~=~=~=~=/

    def wsFromId(self, id_):
        for ws, data in self.USERS.items():
            if id_ == data["id_utilisateur"]:
                return ws
        return None

    async def send(self, websocket, message):
        """Envoie un message au websocket

        S'utilise de la manière suivante :
            await self.send(websocket, {"exemple": "ex",\
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
        await websocket.send(message)  # On envoie le message

    async def send_all(self, message, excepts_ids=[]):
        """Envoie un message à tous les clients

        Arguments:
            message(dict|str)
                Message à envoyer
                dict -> Objet json à envoyer
                str  -> Message à envoyer
            excepts_ids(list<int>)
                ID des utilisateurs auquel on enverra pas le messages
        """
        for ws, data in self.USERS.items():
            if data["id_utilisateur"] not in excepts_ids:
                await self.send(ws, message)

    async def handle_server(self, websocket, _):
        """Gère et reçoit tous les messages d'un client websocket

        Arguments:
            websocket (websocket)
                Client websocket dont on gère les messages

        Author : Nathan
        """
        await self.register(websocket)  # On enregistre l'utilisateur
        try:
            # on traite tous les messages que l'on recoit
            async for message in websocket:
                await self.gere_messages(websocket, message)
        finally:
            id_perso = self.USERS[websocket]["id_utilisateur"]
            p = self.server.personnages[id_perso]
            # on va enregistrer sa derniere position dans la bdd
            self.server.db.action_db("UPDATE utilisateurs SET position_x = ?, position_y = ? WHERE id_utilisateur = ?;", ( p.position["x"], p.position["y"], id_perso))
            #
            del self.server.personnages[id_perso]
            mes_parti = {"action":"j_leave", "id_perso": id_perso}
            # On supprime l'utilisateur
            await self.unregister(websocket)
            # on dit a tt le monde que le joueur a quitté
            await self.send_all(mes_parti)

    async def send_infos_persos(self, websocket):
        """Envoie un dictionnaire contenant toutes les infos d'un perso

        Arguments:
            websocket(websocket)
                Client websocket auquel on envoie les infos

        Author: Nathan
        """
        p = self.server.personnages[self.USERS[websocket]["id_utilisateur"]]
        infos = {"action": "infos_perso",
                 "id_perso": p.id_utilisateur,
                 "pseudo": p.nom,
                 "x": p.position["x"],
                 "y": p.position["y"],
                 "vie": p.vie,
                 "vie_max": p.vie_max,
                 "mana": p.mana,
                 "mana_max": p.mana_max,
                 "xp": p.xp,
                 "xp_tot": p.xp_tot,
                 "region_actu": p.region_actu}
        await self.send(websocket, infos)

    async def gere_messages(self, websocket, message):
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
                id_utilisateur = data["id_utilisateur"]
                self.USERS[websocket]["id_utilisateur"] = id_utilisateur
                # await self.send(websocket, {"action": "debug", "message": f"id {id_utilisateur}"})
                # TODO: Renvoyer que la connexion s'est bien effectuée ou pas
                await self.server.load_perso(id_utilisateur)
                await self.send_infos_persos(websocket)
                # for i, p in self.server.personnages.items():
                #     if i == self.USERS[websocket]["id_utilisateur"]:
                #         continue
                #     if self.server.personnages[id_utilisateur].region_actu != p.region_actu:
                #         # Pas dans la même région : on n'envoie pas les données
                #         continue
                #     infos = {
                #         "action": "autre_joueur",
                #         "id_user": i,
                #         "region": p.region_actu,
                #         "x": p.position["x"],
                #         "y": p.position["y"]
                #     }
                #     await self.send(websocket, infos)

            elif data["action"] == "deplacement":  # Un autre exemple d'action
                # TODO : mettre des vérifs ici ou dans la fonction utilisée
                user = self.USERS[websocket]["id_utilisateur"]
                await self.server.bouger_perso(user, data["deplacement"])
            elif data["action"] == "stats_persos":  # Un autre exemple
                await self.send_infos_persos(websocket)
        else:
            # Il faudra faire attention aux types d'event
            print("Unsupported event : ", data)

    # \=~=~=~=~=~=~=~=~=~=~=~=~= START SERVER =~=~=~=~=~=~=~=~=~=~=~=~=/

    def start(self):
        """Lance le serveur websocket, à appeler dans le serveur.py.

        Author: Nathan
        """
        print("Server starting...")
        self.serveur = ws.serve(self.handle_server, self.IP, self.PORT)
        # On initialise le serveur

        print(f"Server listening on {self.IP}:{self.PORT}")
        asyncio.get_event_loop().run_until_complete(self.serveur)

        asyncio.get_event_loop().run_forever()
        # Le serveur tourne tant qu'on ne l'arrête pas
        # Utiliser Ctrl+C pour l'arrêter
