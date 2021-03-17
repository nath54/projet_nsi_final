
class personnage : 
    def __init__(self, nom, classe, sexe):
        self.nom = str(nom)
        self.sexe = str(sexe)
        self.classe = str(classe)
        self.position_x = 0 ## Position initiale du perso en x
        self.position_y = 0 ## Position initiale du perso en y
        self.sprite_fixe = "penser me transmettre un sprite pour le perso quand il bouge pas"
        self.sprite_droite = "penser me transmettre un sprite pour le perso quand il va a droite"
        self.sprite_gauche = "penser me transmettre un sprite pour le perso quand il va a gauche"
        self.sprite_haut = "penser me transmettre un sprite pour le perso quand il va en haut"
        self.sprite_bas = "penser me transmettre un sprite pour le perso quand il va en bas"
        self.vie = 20
        self.niveau = 0  
        self.xp = 0
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

    def interagir(self):
        pass

    def level_up(self):
        if self.xp == self.xp + 100 :
            self.niveau = self.niveau + 1

    def new_position(self):
        pass

    def perdre_vie(self, dgt_monstre):
        pass

    def gagner_vie(self):
        pass

def test():
    print("début des tests")
    pass


    

