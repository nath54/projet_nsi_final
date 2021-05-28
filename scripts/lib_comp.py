from gere_ennemis import dist_vec
from _thread import start_new_thread as start_nt
import time


def gere_competences(ws_serv, websocket, data, id_user):
    #print("CompÃ©tence ! ",data)
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
    # TODO : mettre le cooldown ici, au lieu de le mettre dans chaque
    # data_comp["tp_recharge"]
    nc = data_compt["nom"] # Pour raccourcir le nom de la variable
    if nc in perso_joueur.divers["cooldowns"].keys():
        if time.time() - perso_joueur.divers["cooldowns"][nc] < data_comp["tp_recharge"]:
            # Ici, le temps n'est pas fini
            # On ne fais donc pas la competence
            return
    # TODO : enlever et mettre a jour le mana
    if perso_joueur.mana < data_comp["cout_mana"]:
        # Ici, il n'y a pas assez de mana
        # On ne fais donc pas la competence
        return
    #
    perso_joueur.divers["cooldowns"][nc] = time.time()
    perso_joueur.change_mana(-data_comp["cout_mana"])
    perso_joueur.update_cooldown(nc)
    #
    if data_comp["nom"] == "moins_un":
        rayon = 1
        heure = time.time()
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
        heure = time.time()
        if not ('heure_last_teleport' not in perso_joueur.divers.keys() or heure-data_comp['tp_recharge']>=perso_joueur.divers['heure_last_teleport']):
            # cd pas fini
            # a rendre plus propre
            return
        elif dist_vec((perso_joueur.position["x"], perso_joueur.position["y"]), (data["x"], data["y"])) < rayon:
            x = data["x"]
            y = data["y"]
            dx = data["x"] - perso_joueur.position["x"]
            dy = data["y"] - perso_joueur.position["y"]
            perso_joueur.bouger((dx,dy))
            server.send_to_user(perso_joueur.id_utilisateur, {"action": "position_perso", "x":perso_joueur.position["x"], "y":perso_joueur.position["y"]})
            server.serveurWebsocket.send_all({"action": "j_pos", "id_perso":perso_joueur.id_utilisateur, "x":perso_joueur.position["x"], "y":perso_joueur.position["y"], "region":perso_joueur.region_actu}, [perso_joueur.id_utilisateur])
            cout_mana = data_comp["cout_mana"]
            if perso_joueur.mana >= cout_mana:
                perso_joueur.mana_max - cout_mana
            if perso_joueur.mana < cout_mana:
                return
            perso_joueur.divers['heure_last_teleport'] = time.time()

    elif data_comp["nom"] == "manger": ## Comp qui ne sera dispo que pour le chevalier et chasseur
        ## TODO : Dès que l'inventaire est dispo, faire en sorte de passer par l'inventaire pour manger 
        heure = time.time()
        if not ('dernier_manger' not in perso_joueur.divers.keys() or heure-data_comp['faim_recharge']>=perso_joueur.divers['dernier_manger']):
            # cd pas fini
            # a rendre plus propre
            return
        if server.personnage.classe == "Chevalier" or server.personnage.classe == "Chasseur":
            if server.monstre.joueur_detecte == None :
                p = server.personnages[id_user]
                p.vie += p.vie_max*0.1
                if p.vie > p.vie_max:
                    p.vie = p.vie_max
                server.send_to_user(p.id_utilisateur, {"action":"vie", "value":p.vie, "max_v": p.vie_max})
    
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

    
    # elif data_comp["nom"] == "manger":
    #     p = server.personnages[id_user]
    #     p.vie += p.vie_max*0.1
    #     if p.vie > p.vie_max:
    #         p.vie = p.vie_max
    #     server.send_to_user(p.id_utilisateur, {"action":"vie", "value":p.vie, "max_v": p.vie_max})

    elif data_comp["nom"] == "provocation" and\
            perso_joueur.classe == "chevalier":
        """Permet d'attirer un ennemi vers le joueur dans un rayon de 5"""
        monstres = server.carte.regions[perso_joueur.region_actu].ennemis
        perso_pos = (perso_joueur.position["x"], perso_joueur.position["y"])
        for ennemi in monstres:
            ennemi_pos = (ennemi.position["x"], ennemi.position["y"])
            if dist_vec(ennemi_pos, perso_pos) <= 5: #distance ?
                ennemi.joueur_detecte = perso_joueur

        x = data["x"]
        y = data["y"]
        dx = data["x"] - perso_joueur.position["x"]
        dy = data["y"] - perso_joueur.position["y"]
        perso_joueur.bouger((dx,dy))

    # elif data_comp["nom"] == "moins_un_zone":
    #     if server.personnage.classe == "Chevalier":
    #         id_monstre_spawn = data["id_monstre_spawn"]
    #         ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
    #         rayon = 1
    #         for x in range(-rayon,rayon+1):
    #             for y in range(-rayon,rayon):
    #                 dx,dy = perso_joueur.position["x"]+x, perso_joueur.position["y"]+y
    #                 ennemi = server.carte.regions[perso_joueur.id_utilisateur].get_case_monstre(dx, dy)
    #                 if ennemi != None:
    #                     ennemi.modif_vie(-1)
   
    
    
    elif data_comp["nom"] == "invisibilite":
        if "invisible" in perso_joueur.divers.keys():
            return
            # Gérer erreur
        tp_invisibilite = 10
        fininvisibilite = time.time()+tp_invisibilite
        perso_joueur.divers["invisible"] = fininvisibilite
        
        def stop_invisibilite(tp,joueur):
            time.sleep(tp)
            del joueur.divers["invisible"]

        start_nt(stop_invisibilite,(10,perso_joueur))
       

    elif data_comp["nom"] == "sort_passionanant":
        if monstre.joueur_detecte is not None:
            pass
        
        

    elif data_comp["nom"] == "boule_de_feu_supreme":
        id_monstre_spawn = data["id_monstre_spawn"]
        ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
        rayon = 1
        for x in range(-rayon,rayon+1):
            for y in range(-rayon,rayon):
                dx,dy = perso_joueur.position["x"]+x, perso_joueur.position["y"]+y
                ennemi = server.carte.regions[perso_joueur.id_utilisateur].get_case_monstre(dx, dy)
                if ennemi != None:
                    ennemi.modif_vie(-10)

    elif data_comp["nom"] == "coup_du_tonnerre":
        id_monstre_spawn = data["id_monstre_spawn"]
        ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
        rayon = 1
        for x in range(-rayon,rayon+1):
            for y in range(-rayon,rayon):
                dx,dy = perso_joueur.position["x"]+x, perso_joueur.position["y"]+y
                ennemi = server.carte.regions[perso_joueur.id_utilisateur].get_case_monstre(dx, dy)
                if ennemi != None:
                    ennemi.modif_vie(-40)

    elif data_comp["nom"] == "faisceau_de_lumiere":
        id_monstre_spawn = data["id_monstre_spawn"]
        ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
        rayon = 1
        for x in range(-rayon,rayon+1):
            for y in range(-rayon,rayon):
                dx,dy = perso_joueur.position["x"]+x, perso_joueur.position["y"]+y
                ennemi = server.carte.regions[perso_joueur.id_utilisateur].get_case_monstre(dx, dy)
                if ennemi != None:
                    ennemi.modif_vie(-25)

    elif data_comp["nom"] == "sort_Foudre_celeste":
        id_monstre_spawn = data["id_monstre_spawn"]
        ennemi = server.carte.regions[perso_joueur.region_actu].ennemis[id_monstre_spawn]
        rayon = 1
        for x in range(-rayon,rayon+1):
            for y in range(-rayon,rayon):
                dx,dy = perso_joueur.position["x"]+x, perso_joueur.position["y"]+y
                ennemi = server.carte.regions[perso_joueur.id_utilisateur].get_case_monstre(dx, dy)
                if ennemi != None:
                    ennemi.modif_vie(-100)


def fininvisible(duree,joueur):
    time.sleep(duree)
    del joueur.divers['invisible']

    

