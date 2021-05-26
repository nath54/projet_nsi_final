# Format de quête :

```SQL
CREATE TABLE quete
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom TEXT,
    description_ TEXT,
    condition TEXT,
    objectif TEXT,
    recompense TEXT
)
```

# Formats de `condition`, `objectif`, `recompense`

## `condition`

Dictionnaire {str: str|list(int)} : format `.json`
```JSON

{
    "classe": "nom_classe",
    "niveau": int niveau,
    "quete": [int id_quete_1, int id_quete_2, ...]
}
{
    "classe": "chevalier",
    "niveau": 10,
    "quete": [int id_quete_1, int id_quete_2, ...]
}
```

## `objectif`

Dictionnaire {str: ???} : format `.json`
```JSON
...
```

## `recompense`
Dictionnaire {str: int|list<[int, int]>} : format `.json`
```JSON
{
    "Argent": int nb_argent,
    "XP": int nb_point_exp,
    "Objet": [[int id_obj_1, int qt], [int id_obj_2, int qt], ...]
}
```