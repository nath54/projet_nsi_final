# region Imports :

import json

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
# endregion


class Quete:
    """Classe des quêtes

    Attributes:
        id(int):
            Identifiant de la quête dans la base de données
        nom(str):
            Nom de la quête
        description(str):
            Description de la quête
        condition(dict<str: str|list<int>>):
            Condition pour commencer la quête ; voir `quete.md` pour le format
        objectif(dict<str: TODO: Trouver format objectif>):
            Objectif de la quête ; voir `quete.md` pour le format
        recompense(dict<str: int|list<[int, int]>>)
            Récompense de la quête ; voir `quete.md` pour le format
    """
    def __init__(self, id, db):
        self.id = id
        self.load_quete(id, db)
        pass

    def load_quete(self, id, db):
        """Charge la quête depuis la base de données

        Parameters:
            id(int): ID de la quête dans la base de données
            db(DB): Instance de la base de données

        TODO: Ajuster les noms avec ceux de la base de données

        """
        curseur = db.cursor()
        sql = """SELECT nom, description_, condition_, objectif, recompense
                 FROM quete
                 WHERE id = """ + id
        curseur.execute(sql)
        res = [ligne for ligne in curseur]

        self.nom = res[0]
        self.description = res[1]
        self.condition = json.loads(res[2])
        self.objectif = json.loads(res[3])
        self.recompense = json.loads(res[4])
