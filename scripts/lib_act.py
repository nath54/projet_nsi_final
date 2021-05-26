
def gere_actions(ws_serv, data, websocket, id_user):
    print("acitons ! ", data)
    server = ws_serv.server
    #TODO : vérifier que l'objet sur la case possede bien l'action
    nom_act = data["nom_action"]
    if nom_act == "change_region":
        server.personnages[id_user].position = {"x": data["x"], "y": data["y"]}
        server.db.action_db("UPDATE utilisateurs SET region_actu=?, position_x=?, position_y=? WHERE id_utilisateur=?;", (data["id_region"], data["x"], data["y"], id_user))
        ws_serv.send(websocket, {"action": "reload"})
    