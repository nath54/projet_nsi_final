

CREATE TABLE utilisateurs (
	id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
	pseudo TEXT NOT NULL,
	mdp TEXT NOT NULL,
 	sexe TEXT NOT NULL DEFAULT "femme",
 	vie INT NOT NULL DEFAULT 100,
 	stamina INT NOT NULL DEFAULT 100,
 	mana INT NOT NULL DEFAULT 100,
 	armor INT NOT NULL DEFAULT 0,
 	classe TEXT NOT NULL DEFAULT "chevalier",
 	argent INT NOT NULL DEFAULT 0,
 	experience INT NOT NULL DEFAULT 0,
 	experience_tot INT NOT NULL DEFAULT 100,
 	competence TEXT NOT NULL DEFAULT '',
 	quetes TEXT NOT NULL  DEFAULT '',
 	region_actu INT NOT NULL DEFAULT 1 ,
 	position_x INT NOT NULL DEFAULT 1 ,
 	position_y INT NOT NULL DEFAULT 1 ,
	id_tete INT NOT NULL DEFAULT 1,
	img_tete TEXT NOT NULL DEFAULT 1,
	id_cheveux INT NOT NULL DEFAULT 1,
	img_cheveux TEXT NOT NULL DEFAULT 1,
	id_barbe INT NOT NULL DEFAULT 1,
	img_barbe TEXT NOT NULL DEFAULT 1,
	id_haut INT NOT NULL DEFAULT 1,
	img_haut TEXT NOT NULL DEFAULT 1,
	id_bas INT NOT NULL DEFAULT 1,
	img_bas TEXT NOT NULL DEFAULT 1,
	id_pieds INT NOT NULL DEFAULT 1,
	img_pieds TEXT NOT NULL DEFAULT 1,
	niveau INT NOT NULL DEFAULT 0,
	arme INT DEFAULT NULL
);


CREATE TABLE tokens (
	id_utilisateur INT PRIMARY KEY,
	token TEXT NOT NULL
);


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
	img_pieds TEXT
);


CREATE TABLE inventaire (
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_objet INT NOT NULL,
	id_utilisateur INT NOT NULL,
 	quantite INT NOT NULL DEFAULT 1
);


CREATE TABLE monde (
	id_monde INT PRIMARY KEY AUTO_INCREMENT,
	ville TEXT,
	region TEXT,
 	niveau INT
);


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
 	role_ TEXT
);


CREATE TABLE monstre (
	id_monstre  INT PRIMARY KEY,
	nom TEXT,
	niveau INT NOT NULL,
	pv TEXT NOT NULL,
	dgt TEXT NOT NULL,
	loot TEXT DEFAULT "[]",
	img_base TEXT NOT NULL DEFAULT "",
	img_mort TEXT NOT NULL DEFAULT "tombe.png",
	img_negatif TEXT NOT NULL DEFAULT "",
	img_en_combat TEXT NOT NULL DEFAULT "",
	temps_bouger INT NOT NULL DEFAULT 0.8,
	rayon_detect INT NOT NULL DEFAULT 3,
	rayon_perdu INT NOT NULL DEFAULT 6,
	portee_attaque INT NULL DEFAULT 1,
	agressif BOOLEAN NOT NULL DEFAULT 1,
	pacifique BOOLEAN NOT NULL DEFAULT 0
);


CREATE TABLE classe (
	id_classe  INT PRIMARY KEY AUTO_INCREMENT,
 	nom_classe TEXT,
 	force_ INT,
 	armure INT,
 	dgt INT
);


CREATE TABLE terrain (
	id_terrain INT PRIMARY KEY,
 	image_ TEXT,
 	nom  TEXT,
 	peut_marcher BOOLEAN,
 	cultivable BOOLEAN,
 	objet_dessus BOOLEAN
);


CREATE TABLE objets (
	id_objet INT PRIMARY KEY,
 	nom  TEXT,
 	image_ TEXT,
	z_index INT,
 	collision BOOLEAN
);


CREATE TABLE regions(
	id_region INT PRIMARY KEY AUTO_INCREMENT,
	nom TEXT NOT NULL,
	description_ TEXT
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
	parametres TEXT NOT NULL DEFAULT '{}',
	CONSTRAINT comp_key_x_y PRIMARY KEY (x, y, id_region)
);

CREATE INDEX `index_id_region` ON `regions_objets` (`id_region`);



CREATE TABLE regions_monstres(
	id_monstre_spawn INT PRIMARY KEY AUTO_INCREMENT,
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_monstre INT DEFAULT 0
);

CREATE INDEX `index_id_region` ON `regions_monstres` (`id_region`);



CREATE TABLE comptes_administrateurs (
	id_admin INT PRIMARY KEY AUTO_INCREMENT,
	pseudo TEXT NOT NULL,
	mdp TEXT NOT NULL
);



CREATE TABLE arme (
	id_arme INT PRIMARY KEY AUTO_INCREMENT,
	nom TEXT,
	classe TEXT,
	dgt INT,
 	niveau INT,
	style TEXT,
	portee TEXT,
	munition TEXT,
	quantite_mun INT,
	img_arme TEXT
);


CREATE TABLE competences (
	id_competence INT PRIMARY KEY,
	nom TEXT NOT NULL,
	description_ TEXT,
	type_cible TEXT,
	cout_mana INT NOT NULL,
	tp_recharge FLOAT NOT NULL,
	img_icon TEXT NOT NULL,
	niv_min INT NOT NULL DEFAULT 1
);


CREATE TABLE classes_competences (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_competence INT NOT NULL,
	nom_classe TEXT NOT NULL
);

