
class personnage : 
    def __init__(self, nom, classe, sexe):
        self.nom = nom
        self.sexe = sexe
        self.classe = classe
        self.position = {"x": 0, "y": 0}
        self.sprite_fixe = "penser me transmettre un sprite pour le perso quand il bouge pas"
        self.sprite_droite = "penser me transmettre un sprite pour le perso quand il va a droite"
        self.sprite_gauche = "penser me transmettre un sprite pour le perso quand il va a gauche"
        self.sprite_haut = "penser me transmettre un sprite pour le perso quand il va en haut"
        self.sprite_bas = "penser me transmettre un sprite pour le perso quand il va en bas"
        self.vie = 20
        self.max_vie = 20
        self.niveau = 0  
        self.xp = 0
        self.stamina = 20
        self.mana = 20 
        self.mana_max = 20
        self.armor = 0 

    def afficher(self):
        self.sprite_fixe
        

    def bouger(self, touche): #déplacement sous la forme de dict (dep x, dep y)
        if touche == "up":
            self.position["y"] = self.position["y"] + 1
        elif touche == "right":
            self.position["x"] = self.position["x"] + 1
        elif touche == "left" :
            self.position["x"] = self.position["x"] - 1
        elif touche == "down":
            self.position["y"] = self.position["y"] - 1
        
    def emplacement(self):
        self.position

    def prendre_objet(self, touche):
        if touche == "e" or touche =="E":

            pass

    def attaquer(self, touche):
        pass

    def interagir(self, touche):
        if touche == "e" or touche == "E":
            pass

    def gagner_xp(self, xp):
        pass

    def level_up(self):
        if self.xp == self.xp + 100 :
            self.niveau = self.niveau + 1

    def perdre_vie(self, dgt_monstre):
        pass

    def gagner_vie(self):
        pass

def test():
    print("début des tests")
    p = personnage("Lance", "mage", "homme")

    p.bouger("up")
    assert p.position == {"x": 0, "y": 1}
    p.bouger("left")
    assert p.position == {"x": -1, "y": 1}
    p.bouger("right")
    assert p.position == {"x": 0, "y": 1}
    p.bouger("up")
    assert p.position == {"x": 0, "y": 2}
    
    print("fin des tests")


    

