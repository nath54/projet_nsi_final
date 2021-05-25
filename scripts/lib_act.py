
def gere_actions(ws_serv, data, websocket, id_user):
    print("acitons ! ", data)
    server = ws_serv.server
    #TODO : vérifier que l'objet sur la case possede bien l'action
    nom_act = data["nom_action"]
    if nom_act == "change_region":
        server.db.action_db("UPDATE utilisateurs SET region_actu=? WHERE id_utilisateur=?;", (data["id_region"],  id_user))
        ws_serv.send(websocket, {"action": "reload"})
    