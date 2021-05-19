#!/usr/bin/python3
from websocket_serveur import ServeurWebsocket
from carte import Carte
from dbclient import dbClient
from personnage import Personnage
from gere_ennemis import gere_ennemis
from console_debug import console
from _thread import start_new_thread as start_nt

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
    def __init__(self, debug=False, act_console=False):
        # TODO : init du serveur
        self.serveurWebsocket = ServeurWebsocket(self, debug)
        self.db = dbClient()  # Pour avoir un accès à la base de donnée
        self.carte = Carte(self)
        self.carte.load()
        self.personnages = {} # clé : id_utilisateur, value : Personnage()
        self.running = False
        self.debug = debug
        self.active_console = act_console
        self.t_console = None
        self.t_gere_ennemis = None
        #
        self.nb_t_actifs = 0
        #
        self.data_competences = {}
        self.load_competences()

    def start(self):
        """Lance le serveur et tous les éléments utiles"""
        # TODO : lancer les autres éléments serveur
        self.running = True

        # On lance le script qui gere les ennemis
        self.t_gere_ennemis = start_nt(gere_ennemis, (self,))
        print(f"Thread gere ennemis : {self.t_gere_ennemis}")

        # On lance la console de dev
        if self.active_console:
            self.t_console = start_nt(console, (self,))

        # Maintenant, on peut gérer les websockets
        self.serveurWebsocket.start()

    def exit(self):
        # On pourrait sauvegarder des données
        #TODO
        self.running = False
        # On attends que les autres thread finissent
        while self.nb_t_actifs > 1:
            pass
        # On quitte le thread websocket
        self.serveurWebsocket.finish()


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
        # print(id_utilisateur, self.serveurWebsocket.USERS.items())
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
                 "region_actu": perso.region_actu,
                 "id_tete": perso.id_tete,
                 "id_cheveux": perso.id_cheveux,
                 "id_barbe": perso.id_barbe,
                 "id_haut": perso.id_haut,
                 "id_bas": perso.id_bas,
                 "id_pied": perso.id_pied}
        self.serveurWebsocket.send_all(infos, [id_utilisateur])
        ws_base = self.serveurWebsocket.wsFromId(id_utilisateur)
        #on va récuperer toutes les infos des autres joueurs
        for ws_id, data in self.serveurWebsocket.USERS.items():
            if id_utilisateur != data["id_utilisateur"]:
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
                         "region_actu": p.region_actu,
                         "id_tete": p.id_tete,
                         "id_cheveux": p.id_cheveux,
                         "id_barbe": p.id_barbe,
                         "id_haut": p.id_haut,
                         "id_bas": p.id_bas,
                         "id_pied": p.id_pied}
                self.serveurWebsocket.send(ws_base, infos)


    def bouger_perso(self, id_utilisateur, deplacement, cooldown=False):
        self.personnages[id_utilisateur].bouger(deplacement, cooldown)


    def load_competences(self):
        req = "SELECT id_competence, nom, description_, type_cible, cout_mana, tp_recharge FROM competences;"
        res = self.db.requete_db(req)
        for data in res:
            self.data_competences[data[0]] = {
                "id_competence": data[0],
                "nom": data[1],
                "description": data[2],
                "type_cible": data[3],
                "cout_mana": data[4],
                "tp_recharge": data[5]
            }


if __name__ == '__main__':
    import sys
    debug = "-d" in sys.argv or "--debug" in sys.argv
    act_console = "-c" in sys.argv or "--console" in sys.argv
    # On lance le serveur ici
    server = Serveur(debug, act_console)
    server.start()
