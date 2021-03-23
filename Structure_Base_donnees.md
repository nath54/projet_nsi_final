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
CREATE TABLE utilisateurs (
			id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
	    	pseudo TEXT,
		   	mdp TEXT,
			sexe TEXT,
			classe TEXT,
			region INT,
			position TEXT,
			vie INT,
		   	vie_max INT,
		   	niveau INT,
		   	experience INT,
			stamina INT,
			mana INT,
			mana_max INT,
			inventaire TEXT,
			argent INT,
		   	competence TEXT,
		   	quetes TEXT,
		   	id_quete INT,
		   	complete BOOLEAN);
```


## TABLE `objet`:
 - `id_objet` *INT PRIMARY KEY AUTO_INCREMENT* : id objet dans le jeu
 - `nom_objet` _TEXT_ : nom des objets
 - `description_` _TEXT_ : description de l'objet
 - `image_` _TEXT_ : image de l'objet
 * `effet` *TEXT* : Effet de l'objet en `.json` sous forme (TODO: à compléter) :
```json
{
	"regen_pv": int pv_a_regen,
	"regen_pv_pourcent": int pourcent_a_regen,
	"regen_mana": int mana_a_regen,
	"regen_mana_pourcent": int pourcent_a_regen,
	"boost_force": int force_a_ajouter,
	"ajout_xp": int xp_a_ajouter,
	"ajout_niveau": int niveau_a_ajouter,
	"ajout_max_pv": int pv_max_a_ajouter,
	"ajout_mana_max": int mana_max_a_ajouter,
	...
}
```

```sql
CREATE TABLE objet (
			id_objet INT PRIMARY KEY AUTO_INCREMENT,
	     	nom_objet TEXT,
		 	description_ TEXT,
		 	image_ TEXT,
			effet TEXT);
```


## TABLE `inventaire`:
 - `id_objet` *INT PRIMARY KEY AUTO_INCREMENT* : id objet
 - `id_utilisateur` _INT_ : id user
 - `quantite` _INT_ : Quantite d'un objet

```sql
CREATE TABLE inventaire (
			id_objet  INT PRIMARY KEY AUTO_INCREMENT,
	     	id_utilisateur INT,
	     	quantite INT);
```


## TABLE `monde`:
 - `id_monde` *INT PRIMARY KEY AUTO_INCREMENT*
 - `ville` _TEXT_ : nom ville
 - `region` _TEXT_ : region du monde
 - `niveau` _INT_ : niveau des villes ou region

```sql
CREATE TABLE monde (
			id_monde INT PRIMARY KEY AUTO_INCREMENT,
			ville TEXT,
	     	region TEXT,
		 	niveau INT);
```


## TABLE `quete`:
* `id` *INT PRIMARY KEY AUTO_INCREMENT* : id de la quête
* `nom` *TEXT* : Nom de la quête
* `description` *TEXT* : Description de la quête affichée au joueur
* `condition` *TEXT* : Condition de début de la quête (voir `./scripts/quete.md`)
* `objectif` *TEXT* : Objectifs pour terminer la quête (voir `./scripts/quete.md`)
* `recompense` *TEXT* : Récompenses offertes lorsqu'on finit la quête (voir `./scripts/quete.md`)

```sql
CREATE TABLE quete
(
    id_quete INT PRIMARY KEY AUTO_INCREMENT,
    nom TEXT,
    description_ TEXT,
    condition_ TEXT,
    objectif TEXT,
    recompense TEXT
);
```


## TABLE `pnj`:
 - `id_pnj` *INT PRIMARY KEY AUTO_INCREMENT* : id pnj
 - `nom_pnj` _TEXT_ : nom_pnj
 - `role_` _TEXT_ : métier d'un pnj

```sql
CREATE TABLE pnj (
			id_pnj INT PRIMARY KEY AUTO_INCREMENT,
	     	nom_pnj TEXT,
	     	role_ TEXT);
```


## TABLE `monstre`:
 - `id_monstre` *INT PRIMARY KEY AUTO_INCREMENT* : id d'un monstre
 - `nom_monstre` _TEXT_ : nom du monstre
 - `pv` _INT_ : pv du monstre
 - `armure` _INT_ : armure du monstre
 - `dgt` _INT_ : dégats infligés par le monstre

```sql
CREATE TABLE monstre (id_monstre  INT PRIMARY KEY AUTO_INCREMENT,
	     nom_monstre TEXT,
	     pv INT,
		 armure INT,
		 dgt INT);
```


## TABLE `classe`:
 - `id_classe` *INT PRIMARY KEY AUTO_INCREMENT* : id de la classe
 - `nom_classe` _TEXT_ : nom de la classe
 - `force_` _INT_ : force de base de la classe
 - `armure` _INT_ : armure de monstre
 - `dgt` _INT_ : dégats infligés par le monstre

```sql
CREATE TABLE classe (
			id_classe  INT PRIMARY KEY AUTO_INCREMENT,
	     	nom_classe TEXT,
	     	force_ INT,
		 	armure INT,
		 	dgt INT);
```


## TABLE `terrain`:
 - `id_terrain` *INT PRIMARY KEY* : id du terrain
 - `nom` TEXT : nom du terrain
 - `peut_marcher` BOOLEAN : si on peut marcher sur la case
 - `image_` TEXT : image du terrain
 - `cultivable` BOOLEAN : si l'on peut cultiver dessus
 - `objet_dessus` BOOLEAN : si il y a un objet dessus

```sql
CREATE TABLE terrain (
			id_terrain INT PRIMARY KEY,
		 	image_ TEXT,
		 	nom  TEXT,
	     	peut_marcher BOOLEAN,
		 	cultivable BOOLEAN,
		 	objet_dessus BOOLEAN);
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

```sql
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
```

## TABLE `regions_terrains`
- `id_regions_terrains` *INT PRIMARY KEY AUTO_INCREMENT* : id de la case de la region
- `id_region` _INT_ : id de la region
- `x` _INT_
- `y` _INT_
- `id_terrain` _INT DEFAULT 0_ :

```sql
CREATE TABLE regions_terrains(
	id_regions_terrains INT PRIMARY KEY AUTO_INCREMENT,
	id_region INT,
	x INT,
	y INT,
	id_terrain INT DEFAULT 0
);
```

```sql
-- A laisser, sinon, il manquera la derniere partie sql
```



