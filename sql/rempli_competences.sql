
INSERT INTO competences SET
    id_competence = 1,
    nom = "moins_un",
    description_ = "Enleve 1 à l'ennemi selectionné",
    type_cible = "ennemi",
    cout_mana = 3,
    tp_recharge = 5,
    img_icon = "moins_un.png";
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 2,
    nom = "teleportation",
    description_ = "Se téléporte sur le terrain selectionné dans un rayon de 10 cases autour du joueur",
    type_cible = "terrain",
    cout_mana = 15,
    tp_recharge = 15,
    img_icon = "teleportation.png";
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 3,
    nom = "premiers_secours",
    description_ = "Restaure 10% des pv max d'un autre joueur sélectionné, si aucun joueur n'est sélectionné, applique l'effet au joueur",
    type_cible = "joueur",
    cout_mana = 15,
    tp_recharge = 10,
    img_icon = "premiers_secours.png";
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 4,
    nom = "bouclier",
    description_ = "se protège de toutes attaques tout autours du joueur",
    type_cible = "",
    cout_mana = 15,
    tp_recharge = 20,
    img_icon = "bouclier.png";
    niv_min = 1;

INSERT INTO competences SET
    id_competence = 5,
    nom = "manger",
    description_ = "mange et restaure 20% de ses PV",
    type_cible = "joueur",
    cout_mana = 10,
    tp_recharge = 15,
    img_icon = "manger.png";

    

    