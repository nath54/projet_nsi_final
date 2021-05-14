

def gere_competences(ws_serv, websocket, data, id_user):
    print("Compétence ! ",data)
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
        monstre = server.carte.regions[perso_joueur.region_actu].monstres[id_monstre_spawn]
        print(monstre)



