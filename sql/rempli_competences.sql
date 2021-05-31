
INSERT INTO competences SET
    id_competence = 1,
    nom = "moins_un",
    description_ = "Enleve 1 à l'ennemi selectionné",
    type_cible = "ennemi",
    cout_mana = 3,
    tp_recharge = 5,
    img_icon = "moins_un.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 2,
    nom = "teleportation",
    description_ = "Se téléporte sur le terrain selectionné dans un rayon de 10 cases autour du joueur",
    type_cible = "terrain",
    cout_mana = 15,
    tp_recharge = 15,
    img_icon = "teleportation.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 3,
    nom = "premiers_secours",
    description_ = "Restaure 10% des pv max d'un autre joueur sélectionné, si aucun joueur n'est sélectionné, applique l'effet au joueur",
    type_cible = "joueur",
    cout_mana = 15,
    tp_recharge = 10,
    img_icon = "premiers_secours.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 4,
    nom = "bouclier",
    description_ = "Se protège de toutes attaques tout autour du joueur",
    type_cible = "",
    cout_mana = 15,
    tp_recharge = 20,
    img_icon = "bouclier.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 5,
    nom = "manger",
    description_ = "Mange et restaure 20% de ses PV",
    type_cible = "joueur",
    cout_mana = 10,
    tp_recharge = 15,
    img_icon = "manger.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 6,
    nom = "moins_un_zone",
    description_ = "Enlève 1 PV aux ennemis dans un rayon d'une case autour du joueur",
    type_cible = "ennemi",
    cout_mana = 4,
    tp_recharge = 5,
    img_icon = "moins_un_zone.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 7,
    nom = "provocation",
    description_ = "Provoque et attire les ennemis alentour",
    type_cible = "joueur",
    cout_mana = 5,
    tp_recharge = 15,
    img_icon = "provoc.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 8,
    nom = "invisibilite",
    description_ = "Devient invisible et indétectable des ennemis",
    type_cible = "joueur",
    cout_mana = 20,
    tp_recharge = 30,
    img_icon = "invisible.png",
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 9,
    nom = "tir_de_fusil",
    description_ = "Enlève 5 PV à un ennemi situé dans un rayon de 15 blocs",
    type_cible = "ennemi",
    cout_mana = 5,
    tp_recharge = 5,
    img_icon = "fusil.png",
    niv_min = 1;

INSERT INTO classes_competences SET id_competence = 1, nom_classe = "sorcier";
INSERT INTO classes_competences SET id_competence = 2, nom_classe = "sorcier";
INSERT INTO classes_competences SET id_competence = 3, nom_classe = "sorcier";
INSERT INTO classes_competences SET id_competence = 4, nom_classe = "chevalier";
INSERT INTO classes_competences SET id_competence = 5, nom_classe = "chevalier";
INSERT INTO classes_competences SET id_competence = 5, nom_classe = "chasseur";
INSERT INTO classes_competences SET id_competence = 6, nom_classe = "chevalier";
INSERT INTO classes_competences SET id_competence = 7, nom_classe = "chevalier";
INSERT INTO classes_competences SET id_competence = 8, nom_classe = "sorcier";
INSERT INTO classes_competences SET id_competence = 9, nom_classe = "chasseur";