def fait_competence(data,serveur,ws,id_joueur):
    if data['nom_competence']=="sort_teleportation":
        sort_teleportation(data,serveur,ws,id_joueur)

    if data['nom_competence']=="sort_Foudre_celeste":
        sort_Foudre_celeste(data,serveur,ws,id_joueur)
    
    if data['nom_competence']=="sort_Passionant":
        sort_Passionant(data,serveur,ws,id_joueur)

    if data['nom_competence']=="coup_du_tonerre":
        coup_du_tonerre(data,serveur,ws,id_joueur)

    if data['nom_competence']=="boule_de_feu_supreme":
        boule_de_feu_supreme(data,serveur,ws,id_joueur)

    if data['nom_competence']=="sous_les_radars":
        sous_les_radars(data,serveur,ws,id_joueur)

    if data['nom_competence']=="faisseau_de_lumiere":
        faisseau_de_lumiere(data,serveur,ws,id_joueur)
    


def sort_teleportation(data,serveur,ws,id_joueur):
    p = serveur.server.personnages[id_joueur]
    if server.server.carte.est_case_libre(p.region_actu, data['x'], data['y']):
        p.position["x"] = data['x'] 
        p.position["y"] = data['y']
        serveur.server.send_to_user(p.id_utilisateur, {"action": "position_perso", "x":p.position["x"], "y":p.position["y"]})
        serveur.server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":p.id_utilisateur, "x":p.position["x"], "y":p.position["y"], "region":p.region_actu}, [p.id_utilisateur])

def sort_Foudre_celeste(data,serveur,ws,id_joueur):
    p = serveur.server.personnages[id_joueur]
    m = serveur.server.monstres[id_monstre]
    if self.server.monstre.position == {'x': npx, 'y': npy}:
            self.server.monstre.modif_vie(dgt)
