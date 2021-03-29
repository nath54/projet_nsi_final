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


class Objet:
    """Classe d'objet disponible dans l'inventaire

    Attributes:
        id(int):
            Identifiant de l'objet dans la base de données.
        nom(str):
            Nom de l'objet, visible depuis l'inventaire.
        description(str):
            Description de l'objet, visible depuis l'inventaire.
        image(str):
            Nom de l'image représentant l'objet.
        effet(dict<str: int|(str)>):
            Effet de l'objet. Se référer à `/Structure_Base_donnees.md` pour la
            syntaxe.
    """
    def __init__(self, id_, db):
        self.id_ = id_
        self.load_objet(id_, db)
        pass

    def load_objet(self, id_, db):
        """Charge l'objet depuis la base de données

        Parameters:
            id(int): ID de l'objet dans la base de données
            db(DB): Instance de la base de données

        TODO: Ajuster les noms avec ceux de la base de données

        """
        curseur = db.cursor()
        sql = """SELECT nom_objet, description_, image_, effet
                 FROM objet
                 WHERE id_objet = """ + id_
        curseur.execute(sql)
        res = [ligne for ligne in curseur]

        self.nom = res[0]
        self.description = res[1]
        self.image = res[2]
        self.effet = json.loads(res[3])
