
CREATE TABLE utilisateurs (
	id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
	pseudo TEXT,
	mdp TEXT,
 	sexe TEXT,
 	vie INT DEFAULT 100,
 	stamina INT DEFAULT 100,
 	mana INT DEFAULT 100,
 	armor INT DEFAULT 0,
 	classe TEXT,
 	niveau INT DEFAULT 1,
 	argent INT DEFAULT 0,
 	experience INT DEFAULT 0,
 	experience_tot INT DEFAULT 100,
 	competence TEXT,
 	quetes TEXT,
 	region_actu INT DEFAULT 1,
 	position_x INT DEFAULT 1,
 	position_y INT DEFAULT 1,
 	id_tete INT DEFAULT 1,
 	id_cheveux INT DEFAULT 1,
 	id_barbe INT DEFAULT 1,
 	id_haut INT DEFAULT 1,
 	id_bas INT DEFAULT 1,
 	id_pieds INT DEFAULT 1);


CREATE TABLE personnalisation (
			id_utilisateur INT,
			id_tete INT,
	     	img_tete TEXT,
			id_cheveux INT,
		 	img_cheveux TEXT,
			id_barbe INT,
		 	img_barbe TEXT,
			id_haut INT,
			img_haut TEXT,
			id_bas INT,
			img_bas TEXT,
			id_pieds INT,
			img_pieds TEXT);


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


CREATE TABLE monstre (
	id_monstre  INT PRIMARY KEY,
	nom TEXT,
	niveau INT NOT NULL,
	pv TEXT NOT NULL,
	dgt TEXT NOT NULL,
	loot TEXT,
	img_base TEXT NOT NULL);


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


CREATE TABLE objets (
	id_objet INT PRIMARY KEY,
 	nom  TEXT,
 	image_ TEXT,
	z_index INT,
 	collision BOOLEAN);


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
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_terrain INT DEFAULT 0,
	CONSTRAINT comp_key_x_y PRIMARY KEY (x, y, id_region)
);

CREATE INDEX `index_id_region` ON `regions_terrains` (`id_region`);



CREATE TABLE regions_objets(
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_objet INT DEFAULT 0,
	CONSTRAINT comp_key_x_y PRIMARY KEY (x, y, id_region)
);

CREATE INDEX `index_id_region` ON `regions_objets` (`id_region`);



CREATE TABLE regions_monstres(
	id_monstre_spawn INT PRIMARY KEY AUTO_INCREMENT,
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_monstre INT DEFAULT 0,
);

CREATE INDEX `index_id_region` ON `regions_monstres` (`id_region`);



CREATE TABLE comptes_administrateurs (
	id_admin INT PRIMARY KEY AUTO_INCREMENT,
	pseudo TEXT NOT NULL,
	mdp TEXT NOT NULL
);


