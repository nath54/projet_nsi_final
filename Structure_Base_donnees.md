# Projet_classe :

## TABLE `utilisateurs`:
 - `id_utilisateur` *INT PRIMARY KEY AUTO_INCREMENT* : id user
 - `pseudo` _TEXT_ : pseudo
 - `mdp` _TEXT_ : mdp du user
 - `sexe` _TEXT_ : Détermine le sexe du personnage
 - `vie` _INT_ : vie actuelle du joueur
 - `stamina` _INT_ : Stamina actuelle du joueur
 - `mana` _INT_ : Mana actuelle du joueur
 - `armor` _INT_ : Armure du joueur
 - `classe` _TEXT_ : classe du joueur
 - `niveau` _INT_ : niveau du joueur
 - `argent` _INT_ : argent du joueur
 - `experience` _INT_ : expérience du joueur
 - `experience_tot` _INT_ : expérience a atteindre du joueur pour qu'il passe au niveau suivant
 - `competence` _TEXT_ : qualité du personnage
 - `quetes` _TEXT_ : les quetes réalisée par le joueur
 - `region_actu` _INT DEFAULT 1_ : id de la région où le joueur est
 - `position_x` _INT_ : case/position x où le joueur est
 - `position_y` _INT_ : case/position y où le joueur est
 - `id_tete` _INT_ : id de la tête pour le personnalisation
 - `id_cheveux` _INT_ : id des cheveux pour la personnalisation
 - `id_barbe` _INT_ : id de la barbe pour la personnalisation
 - `id_haut` _INT_ : id du haut du corps pour la perso
 - `id_bas` _INT_ : id des jambes pour la perso
 - `id_pieds` _INT_ : id des pieds pour la perso


```sql
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
 argent INT,
 experience INT,
 experience_tot INT,
 competence TEXT,
 quetes TEXT,
 region_actu INT DEFAULT 1,
 position_x INT,
 position_y INT,
 id_tete INT,
 id_cheveux INT,
 id_barbe INT,
 id_haut INT,
 id_bas INT,
 id_pieds INT);
```
## TABLE 'personnalisation':
 - `id_tete` _INT_ : id de la tête pour le personnalisation
 - `img_tete` _TEXT_ : image de la tete
 - `id_cheveux` _INT_ : id des cheveux pour la personnalisation
 - `img_cheveux` _TEXT_ : image des cheveux
 - `id_barbe` _INT_ : id de la barbe pour la personnalisation
 - `img_barbe` : image de la barbe
 - `id_haut` _INT_ : id du haut du corps pour la perso
 - `img_haut` _TEXT_ : image du haut
 - `id_bas` _INT_ : id des jambes pour la perso
 - `img_bas` _TEXT_ : image du bas
 - `id_pieds` _INT_ : id des pieds pour la perso
 - `img_pieds` _TEXT_ : image des pieds

 ```sql
CREATE TABLE personnalisation (
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
 - `niveau` _INT_ : niveau du monstre
 - `pv` _INT_ : pv du monstre
 - `armure` _INT_ : armure du monstre
 - `dgt` _INT_ : dégats infligés par le monstre
 - `loot` _TEXT_ : ce que va lacher le monstre en mourrant
 - `id_region` _INT_ : région dans laquelle le monstre se situe
 - `position_x` _INT_ : case x où le monstre est
 - `position_y` _INT_ : case y où le monstre est

```sql
CREATE TABLE monstre (id_monstre  INT PRIMARY KEY AUTO_INCREMENT,
	     nom_monstre TEXT,
		 niveau INT,
	     pv INT,
		 armure INT,
		 dgt INT,
		 loot TEXT,
		 id_region INT,
		 position_x INT,
		 position_y INT);
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
 - `nom` _TEXT_ : nom du terrain
 - `peut_marcher` _BOOLEAN_ : si on peut marcher sur la case
 - `image_` _TEXT_ : image du terrain
 - `cultivable` _BOOLEAN_ : si l'on peut cultiver dessus
 - `objet_dessus` _BOOLEAN_ : si il y a un objet dessus

```sql
CREATE TABLE terrain (
			id_terrain INT PRIMARY KEY,
		 	image_ TEXT,
		 	nom  TEXT,
	     	peut_marcher BOOLEAN,
		 	cultivable BOOLEAN,
		 	objet_dessus BOOLEAN);
```


## TABLE `objets`:
 - `id_objet` *INT PRIMARY KEY* : id du terrain
 - `nom` _TEXT_ : nom du terrain
 - `image_` _TEXT_ : image du terrain
 - `z_index` _INT DEFAULT 1_ : pour qu'on puisse avoir des objets au dessus et en dessous du joueur
 - `collision` _BOOLEAN_ : S'il y a des collisions avec, si 1, le joueur ne peut pas aller sur la case

`Le terrain sera en z_index 0`
`Les objets de base seront en z_index 1`
`Les persos et les ennemis seront en z_index 2`
`Les objets au dessus du perso seront en z_index 3 (exemple : buisson)`

```sql
CREATE TABLE objets (
			id_objet INT PRIMARY KEY,
		 	nom  TEXT,
		 	image_ TEXT,
			z_index INT,
		 	collision BOOLEAN);
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
- `id_region` _INT_ : id de la region
- `x` _INT NOT NULL_ : clé composée x_y
- `y` _INT NOT NULL_ : clé composée x_y
- `id_terrain` _INT DEFAULT 0_ :

```sql
CREATE TABLE regions_terrains(
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_terrain INT DEFAULT 0,
	CONSTRAINT comp_key_x_y PRIMARY KEY (x, y, id_region)
);

CREATE INDEX `index_id_region` ON `regions_terrains` (`id_region`);

```


## TABLE `regions_objets`
- `id_region` _INT_ : id de la region
- `x` _INT NOT NULL_ : clé composée x_y
- `y` _INT NOT NULL_ : clé composée x_y
- `id_objet` _INT DEFAULT 0_ :


```sql
CREATE TABLE regions_objets(
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_objet INT DEFAULT 0,
	CONSTRAINT comp_key_x_y PRIMARY KEY (x, y, id_region)
);

CREATE INDEX `index_id_region` ON `regions_objets` (`id_region`);

```



## TABLE `comptes_administrateurs`
- `id_admin` _INT PRIMARY KEY AUTO_INCREMENT_ : id de l'admin
- `pseudo` _TEXT NOT NULL_
- `mdp` _TEXT NOT NULL_

```sql

CREATE TABLE comptes_administrateurs (
	id_admin INT PRIMARY KEY AUTO_INCREMENT,
	pseudo TEXT NOT NULL,
	mdp TEXT NOT NULL
);

```


```sql
-- A laisser, sinon, il manquera la derniere partie sql pour le programme python
```



