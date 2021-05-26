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

    if data['nom_competence']=="faisceau_de_lumiere":
        faisceau_de_lumiere(data,serveur,ws,id_joueur)
    


def sort_teleportation(data,serveur,ws,id_joueur):
    p = serveur.server.personnages[id_joueur]
    rayon = 5
    if server.carte.est_case_libre(p.region_actu, data['x'], data['y']):
        if dist_vec((p.position["x"], p.position["y"]), (data["x"], data["y"]) < rayon:
            p.position["x"] = data['x'] 
            p.position["y"] = data['y']
            serveur.server.send_to_user(p.id_utilisateur, {"action": "position_perso", "x":p.position["x"], "y":p.position["y"]})
            serveur.server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":p.id_utilisateur, "x":p.position["x"], "y":p.position["y"], "region":p.region_actu}, [p.id_utilisateur])

def boule_de_feu_supreme(data,serveur,ws,id_joueur):
    p = serveur.server.personnages[id_joueur]
    m = serveur.server.monstres[id_monstre_spawn]
    id_monstre_spawn = data["id_monstre_spawn"]
    ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
    ennemi.modif_vie(-10)

def coup_du_tonerre(data,serveur,ws,id_joueur):
    p = serveur.server.personnages[id_joueur]
    m = serveur.server.monstres[id_monstre_spawn]
    id_monstre_spawn = data["id_monstre_spawn"]
    ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
    ennemi.modif_vie(-40)
    

def faisseau_de_lumiere(data,serveur,ws,id_joueur):
    p = serveur.server.personnages[id_joueur]
    m = serveur.server.monstres[id_monstre_spawn]
    id_monstre_spawn = data["id_monstre_spawn"]
    ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
    ennemi.modif_vie(-25)


def sort_Foudre_celeste(data,serveur,ws,id_joueur):
    p = server.personnages[id_joueur]
    m = server.monstres[id_monstre_spawn]
    id_monstre_spawn = data["id_monstre_spawn"]
    ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
    ennemi.modif_vie(-100)

def sort_Passionant(data,serveur,ws,id_joueur):
    pass

def sous_les_radars(data,serveur,ws,id_joueur):
    p = server.personnages[id_joueur]
    m = server.monstres[id_monstre_spawn]
    pdivers