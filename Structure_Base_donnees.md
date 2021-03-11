Projet_classe :

-utilisateurs (id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
	       Pseudo TEXT,
		   mdpTEXT, 
		   classe TEXT,
		   niveau INT, 
		   experience INT,
		   caracteristique TEXT) 

-inventaire (id_objet  INT,
	     id_utilisateur,
	     quantite INT)

-objet(id_objet INT, 
	nom_objets TEXT, 
	quantite INT)

-monde(quetes TEXT)


