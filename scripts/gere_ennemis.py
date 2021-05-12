
import time
import math
import random

# a et b sont deux tuples d'entiers
def dist_vec(a, b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

# a et b sont deux tuples d'entiers
def sum_vec(a,b):
    return (a[0]+b[0], a[1]+b[1])

# renvoie la prochaine case
# depart et arrivee sont des tuples (x, y)
# Petit algo de recherche de chemin simple pour l'instant
def rech_chemin_simple(server, id_region, depart, arrivee, lst_deps=[(0,1),(0,-1),(1,0),(-1,0)]):
    ppt = None
    dist = dist_vec(depart, arrivee)
    for deplacement in lst_deps:
        new_pos = sum_vec(depart, deplacement)
        # On vérifie les collisions de la case
        if not server.carte.est_case_libre(id_region, new_pos[0], new_pos[1]):
            continue
        # On cherche le deplacement qui rapproche le plus de l'arrivée
        distance = dist_vec(new_pos, arrivee)
        if dist == None or distance < dist:
            ppt = deplacement
            dist = distance
    return ppt # faudra aussi faire un test si ppt != None, en gros, si on peut se déplacer


# position est un tuple
def rech_dep_alea(server, id_region, position, lst_deps=[(0,1),(0,-1),(1,0),(-1,0)]):
    res_dep = None
    possibles = []
    # On recherche tous les déplacements possibles
    for dep in lst_deps:
        new_pos = sum_vec(position, dep)
        if server.carte.est_case_libre(id_region, new_pos[0], new_pos[1]):
            possibles.append(dep)
    # Faudra faire un test si != None
    if len(possibles) == 0:
        return None
    else:
        return random.choice(possibles)


# Fonction qui va gérer tous les ennemis
def gere_ennemis(server):
    server.nb_t_actifs += 1
    while server.running:

        # On s'occupe des monstres
        for id_region, region in server.carte.regions.items():
            # On vérifie qu'il y a au moin un joueur dans la région
            if server.carte.nb_players_in_region(id_region) == 0:
                continue
            #

            # Une double boucle, ce n'est pas très beau, mais on fait simple pour l'instant
            for monstre in region.ennemis.values():
                
                try:

                    # On ne bouge que les monstres vivants
                    if monstre.etat != "vivant":
                        continue
                    # on les bouge toutes les secondes
                    tpb = monstre.tp_bouger
                    if monstre.joueur_detecte:
                        tpb *= 0.75
                    if time.time() - monstre.dernier_bouger < tpb:
                        continue
                    #
                    monstre.dernier_bouger = time.time()
                    # monstre
                    if monstre.joueur_detecte is None:
                        for joueur in server.personnages.values():
                            if joueur.region_actu == id_region:
                                m_pos = (monstre.position["x"], monstre.position["y"])
                                j_pos = (joueur.position["x"], joueur.position["y"])
                                if dist_vec(m_pos, j_pos) < monstre.detection_joueur:
                                    monstre.joueur_detecte = joueur
                    #
                    if monstre.joueur_detecte is not None:
                        m_pos = (monstre.position["x"], monstre.position["y"])
                        j_pos = (monstre.joueur_detecte.position["x"], monstre.joueur_detecte.position["y"])
                        if dist_vec(m_pos, j_pos) >= monstre.perte_joueur:
                            monstre.joueur_detecte = None
                    if monstre.joueur_detecte is not None:
                        #
                        # m_pos = (monstre.position["x"], monstre.position["y"])
                        # j_pos = (monstre.joueur_detecte.position["x"], monstre.joueur_detecte.position["y"])
                        if dist_vec(m_pos, j_pos) <= monstre.portee_attaque:
                            # On attaque
                            att = monstre.get_value_from_formes(monstre.dgt)
                            monstre.joueur_detecte.subit_degats(att)
                        else:
                            # On se dirige vers le joueur
                            res_dep = rech_chemin_simple(server, id_region, m_pos, j_pos)
                            if res_dep != None:
                                monstre.bouger(res_dep)
                            else:
                                monstre.nb_bloque += 1
                                if monstre.nb_bloque >= monstre.patiente_bloque:
                                    monstre.nb_bloque = 0
                                    position = (monstre.position["x"], monstre.position["y"])
                                    res_dep = rech_dep_alea(server, id_region, position)
                                    if res_dep == None:
                                        monstre.bouger(res_dep)

                            #
                            monstre.compteur_deplacements_retour += 1
                    elif monstre.compteur_deplacements_retour < monstre.max_compteur_deplacement_retour:
                        # On peut le bouger aléatoirement
                        position = (monstre.position["x"], monstre.position["y"])
                        res_dep = rech_dep_alea(server, id_region, position)
                        #
                        if res_dep != None:
                            # On a notre deplacement
                            monstre.bouger(res_dep)
                        #
                    else:
                        # Il doit revenir a sa place
                        depart = (monstre.position["x"], monstre.position["y"])
                        arrivee = (monstre.position_base["x"], monstre.position_base["y"])
                        res_dep = rech_chemin_simple(server, id_region, depart , arrivee)
                        if res_dep != None:
                            # On a notre deplacement
                            monstre.bouger(res_dep)
                except Exception as e:
                    print("Erreur (mais, hehehe, j'ai pas planté) : ", e)


        # on attends un peu
        time.sleep(0.0618)

    # Fin du thread
    print("Fin de l'ennemi")
    server.nb_t_actifs -= 1
