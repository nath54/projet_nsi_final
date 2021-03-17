
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
		   complete BOOLEAN)


CREATE TABLE objet (id_objet INT,
	     nom_objet TEXT,
		 description_ TEXT,
		 image_ TEXT,
	     quantite INT)


CREATE TABLE inventaire (id_objet  INT,
	     id_utilisateur INT,
	     quantite INT)


CREATE TABLE monde (ville TEXT,
	     region TEXT,
		 niveau INT)


CREATE TABLE inventaire (id_quete INT,
	     quetes TEXT,
		 id_utilisateur INT)


CREATE TABLE pnj (id_pnj INT,
	     nom_pnj TEXT,
	     role TEXT)


CREATE TABLE inventaire (id_monstre  INT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT)


CREATE TABLE inventaire (id_monstre  INT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT)

