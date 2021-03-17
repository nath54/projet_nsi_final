class Quete:
    def __init__(self, id):
        """Initialise une quête.

        Parameters:
            nom (str): Nom de la quête
            description (str): Description de la quête
            condition (dict {str: str|int}):
                {
                    "classe": "|nom_classe|",
                    "niveau": |niveau|,
                    "quete": [id_quete_1, id_quete_2, ...]
                }
            objectif (dict {}):
                {
                    TODO
                }
            recompense (dict {str: int|list((int, int))}):
            {
                "Argent", |nb_argent|
                "XP", |nb_point_exp|,
                "Objet", [(id_obj_1, qt), (id_obj_2, qt), ...]
            }
        """
        self.id = id
        load_quete(id)
        pass

    def load_quete(self, id):
        """Charge la quête depuis la base de données

        Parameters:
            
        """
        self.condition = condition
        self.objectif = objectif
        self.recompense = recompense
