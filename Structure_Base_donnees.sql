
CREATE TABLE utilisateurs (
 id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
 pseudo TEXT,
 mdp TEXT,
 sexe TEXT,
 vie INT,
 stamina INT,
 mana INT,
 armor INT,
 classe TEXT,
 niveau INT,
 argent INT
 experience INT,
 experience_tot INT,
 competence TEXT,
 quetes TEXT,
 region_actu INT DEFAULT 1,
 position_x INT,
 position_y INT);


CREATE TABLE objet (
			id_objet INT PRIMARY KEY AUTO_INCREMENT,
	     	nom_objet TEXT,
		 	description_ TEXT,
		 	image_ TEXT,
			effet TEXT);


CREATE TABLE inventaire (
			id_objet  INT PRIMARY KEY AUTO_INCREMENT,
	     	id_utilisateur INT,
	     	quantite INT);


CREATE TABLE monde (
			id_monde INT PRIMARY KEY AUTO_INCREMENT,
			ville TEXT,
	     	region TEXT,
		 	niveau INT);


CREATE TABLE quete
(
    id_quete INT PRIMARY KEY AUTO_INCREMENT,
    nom TEXT,
    description_ TEXT,
    condition_ TEXT,
    objectif TEXT,
    recompense TEXT
);


CREATE TABLE pnj (
			id_pnj INT PRIMARY KEY AUTO_INCREMENT,
	     	nom_pnj TEXT,
	     	role_ TEXT);


CREATE TABLE monstre (id_monstre  INT PRIMARY KEY AUTO_INCREMENT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT);


CREATE TABLE classe (
			id_classe  INT PRIMARY KEY AUTO_INCREMENT,
	     	nom_classe TEXT,
	     	force_ INT,
		 	armure INT,
		 	dgt INT);


CREATE TABLE terrain (
			id_terrain INT PRIMARY KEY,
		 	image_ TEXT,
		 	nom  TEXT,
	     	peut_marcher BOOLEAN,
		 	cultivable BOOLEAN,
		 	objet_dessus BOOLEAN);


CREATE TABLE regions(
	id_region INT PRIMARY KEY AUTO_INCREMENT,
	nom TEXT,
	tx INT,
	ty INT,
	voisin_droite INT DEFAULT NULL,
	voisin_gauche INT DEFAULT NULL,
	voisin_haut INT DEFAULT NULL,
	voisin_bas INT DEFAULT NULL
);


CREATE TABLE regions_terrains(
	id_regions_terrains INT PRIMARY KEY AUTO_INCREMENT,
	id_region INT,
	x INT,
	y INT,
	id_terrain INT DEFAULT 0
);

