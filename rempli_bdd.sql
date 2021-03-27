
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
    image_="sol_pierre_O.png",
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


-- OBJETS :

INSERT INTO objets SET
    id_objet = 1,
    nom = "arbre_1",
    image_ = "arbre_1.png",
    collision = 1;


INSERT INTO objets SET
    id_objet = 2,
    nom = "buisson_1",
    image_ = "buisson_1.png",
    collision = 1;


INSERT INTO objets SET
    id_objet = 3,
    nom = "mur_1",
    image_ = "mur_1.png",
    collision = 1;


INSERT INTO objets SET
    id_objet = 4,
    nom = "porte_prison_fermee",
    image_ = "porte_prison_fermee.png",
    collision = 1;


INSERT INTO objets SET
    id_objet = 5,
    nom = "porte_prison_ouverte",
    image_ = "porte_prison_ouverte.png",
    collision = 0;


