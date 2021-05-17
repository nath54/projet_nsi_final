from gere_ennemis import dist_vec
import time


def gere_competences(ws_serv, websocket, data, id_user):
    #print("Compétence ! ",data)
    server = ws_serv.server
    #
    perso_joueur = server.personnages[id_user]
    #
    if not data["id_competence"] in perso_joueur.competences.values():
        #TODO : envoyer un message d'erreur
        #
        return
    #
    data_comp = server.data_competences[data["id_competence"]]
    #
    if data_comp["nom"] == "moins_un":
        id_monstre_spawn = data["id_monstre_spawn"]
        ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
        #
        ennemi.modif_vie(-1)
    
    elif data_comp["nom"] == "premiers_secours":
        if "id_joueur" in data.keys():
            p = server.personnages[data["id_joueur"]]
        else:
            p = server.personnages[id_user]
        p.vie += p.vie_max*0.1
        if p.vie > p.vie_max:
            p.vie = p.vie_max
        server.send_to_user(p.id_utilisateur, {"action":"vie", "value":p.vie, "max_v": p.vie_max})
        ws_serv.send_all({"action":"vie_joueur", "value":p.vie, "max_v": p.vie_max, "id_joueur": p.id_utilisateur}, [p.id_utilisateur])

    elif data_comp["nom"] == "teleportation":
        rayon = 5
        cooldown = 30
        if dist_vec((perso_joueur.position["x"], perso_joueur.position["y"]), (data["x"], data["y"]) < rayon:
            if "dernier_teleportation" not in perso_joueur.divers.keys() or time.time()-perso_joueur.divers["dernier_teleportation"]>cooldown:
                perso_joueur.divers["dernier_teleportation"] = time.time()
                x = data["x"]
                y = data["y"]
                dx = data["x"] - perso_joueur.position["x"]
                dy = data["y"] - perso_joueur.position["y"]
                perso_joueur.bouger((dx,dy))
                serveur.server.send_to_user(p.id_utilisateur, {"action": "position_perso", "x":p.position["x"], "y":p.position["y"]})
                serveur.server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":p.id_utilisateur, "x":p.position["x"], "y":p.position["y"], "region":p.region_actu}, [p.id_utilisateur])


    elif data_comp["nom"] == "moins_un_zone":
        id_monstre_spawn = data["id_monstre_spawn"]
        ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
        rayon = 1
        for x in range(-rayon,rayon+1):
            for y in range(-rayon,rayon):
                dx,dy = perso_joueur.position["x"]+x, perso_joueur.position["y"]+y
                ennemi = server.carte.regions[perso_joueur.id_utilisateur].get_case_monstre(dx, dy)
                if ennemi != None:
                    ennemi.modif_vie(-1)

    elif data_comp["nom"] == "manger":
        p = server.personnages[id_user]
        p.vie += p.vie_max*0.1
        if p.vie > p.vie_max:
            p.vie = p.vie_max
        server.send_to_user(p.id_utilisateur, {"action":"vie", "value":p.vie, "max_v": p.vie_max})

    elif data_comp["nom"] == "provocation" and\
            perso_joueur.classe == "chevalier":
        """Permet d'attirer un ennemi vers le joueur dans un rayon de 5"""
        monstres = server.carte.regions[perso_joueur.region_actu].ennemis
        perso_pos = (perso_joueur.position[x], perso_joueur.position[y])
        for ennemi in monstres:
            ennemi_pos = (ennemi.position[x], ennemi.position[y])
            if distance(ennemi_pos, perso_pos) <= 5:
                ennemi.joueur_detecte = perso_joueur
