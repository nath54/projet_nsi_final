
import asyncio

import websockets as ws
# Pour ne pas le confondre avec les variables websocket que l'on utilisera

import json
import random
from datetime import datetime


class ServeurWebsocket:
    """
    Ceci est la classe websocket pour communiquer avec le client websocket javascript
    """

    ###################################### INITIALISATION ######################################

    def __init__(self, server):
        """Constructeur de la classe ServeurWebsocket

        Author : Nathan
        """
        config = self.load_config("config.json")  # Fichier de configuration
        self.IP = config["host_websocket"]  # Ip/Information Réseau pour la connexion websocket
        self.PORT = config["port_websocket"]  # Port utilisée pour la connexion websocket
        self.USERS = dict()  # Dictionnaire des utilisateurs actuellement connectés au serveur websocket
                             # websocket : id_utilisateur
        self.server = server
        self.DEBUG = True  # Permettra d'afficher des messages d'erreurs/de débuggage lors des tests

    def load_config(self, path):
        """Récupère la config du serveur enregistrée dans un fichier json

        Args:
            path (str): chemin utilisé pour lire le fichier de configuration

        Returns:
            dict<???, ???>: Renvoie un dictionnaire contenant les infos du fichier de configuration

        Author : Nathan
        """
        data = json.load(open(path, "r"))
        return data

    def debug(self, *message):
        """Affiche des messages quand on est en mode debug

        Args:
            *message (list): La liste des informations a afficher

        Author : Nathan
        """
        if self.DEBUG:
            now = datetime.now().time() # time object
            print(now, ":", *message) # Affiche le message

    ############################# REGISTER / UNREGISTER CONNECTION #############################

    async def register(self, websocket):
        """Fonction qui va enregistrer un client websocket connecté

        Args:
            websocket (websocket): client websocket

        Author : Nathan

        """
        self.debug("Client connected !", websocket)
        self.USERS[websocket] = {"id_utilisateur": None} # On va pouvoir stocker des informations
                                       # relatives au client websocket ici

    async def unregister(self,websocket):
        """Fonction qui va enlever un client websocket qui se déconnecte

        Args:
            websocket (websocket): client websocket

        Author : Nathan
        """
        self.debug("Client disconnected !", websocket)
        del(self.USERS[websocket]) # On enleve l'utilisateur


    ################################ INTERACTION CLIENT/SERVEUR ################################

    async def send(self, websocket, message):
        """fonction qui envoie un message au websocket
           `message` peut être sous format parsable par json

           S'utilise de la manière suivante :
            await self.send(websocket, {"exemple", "ex", "encore_exemple", "ex"})

        Args:
            websocket (websocket): client websocket
            message (dict/str): message à envoyer

        Author : Nathan
        """
        message = json.dumps(message)  # On convertit en json
        await websocket.send(message)  # On envoie le message

    async def handle_server(self, websocket, _):
        """Fonction qui va gerer et recevoir tous les messaged d'un client websocket
           de sa connection à sa déconnection

        Args:
            websocket (websocket): client websocket

        Author : Nathan
        """
        await self.register(websocket) # On enregistre l'utilisateur
        try:
            async for message in websocket: # on traite tous les messages que l'on recoit
                await self.gere_messages(websocket, message)
        finally:
            await self.unregister(websocket) # On supprime l'utilisateur

    async def gere_messages(self, websocket, message):
        """analyse tous les messages qu'elle recoit,
           et réagit en conséquence

        Args:
            websocket (websocket): client websocket
            message (str): message recu

        Author : Nathan
        """
        data = json.loads(message)
        self.debug("get from ", websocket, " : ", data)
        if "action" in data.keys():
            if data["action"] == "connection":  # un exemple d'action possible
                id_utilisateur = data["id_utilisateur"]
                # TODO: renvoyer que la connection s'est bien effectuée ou pas
                self.server.load_perso(id_utilisateur)
            elif data["action"] == "deplacement":  # un autre exemple d'action à gerer
                # TODO: mettre des vérifs ici, ou dans la fonction qu'on appelle
                self.server.bouger_perso(self.USERS[websocket]["id_utilisateur"], data["deplacement"])
            elif data["action"] == "stats_persos":  # un autre exemple d'action à gerer
                p = self.server.personnages[self.USERS[websocket]["id_utilisateur"]]
                infos = {"action": "infos_persos",
                         "x": p.x,
                         "y": p.y,
                         "vie": p.vie,
                         "vie_max": p.vie_tot,
                         "mana": p.mana,
                         "mana_max": p.mana_tot,
                         "xp": p.xp,
                         "xp_tot": p.xp_tot,
                         "region_actu": p.region_actu}
                self.send(websocket, infos)
        else:
            print("Unsupported event : ", data)  # Il faudra faire attention aux types d'event

    ###################################### START SERVER ######################################

    def start(self):
        """Lance le serveur websocket, à appeler dans le serveur.py,

        Author : Nathan

        """
        print("Server starting...")
        self.serveur = ws.serve(self.handle_server, self.IP, self.PORT)  # On initialise le serveur
        print(f"Server listening on {self.IP}:{self.PORT}")
        asyncio.get_event_loop().run_until_complete(self.serveur)
        asyncio.get_event_loop().run_forever()  # Le serveur tourne tant qu'on ne l'arrête pas
        # Un petit Ctrl+C fait très bien l'affaire ;)
