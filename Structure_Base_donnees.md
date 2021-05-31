# Projet_classe :

## TABLE `utilisateurs`:
 - `id_utilisateur` *INT PRIMARY KEY AUTO_INCREMENT* : id user
 - `pseudo` _TEXT_ : pseudo
 - `mdp` _TEXT_ : mdp du user
 - `sexe` _TEXT_ : Détermine le sexe du personnage
 - `vie` _INT DEFAULT 100_ : vie actuelle du joueur
 - `stamina` _INT DEFAULT 100_ : Stamina actuelle du joueur
 - `mana` _INT DEFAULT 100_ : Mana actuelle du joueur
 - `armor` _INT DEFAULT 0_ : Armure du joueur
 - `classe` _TEXT_ : classe du joueur
 - `niveau` _INT DEFAULT 1_ : niveau du joueur
 - `argent` _INT DEFAULT 0_ : argent du joueur
 - `experience` _INT DEFAULT 0_ : expérience du joueur
 - `experience_tot` _INT DEFAULT 100_ : expérience a atteindre du joueur pour qu'il passe au niveau suivant
 - `competence` _TEXT_ : qualité du personnage
 - `quetes` _TEXT_ : les quetes réalisée par le joueur
 - `region_actu` _INT DEFAULT 1_ : id de la région où le joueur est
 - `position_x` _INT DEFAULT 1_ : case/position x où le joueur est
 - `position_y` _INT DEFAULT 1_ : case/position y où le joueur est
 - `id_tete` _INT DEFAULT 1_ : id de la tête pour le personnalisation
 - `id_cheveux` _INT DEFAULT 1_ : id des cheveux pour la personnalisation
 - `id_barbe` _INT DEFAULT 1_ : id de la barbe pour la personnalisation
 - `id_haut` _INT DEFAULT 1_ : id du haut du corps pour la perso
 - `id_bas` _INT DEFAULT 1_ : id des jambes pour la perso
 - `id_pieds` _INT DEFAULT 1_ : id des pieds pour la perso


```sql

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
```

## TABLE `tokens`:
 - `id_utilisateur` _INT PRIMARY KEY_
 - `token` _TEXT NOT NULL_

```sql
CREATE TABLE tokens (
	id_utilisateur INT PRIMARY KEY,
	token TEXT NOT NULL
);
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

```json
CREATE TABLE objet (
	id_objet INT PRIMARY KEY AUTO_INCREMENT,
 	nom_objet TEXT,
 	description_ TEXT,
 	image_ TEXT,
	effet TEXT
);
```


## TABLE `inventaire`:
 - `id_objet` *INT PRIMARY KEY AUTO_INCREMENT* : id objet
 - `id_utilisateur` _INT_ : id user
 - `quantite` _INT_ : Quantite d'un objet

```sql
CREATE TABLE inventaire (
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_objet INT NOT NULL,
	id_utilisateur INT NOT NULL,
 	quantite INT NOT NULL DEFAULT 1
);
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
 	niveau INT
);
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
 	role_ TEXT
);
```


## TABLE `monstre`:
 - `id_monstre` *INT PRIMARY KEY* : id d'un monstre, il n'est pas en auto-increment parce que comme ca, ce sera plus simple de controller
 - `nom` _TEXT_ : nom du monstre
 - `niveau` _INT_ : niveau du monstre (le plus simple sera de faire plusieurs mêmes monstres de niveaux différents)
 - `pv` _TEXT_ : dict json décrivant les pv du monstre
				 exemple : {"forme": "random between", "values": [1,5]}
				 exemple : {"forme": "random expr between", "expr":"5x", "values": [1,5]}
				 exemple : {"forme": "value", "value": 1}
 - `dgt` _TEXT_ : dict json dégats infligés par le monstre
				 exemple : {"forme": "random between", "values": [1,5]}
				 exemple : {"forme": "random expr between", "expr":"5x", "values": [1,5]}
				 exemple : {"forme": "value", "value": 1}
 - `loot` _TEXT_ : liste json ce que va lacher le monstre en mourrant
 - `img_base` _TEXT NOT NULL_ : chemin vers l'image de base du monstre
 - `img_mort` _TEXT NOT NULL DEFAULT "tombe.png"_ : chemin vers l'image de mort du monstre
 - `temps_bouger` _INT NOT NULL DEFAULT 0.8_ :
 - `rayon_detect` _INT NOT NULL DEFAULT 3
 - `rayon_perdu` _INT NOT NULL DEFAULT 6
 - `portee_attaque` _INT NOT NULL DEFAULT 1_
 - `agressif` _BOOLEAN NOT NULL DEFAULT 1_
 - `pacifique` _BOOLEAN NOT NULL DEFAULT 1_

```sql
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
 	dgt INT
);
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
 	objet_dessus BOOLEAN
);
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
 	collision BOOLEAN
);
```

## TABLE `regions`
 - `id_region` *INT PRIMARY KEY AUTO_INCREMENT* : id de la region
 - `nom` _TEXT_ : nom de la region
 - `description_` _TEXT_ : une petite description de la région

```sql
CREATE TABLE regions(
	id_region INT PRIMARY KEY AUTO_INCREMENT,
	nom TEXT NOT NULL,
	description_ TEXT
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
- `parametres` _TEXT NOT NULL DEFAULT '{}'_ : les parametres d'un objet sous la forme d'un dictionnaire json


```sql
CREATE TABLE regions_objets(
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_objet INT DEFAULT 0,
	parametres TEXT NOT NULL DEFAULT '{}',
	CONSTRAINT comp_key_x_y PRIMARY KEY (x, y, id_region)
);

CREATE INDEX `index_id_region` ON `regions_objets` (`id_region`);

```

## TABLE `regions_monstres`
- `id_monstre_spawn` *INT PRIMARY KEY AUTO_INCREMENT* : id du monstre
- `id_region` _INT_ : id de la region
- `x` _INT NOT NULL_ : clé composée x_y
- `y` _INT NOT NULL_ : clé composée x_y
- `id_objet` _INT DEFAULT 0_ :


```sql
CREATE TABLE regions_monstres(
	id_monstre_spawn INT PRIMARY KEY AUTO_INCREMENT,
	x INT NOT NULL,
	y INT NOT NULL,
	id_region INT NOT NULL,
	id_monstre INT DEFAULT 0
);

CREATE INDEX `index_id_region` ON `regions_monstres` (`id_region`);
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

## TABLE `arme`:
 - `id_arme` *INT PRIMARY KEY AUTO_INCREMENT*
 - `nom` _TEXT_ : nom de l'objet
 - `classe` _TEXT_ : classe à laquelle l'arme appartient
 - `dgt` _INT_ : les dégats de l'arme
 - `niveau` _INT_ : niveau de l'arme
 - `style` _TEXT_ : Corps à corps ou distance
 - `portee` _INT_ : Portée d'une arme
 - `munition` _TEXT_ : les munitions que posséde le joueur
 - `quantite_mun` _INT_ : Le nombre de munitions que posséde le joueur
 - `img_arme` _TEXT_ : Chemin vers l'image de l'arme

```sql
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
```

## TABLE competences
 - `id_competence` _INT PRIMARY KEY_ : id de la compétence
 - `nom` _TEXT NOT NULL_ : nom de la compétence
 - `description` _TEXT_ : description de la compétence
 - `type_cible` _TEXT NOT NULL_ : le type de la cible (`ennemi`,`objet`,`terrain`)
 - `cout_mana` _INT NOT NULL_ : le coût en mana de la compétence
 - `tp_recharge` _FLOAT NOT NULL_ : le temps de recharge en secondes de la compétence
 - `img_icon` _TEXT NOT NULL_ : Le nom du fichier de l'icone de la compétence
 - `niv_min` _INT NOT NULL DEFAULT 1

Les effets de la compétence seront codés directement dans le serveur

```sql
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
```

## TABLE `classes_competences`

- `id` INT NOT NULL PRIMARY_KEY AUTO_INCREMENT
- `id_competence` INT NOT NULL
- `nom_classe` TEXT NOT NULL

```sql
CREATE TABLE classes_competences (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_competence INT NOT NULL,
	nom_classe TEXT NOT NULL
);
```

```sql
-- A laisser, sinon, il manquera la derniere partie sql pour le programme python
```
