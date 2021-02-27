# Initialisation de la base de donnée

## Créer la base de donnée

La première chose à faire lorsque l'on veut tester ce projet, c'est de créer la base de donnée dans son gestionnaire de base de donnée.
Vous pouvez l'appeler comme vous voulez, mais il faudra que vous guardiez ce nom pour les fichiers de configuration.

depuis un terminal sql, cela donnera :

```sql
CREATE DATABASE `le nom de la base de donnée`;
```

Si vous utilisez phpmyadmin, vous pouvez lorsque vous créez un compte et lui assigner directement une base de de donnée du même nom avec tous les droits dessus.

## Créer un utilisateur qui a accès à la base de donnée

Il faudra ensuite créer un utilisateur et lui donner tous les droits à la base de donnée que créée précedemment.


# Structure de la base de donnée

## Table `comptes` :
 - `id` *INT PRIMARY KEY AUTO_INCREMENT* : id du compte
 - `pseudo` _TEXT UNIQUE NOT NULL_ : pseudo du compte
 - `email` _TEXT UNIQUE NOT NULL_ : email du compte
 - `password_` _TEXT UNIQUE NOT NULL_ : mot de passe du compte (**chiffré avec MD5()**)
 - `valid` _TINYINT DEFAULT 0 NOT NULL_ : si l'email du compte a été validé
 - `key_connected` _TEXT DEFAULT NULL_ : la clé de connexion du compte quand il se connecte
