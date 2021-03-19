
CREATE TABLE utilisateurs (id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
	       pseudo TEXT,
		   mdp TEXT,
		   vie_max INT,
		   classe TEXT,
		   niveau INT,
		   experience INT,
		   competence TEXT,
		   quetes TEXT,
		   id_quete INT,
		   complete BOOLEAN);


CREATE TABLE objet (id_objet INT PRIMARY KEY AUTO_INCREMENT,
	     nom_objet TEXT,
		 description_ TEXT,
		 image_ TEXT,
	     quantite INT);


CREATE TABLE inventaire (id_objet  INT PRIMARY KEY AUTO_INCREMENT,
	     id_utilisateur INT,
	     quantite INT);


CREATE TABLE monde (ville TEXT,
	     region TEXT,
		 niveau INT);


CREATE TABLE quete
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT
    nom TEXT,
    description TEXT,
    condition TEXT,
    objectif TEXT,
    recompense TEXT
)


CREATE TABLE pnj (id_pnj INT PRIMARY KEY AUTO_INCREMENT,
	     nom_pnj TEXT,
	     role TEXT);


CREATE TABLE monstre (id_monstre  INT PRIMARY KEY AUTO_INCREMENT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT);


CREATE TABLE classe (id_classe  INT PRIMARY KEY AUTO_INCREMENT,
	     nom_classe TEXT,
	     force INT,
		 armure INT,
		 dgt INT);

