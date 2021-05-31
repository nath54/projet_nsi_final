<?php
include_once "../../includes/init.php";
include_once "../../includes/bdd.php";
$db = load_db("../../includes/config.json");
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Bienvenue sur Mathopia !</title>
    </head>
    <body>

    <?php

    // Si le pseudo et le mot de passe entré ne correspondent pas, on renvoie l'utilisateur à l'accueil en lui indiquant qu'il y a une erreur
    if(!isset($_POST["pseudo"]) && !isset($_POST["mdp"]))
    {
        $_SESSION["error"] = "Problème lors de la connexion !";
        header('Location: accueil.php');
    }

    // On recherche dans la bdd le pseudo entré et si le mot de passe y correspond
    $res = requete_prep($db, "SELECT * FROM utilisateurs WHERE pseudo = :pseudo AND mdp = MD5(:mdp);", array(":pseudo"=>$_POST["pseudo"], ":mdp"=>$_POST["mdp"]));

    // On laisse le joueur se connecter au jeu, si son mot de passe est bon
    if (count($res)>0)
    {
        $_SESSION["player_id"] = $res[0]["id_utilisateur"];
        header('Location: jeu.php');

        $req = requete_prep($db, "SELECT * FROM utilisateurs WHERE id_utilisateur = :id_utilisateur;", array($_SESSION["player_id"]));

        // On redirige le joueur vers le menu de création de personnage, puis on le laisse se connecter une fois son personnage personnalisé
        if($req[0]['niveau'] == 0)
        {
            header('Location: creation_perso.php');
        }
        else
        {
            header('Location: jeu.php');
        }
    }
    // Sinon on ne laisse pas le joueur se connecter
    else
    {
        $_SESSION["error"]="Pseudo ou mot de passe incorrect";
        header('Location: accueil.php');
    }
    ?>

    </body>
</html>