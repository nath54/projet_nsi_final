
import json
import sys
# Méthode 1 : mariadb
try:
    import mariadb  # ignore unresolved-import error
except Exception as e:
    # Méthode 2 : mysql
    try:
        import mysql.connector as mariadb  # ignore unresolved-import error
    except Exception as e:
        # Rien n'est installé
        raise UserWarning("Il faut installer la librairie mariadb ou mysql !")

# Serveur principal
class dbClient:

    # region init

    def __init__(self):
        # on récupere les infos
        with open('../includes/config.json') as json_file:
            data = json.load(json_file)
            self.db_ip = data["ip"]
            self.db_port = data["port"]
            self.db_pseudo = data["user"]
            self.db_password = data["password"]
            self.db_database = data["database"]
        self.USERS = dict() # un dictionnaire contenant tous les clients connectés
        # base de donnée
        try: # on va essayer de se connecter
            self.connection = mariadb.connect(
                user = self.db_pseudo,
                password = self.db_password,
                host = self.db_ip,
                port = self.db_port,
                database = self.db_database)
            print("connecté a la database")
        except mariadb.Error as e:
            print(f"Erreur lors de la connection à la plateforme MariaDB : {e}")
            sys.exit(1)
        self.cursor = self.connection.cursor()

    # endregion

    ################### Fonctions de base pour gérer la base de donnée ###################

    # region actions / requetes

    # effectue une requette et renvoie le resultat (ex: SELECT ...)
    def requete_db(self, requete, args = tuple(), debug = False):
        if debug:
            nba = 0
            for l in requete:
                if l == "?":
                    nba += 1
            print(f"DB DEBUG :\n - requete : {requete}\n - arguments : {args}\n - Nombre d'arguments requis : {nba}")
        self.cursor.execute(requete, args)
        data = []
        for res in self.cursor:
            data.append(res)
        return data

    # effectue une action dans la base de donnée (ex : INSERT ...)
    def action_db(self, requete, args = tuple()):
        self.cursor.execute(requete, args)
        self.connection.commit()

    # endregion

