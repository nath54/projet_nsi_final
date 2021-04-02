<?php 
include_once "../../includes/init.php";
include_once "../../includes/bdd.php";
$db = load_db("../../includes/config.json");
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Bienvenue sur Maths Quest !</title>
    </head>
    <body>
    
        <?php
        
    foreach($_POST as $k=>$v){
        echo "$k = $v <br />";
    }
    if(!isset($_POST["pseudo"]) && !isset($_POST["mdp"])){
        $_SESSION["error"] = "probleme lors de la connexion !";
        header('Location: accueil.php');
    }
    
    $res = requete_prep($db, "SELECT * FROM utilisateurs WHERE pseudo = :pseudo AND mdp = MD5(:mdp);", array(":pseudo"=>$_POST["pseudo"], ":mdp"=>$_POST["mdp"]));
    if (count($res)>0)
    // On laisse le joueur se connecter au jeu, si son mot de passe est bon
    {
        $_SESSION["player_id"] = $res[0]["id_utilisateur"];
        header('Location: jeu.php');

    }
    else // Sinon on ne laisse pas le joueur se connecter
    {
        $_SESSION["error"]="Probleme de connexion";
        header('Location: accueil.php');
    }
    ?>
    
        
    </body>
</html>