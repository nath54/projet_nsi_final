# Projet de la classe NSI

## Installation du projet
### Installation rapide
1. Cloner le [repository GitHub](git@github.com:nath54/projet_nsi_final)
2. Exécuter le code suivant dans un terminal SQL :
```SQL
CREATE DATABASE `projetclasse`;
CREATE USER `projetclasse`@`%` IDENTIFIED BY 'proj#17CLASSE';
GRANT ALL PRIVILEGES ON `projetclasse`.* TO `projetclasse`@`%`;
USE `projetclasse`;
```
3. Ensuite, exécutez `/Structure_Base_donnees.sql`, dans votre terminal SQL dans la base de données `projetclasse`.
4. Exécutez `/rempli_bdd.sql`, dans votre terminal SQL dans la base de données `projetclasse`.


### Installation manuelle
1. Cloner le [repository GitHub](https://github.com/nath54/projet_nsi_final.git)

```sh
git clone git@github.com:nath54/projet_nsi_final.git
```

> Les variables écrites comme `ceci` peuvent être changée. Dans ce cas, veuillez les modifier dans le fichier `/scripts/config.json`
2. Créer une base de données `projetclasse`
3. Créer un utilisateur `projetclasse`, avec pour mot de passe `proj#17CLASSE`
4. Utilisez la base de données `projetclasse`
5. Ensuite, exécutez les scripts `/Structure_Base_donnees.sql`, puis `/rempli_bdd.sql`.

