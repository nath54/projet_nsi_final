
INSERT INTO terrain SET
    id_terrain = 0,
    image_="vide.png",
    nom="vide",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=0;

INSERT INTO terrain SET
    id_terrain = 1,
    image_="terre.png",
    nom="terre",
    peut_marcher=1,
	cultivable=1,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 2,
    image_="herbe.png",
    nom="herbe",
    peut_marcher=1,
	cultivable=1,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 3,
    image_="neige.png",
    nom="neige",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 4,
    image_="sable.png",
    nom="sable",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 5,
    image_="chemin_terre_1.png",
    nom="chemin terre 1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 6,
    image_="chemin_pave_1.png",
    nom="chemin pavé 1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 7,
    image_="chemin_pave_2.png",
    nom="chemin pavé 2",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 8,
    image_="eau.png",
    nom="eau",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 9,
    image_="planches_eau_gauche.png",
    nom="planche eau gauche",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 10,
    image_="sol_pierre_0.png",
    nom="sol pierre 0",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 11,
    image_="sol_pierre_1.png",
    nom="sol pierre 1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 12,
    image_="sol_pierre_2.png",
    nom="sol pierre 2",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 13,
    image_="lava_1.gif",
    nom="lave 1",
    peut_marcher=0,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 14,
    image_="obsidienne.jpg",
    nom="obsidienne",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;


INSERT INTO terrain SET
    id_terrain = 15,
    image_="caillou_1.png",
    nom="caillou_1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 16,
    image_="sable_1.png",
    nom="sable_1",
    peut_marcher=1,
	cultivable=0,
	objet_dessus=1;

INSERT INTO terrain SET
    id_terrain = 17,
    image_="caillou_2.png",
    nom="caillou_2",
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


-- Compte admin

INSERT INTO comptes_administrateurs SET
    pseudo = "jeSuisPasUnAdminJeSuisDieu",
    mdp = MD5("pAdm1nstrat0r");