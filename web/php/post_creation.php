<?php 
include_once "../../includes/init.php";
include_once "../../includes/bdd.php";
$db = load_db("../../includes/config.json");
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Vérification perso</title>
    </head>
    <body>
    
    <?php

    if(!isset($_POST["tete"]) && !isset($_POST["cheveux"]) && !isset($_POST["barbe"]) && !isset($_POST["haut"]) && !isset($_POST["bas"]) && !isset($_POST["pied"])) {
        $_SESSION["error"] = 'Problèmes pas rempli en entier';
    }
    else   if(! in_array($_POST["tete"],["1","2","3","4","5","6"])){
        $_SESSION["error"] = "Valeur invalide";
    }
    else   if(! in_array($_POST["cheveux"],["1","2","3","4","5","6"])){
        $_SESSION["error"] = "Valeur invalide";
    }
    else   if(! in_array($_POST["barbe"],["1","2","3","4","5","6"])){
        $_SESSION["error"] = "Valeur invalide";
    }
    else   if(! in_array($_POST["haut"],["1","2","3","4","5","6"])){
        $_SESSION["error"] = "Valeur invalide";
    }
    else   if(! in_array($_POST["bas"],["1","2","3","4","5","6"])){
        $_SESSION["error"] = "Valeur invalide";
    }
    else   if(! in_array($_POST["pied"],["1","2","3","4","5","6"])){
        $_SESSION["error"] = "Valeur invalide";
    }

    else {
        $req = requete_prep($db, "SELECT * FROM utilisateurs WHERE id_utilisateur = :id_utilisateur;", array($_POST["tete"], $_POST["cheveux"], $_POST["barbe"], $_POST["haut"], $_POST["bas"], $_POST["pied"]));
        header('Location : jeu.php');
    }

    ?>

    </body>
</html>