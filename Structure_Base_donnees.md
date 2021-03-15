# Projet_classe :

## TABLE `utilisateurs`:
 - `id_utilisateur` *INT PRIMARY KEY AUTO_INCREMENT* : id user
 - `pseudo` _TEXT_ : pseudo
 - `mdp` _TEXT_ : mdp du user
 - `vie_max` _INT_ : Vie max du joueur
 - `classe` _TEXT_ : classe du joueur
 - `niveau` _INT_ : niveau du joueur
 - `experience` _INT_ : expérience du joueur
 - `competence` __TEXT_ : qualité du personnage
 - `quetes` _TEXT_ : les quetes réalisée par le joueur
 - `id_quete` _INT_ : id des quetes
 - `complete` _BOOLEAN_ : si la quete est complété ou non par le joueur


```sql
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
```


## TABLE `objet`:
 - `id_objet` _INT_ : id objet dans le jeu
 - `nom_objet` _TEXT_ : nom des objets
 - `quantite` _INT_ : Quantite d'un objet

```sql
CREATE TABLE objet (id_objet INT,
	     nom_objet TEXT,
	     quantite INT)
```


## TABLE `inventaire`:
 - `id_objet` _INT_ : id objet
 - `id_utilisateur` _INT_ : id user
 - `quantite` _INT_ : Quantite d'un objet

```sql
CREATE TABLE inventaire (id_objet  INT,
	     id_utilisateur INT,
	     quantite INT)
```


## TABLE `monde`:
 - `ville` _TEXT_ : nom ville
 - `region` _TEXT_ : region du monde
 - `niveau` _INT_ : niveau des villes ou region

```sql
CREATE TABLE monde (ville TEXT,
	     region TEXT,
		 niveau INT)
```


## TABLE `quete`:
 - `id_quete` _INT_ : id quete
 - `quetes` _TEXT_ : Quêtes dans le monde
 - `id_utilisateur` _INT_ : id des utilisateur ayant complété la quete (Jointure à réaliser)

```sql
CREATE TABLE inventaire (id_quete INT,
	     quetes TEXT,
		 id_utilisateur INT)
```


## TABLE `pnj`:
 - `id_pnj` _INT_ : id pnj
 - `nom_pnj` _TEXT_ : nom_pnj
 - `role` _TEXT_ : métier d'un pnj

```sql
CREATE TABLE pnj (id_pnj INT,
	     nom_pnj TEXT,
	     role TEXT)
```


## TABLE `monstre`:
 - `id_monstre` _INT_ : id d'un monstre
 - `nom_monstre` _TEXT_ : nom du monstre
 - `pv` _INT_ : pv du monstre
 - `armure` _INT_ : armure du monstre
 - `dgt` _INT_ : dégats infligés par le monstre

```sql
CREATE TABLE inventaire (id_monstre  INT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT)
```


## TABLE `classe`:
 - `id_classe` _INT_ : id de la classe
 - `nom_classe` _TEXT_ : nom de la classe
 - `force` _INT_ : force de base de la classe
 - `armure` _INT_ : armure de monstre
 - `dgt` _INT_ : dégats infligés par le monstre

```sql
CREATE TABLE inventaire (id_monstre  INT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT)
```


## TABLE `terrain`:
 - `id_terrain` *INT PRIMARY KEY AUTO_INCREMENT* : id du terrain
 - `nom` TEXT : nom du terrain
 - `peut_marcher` BOOLEAN : si on peut marcher sur la case
 - `image` TEXT : image du terrain
 - `cultivable` BOOLEAN : si l'on peut cultiver dessus
 - `objet_dessus` BOOLEAN : si il y a un objet dessus

```sql
CREATE TABLE inventaire (id_terrain INT PRIMARY KEY AUTO_INCREMENT,
		 image TEXT,
		 nom  TEXT,
	     peut_marcher BOOLEAN,
		 cultivable BOOLEAN,
		 objet_dessus BOOLEAN)
```

## TABLE `regions`
 - `id_region` *INT PRIMARY KEY AUTO_INCREMENT* : id de la region
 - `nom` _TEXT_ : nom de la region
 - `tx` _INT_ : nombre de cases horizontales de la region
 - `ty` _INT_ : nombre de cases verticales de la region
 - `voisin_droite` _INT DEFAULT NULL_ : id de la region qui se situe à droite de cette région
 - `voisin_gauche` _INT DEFAULT NULL_ : id de la region qui se situe à gauche de cette région
 - `voisin_haut` _INT DEFAULT NULL_ : id de la region qui se situe à haut de cette région
 - `voisin_bas` _INT DEFAULT NULL_ : id de la region qui se situe à bas de cette région

## TABLE `regions_terrains`
- `id` *INT PRIMARY KEY AUTO_INCREMENT* : id de la case de la region
- `id_region` _INT_ : id de la region
- `x` _INT_
- `y` _INT_
- `id_terrain` _INT DEFAULT 0_ :




