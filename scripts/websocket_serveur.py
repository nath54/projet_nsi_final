
import asyncio
import websockets as ws # pour ne pas le confondre
                        # avec les variables websocket que l'on utilisera
import json
import random
from datetime import datetime

class ServeurWebsocket:
    """
    Ceci est la classe websocket pour communiquer avec le client websocket javascript
    """

    ###################################### INITIALISATION ######################################

    def __init__(self):
        """Constructeur de la classe ServeurWebsocket
        """
        config = self.load_config("config.json") # Fichier de configuration
        self.IP = config["host_websocket"] # Ip/Information Réseau pour la connection websocket
        self.PORT = config["port_websocket"] # Port utilisée pour la connection websocket
        self.USERS = dict() # Dictionnaire des utilisateurs actuellement connectés au serveur websocket

        self.DEBUG = True # Permettra d'afficher des messages d'erreurs/de debuggage lors des tests
    
    def load_config(self, path):
        """Fonction pour récupérer la configuration du serveur enregistrée dans un fichier json 

        Args:
            path (str): chemin utilisé pour lire le fichier de configuration

        Returns:
            [dict]: Renvoie un dictionnaire contenant les infos du fichier de configuration
        """
        data = json.load(open(path, "r"))
        return data

    def debug(self, *message):
        """Affiche des messages quand on est en mode debug

        Args:
            *message (list): La liste des informations a afficher
        """
        if self.DEBUG:
            now = datetime.now().time() # time object
            print(now, ":", *message) # Affiche le message

    ############################# REGISTER / UNREGISTER CONNECTION #############################

    async def register(self,websocket):
        """Fonction qui va enregistrer un client websocket connecté

        Args:
            websocket (websocket): client websocket
        """
        self.debug("Client connected !", websocket)
        self.USERS[websocket] = dict() # On va pouvoir stocker des informations
                                       # relatives au client websocket ici

    async def unregister(self,websocket):
        """Fonction qui va enlever un client websocket qui se déconnecte

        Args:
            websocket (websocket): client websocket
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
        """
        message = json.dumps(message) # On convertit en json
        await websocket.send(message) # On envoie le message

    async def handle(self, websocket):
        """Fonction qui va gerer et recevoir tous les messaged d'un client websocket
           de sa connection à sa déconnection

        Args:
            websocket (websocket): client websocket
        """
        await self.register(websocket) # On enregistre l'utilisateur
        try:
            async for message in websocket: # on traite tous les messages que l'on recoit
                await self.gere_messages(websocket, data)
        finally:
            await self.unregister(websocket) # On supprime l'utilisateur
    
    async def gere_messages(self, websocket, data):
        """analyse tous les messages qu'elle recoit,
           et réagit en conséquence

        Args:
            websocket (websocket): client websocket
            data (str): message recu
        """
        data = json.loads(message)
        self.debug("get from ", websocket, " : ", data)
        if "action" in data.keys():
            if data["action"] == "connection": # un exemple d'action possible
                pass
            elif data["action"] == "deplacement": # un autre exemple d'action à gerer
                pass
        else:
            print("Unsupported event : ", data) # Il faudra faire attention aux types d'event

    ###################################### START SERVER ######################################

    def start(self):
        """Lance le serveur websocket,
           à appeler dans le serveur.py, 
        """
        print("Server starting...")
        self.serveur = ws.serve(self.handle, self.IP, self.PORT) # On initialise le serveur
        print(f"Server listening on {self.IP}:{self.PORT}")
        asyncio.get_event_loop().run_until_complete(self.serveur) 
        asyncio.get_event_loop().run_forever() # Le serveur tourne tant qu'on ne l'arrete pas
                                               # Un petit Ctrl+C fait très bien l'affaire ;)



