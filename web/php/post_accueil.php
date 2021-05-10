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

    foreach($_POST as $k=>$v){
        echo "$k = $v <br />";
    }
    if(!isset($_POST["pseudo"]) && !isset($_POST["mdp"])){
        $_SESSION["error"] = "Problème lors de la connexion !";
        header('Location: accueil.php');
    }

    $res = requete_prep($db, "SELECT * FROM utilisateurs WHERE pseudo = :pseudo AND mdp = MD5(:mdp);", array(":pseudo"=>$_POST["pseudo"], ":mdp"=>$_POST["mdp"]));
    if (count($res)>0)
    // On laisse le joueur se connecter au jeu, si son mot de passe est bon
    {
        $_SESSION["player_id"] = $res[0]["id_utilisateur"];
        header('Location: jeu.php');

        $req = requete_prep($db, "SELECT * FROM utilisateurs WHERE id_utilisateur = :id_utilisateur;", array($_SESSION["player_id"]));

        if($req[0]['niveau'] == 0)
        {
            $_SESSION["error"]=$req;
            header('Location: creation_perso.php');
        }
        else
        {
            header('Location: jeu.php');
        }
    }
    else // Sinon on ne laisse pas le joueur se connecter
    {
        $_SESSION["error"]="Pseudo ou mot de passe incorrect";
        header('Location: accueil.php');
    }
    ?>

    </body>
</html>