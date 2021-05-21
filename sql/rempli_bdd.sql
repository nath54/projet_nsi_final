
INSERT INTO terrain SET
    id_terrain = 0,
    image_="vide.png",
    nom="vide",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=0;

INSERT INTO terrain SET
    id_terrain = 1,
    image_="caillou_1.png",
    nom="caillou_vert",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 2,
    image_="caillou_2.png",
    nom="caillou_gris",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 3,
    image_="chemin_pave_1.png",
    nom="chemin_pave",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 4,
    image_="chemin_pave_2.png",
    nom="chemin_pave_gris",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 5,
    image_="chemin_terre_1.png",
    nom="chemin_terre",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 6,
    image_="eau.png",
    nom="eau",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=0;

INSERT INTO terrain SET
    id_terrain = 7,
    image_="eau_1.png",
    nom="eau_2",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=0;

INSERT INTO terrain SET
    id_terrain = 8,
    image_="herbe.png",
    nom="herbe clair",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 9,
    image_="herbe_1.png",
    nom="herbe foncé",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;


INSERT INTO terrain SET
    id_terrain = 10,
    image_="lava_1.gif",
    nom="lava_1",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=0;

INSERT INTO terrain SET
    id_terrain = 11,
    image_="neige.png",
    nom="neige",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 12,
    image_="obsidienne.png",
    nom="obsidienne",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 13,
    image_="planches_eau_gauche.png",
    nom="planche eau",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=0;

INSERT INTO terrain SET
    id_terrain = 14,
    image_="sable.png",
    nom="sable",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 15,
    image_="sable_1.png",
    nom="sable 1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 16,
    image_="sol_pierre_0.png",
    nom="sol pierre",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 17,
    image_="sol_pierre_1.png",
    nom="sol_pierre_1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 18,
    image_="sol_pierre_2.png",
    nom="sol_pierre_2",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 19,
    image_="terre.png",
    nom="terre",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;



-- OBJETS :

INSERT INTO objets SET
    id_objet = 0,
    nom = "rien",
    image_ = "rien.png",
    z_index = 1,
    collision = 0;

INSERT INTO objets SET
    id_objet = 1,
    nom = "arbre_1",
    image_ = "arbre_1.png",
    z_index = 1,
    collision = 1;


INSERT INTO objets SET
    id_objet = 2,
    nom = "buisson_1",
    image_ = "buisson_1.png",
    z_index = 3,
    collision = 0;


INSERT INTO objets SET
    id_objet = 3,
    nom = "mur_1",
    image_ = "mur_1.png",
    z_index = 1,
    collision = 1;


INSERT INTO objets SET
    id_objet = 4,
    nom = "porte_prison_fermee",
    image_ = "porte_prison_fermee.png",
    z_index = 1,
    collision = 1;


INSERT INTO objets SET
    id_objet = 5,
    nom = "porte_prison_ouverte",
    image_ = "porte_prison_ouverte.png",
    z_index = 3,
    collision = 0;


INSERT INTO objets SET
    id_objet = 6,
    nom = "mur_metallique",
    image_ = "mur_metallique.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 7,
    nom = "arbre_2",
    image_ = "arbre_2.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 8,
    nom = "Arbre_chene_base",
    image_ = "arbre_chene_base.png",
    z_index = 3,
    collision = 1;


INSERT INTO objets SET
    id_objet = 9,
    nom = "Arbre_chene_haut",
    image_ = "Arbre_chene_haut.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 10,
    nom = "bois_1",
    image_ = "bois_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 11,
    nom = "bois_fenetre_1",
    image_ = "bois_fenetre_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 12,
    nom = "bois_porte_1",
    image_ = "bois_porte_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 13,
    nom = "mur_1",
    image_ = "mur_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 14,
    nom = "bloc1",
    image_ = "bloc1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 15,
    nom = "brique_jaune_1",
    image_ = "brique_jaune_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 16,
    nom = "brique_1",
    image_ = "brique_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 17,
    nom = "brique_fenetre_1",
    image_ = "brique_fenetre_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 18,
    nom = "brique_porte_1",
    image_ = "brique_porte_1.png",
    z_index = 3,
    collision = 1;

INSERT INTO objets SET
    id_objet = 19,
    nom = "mur_pierre_1",
    image_ = "mur_pierre_1.png",
    z_index = 3,
    collision = 1;    

INSERT INTO objets SET
    id_objet = 20,
    nom = "mur_colore",
    image_ = "mur_colore.png",
    z_index = 3,
    collision = 1;


-- Compte admin

INSERT INTO comptes_administrateurs SET
    pseudo = "jeSuisPasUnAdminJeSuisDieu",
    mdp = MD5("pAdm1nstrat0r");