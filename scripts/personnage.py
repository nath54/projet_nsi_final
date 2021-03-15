##Lancelot

class personnage : 
    def __init__(self, nom, classe):
        self.nom = nom
        self.taille_sprite = 
        self.sprite_fixe = "penser me transmettre un sprite pour le perso quand il bouge pas"
        self.sprite_droite = "penser me transmettre un sprite pour le perso quand il va a droite"
        self.sprite_gauche = "penser me transmettre un sprite pour le perso quand il va a gauche"
        self.sprite_haut = "penser me transmettre un sprite pour le perso quand il va en haut"
        self.sprite_bas = "penser me transmettre un sprite pour le perso quand il va en bas"
        self.classe = classe
        self.vie = 20
        self.niveau = 0 
        self.stamina = 20
        self.mana = 20
        self.armor = 0 

    def afficher(self):
        pass

    def bouger(self, deplacement ): #déplacement sous la forme de tuples (dep x, dep y)
        pass

    def prendre_objet(self):
        pass

    def attaquer(self):
        pass

    def selectionner(self):
        pass

    def level_up(self):
        pass

def test():
    print("début des tests")
    pass


    

