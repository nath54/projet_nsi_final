# Projet_classe :

## TABLE `utilisateurs`:
 - `id_utilisateur` *INT PRIMARY KEY AUTO_INCREMENT* : id user
 - `pseudo` _TEXT_ : pseudo
 - `vie_max` _INT_ : Vie max du joueur
 - `classe` _TEXT_ : classe du joueur
 - `niveau` _INT_ : niveau du joueur
 - `experience` _INT_ : expérience du joueur
 - `competence` __TEXT_ : qualité du personnage

```sql
CREATE TABLE utilisateurs (id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
	       pseudo TEXT,
		   mdp TEXT, 
		   classe TEXT,
		   niveau INT, 
		   experience INT,
		   competence TEXT)
```


## TABLE `objet`:
 - `id_objet` _INT_ : id objet dans le jeu
 - `nom_objet` _TEXT_ : nom des objets
 -  `quantite` _INT_ : Quantite d'un objet 

```sql
CREATE TABLE objet (id_objet INT,
	     nom_objet TEXT,
	     quantite INT)
```


## TABLE `inventaire`:
 - `id_objet` _INT_ : id objet
 - `id_utilisateur` _INT_ : id user
 -  `quantite` _INT_ : Quantite d'un objet 

```sql
CREATE TABLE inventaire (id_objet  INT,
	     id_utilisateur INT,
	     quantite INT)
```


## TABLE `quete`:
 - `id_quete` _INT_ : id quete
 - `quetes` _TEXT_ : Quêtes dans le monde
 
```sql
CREATE TABLE inventaire (id_quete INT,
	     quetes TEXT)
```


## TABLE `pnj`:
 - `id_pnj` _INT_ : id pnj
 - `nom_pnj` _TEXT_ : nom_pnj
 -  `role` _TEXT_ : métier d'un pnj

```sql
CREATE TABLE pnj (id_pnj INT,
	     nom_pnj TEXT,
	     role TEXT)
```



