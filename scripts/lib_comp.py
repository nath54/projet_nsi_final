

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
        x = data["x"]
        y = data["y"]
        dx = data["x"] - perso_joueur.position["x"]
        dy = data["y"] - perso_joueur.position["y"]
        perso_joueur.bouger((dx,dy))

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

