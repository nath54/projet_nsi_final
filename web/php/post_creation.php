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


        if(!isset($_POST["tete"]) || !isset($_POST["cheveux"]) || !isset($_POST["barbe"]) || !isset($_POST["haut"]) || !isset($_POST["bas"]) || !isset($_POST["pied"])) {
            $_SESSION["error"] = 'Problèmes pas rempli en entier';
        // On regarde si les skins sélectionnés sont bien au nombre indiqué
        }
        else   if(! in_array($_POST["tete"],["1","2","3"])){
            $_SESSION["error"] = "Valeur invalide";
        }
        else   if(! in_array($_POST["cheveux"],["1","2","3"])){
            $_SESSION["error"] = "Valeur invalide";
        }
        else   if(! in_array($_POST["barbe"],["1","2","3"])){
            $_SESSION["error"] = "Valeur invalide";
        }
        else   if(! in_array($_POST["haut"],["1","2","3","4"])){
            $_SESSION["error"] = "Valeur invalide";
        }
        else   if(! in_array($_POST["bas"],["1","2","3"])){
            $_SESSION["error"] = "Valeur invalide";
        }
        else   if(! in_array($_POST["pied"],["1","2","3"])){
            $_SESSION["error"] = "Valeur invalide";
        }

        // Si tout se passe bien on update la bdd et on enregistre les valeurs sélectionnés 
        else {
            $req = requete_prep($db, "UPDATE utilisateurs SET id_tete = :id_tete , id_cheveux = :id_cheveux , id_barbe = :id_barbe ,id_haut = :id_haut ,id_bas = :id_bas , id_pieds = :id_pied , niveau = 1 WHERE id_utilisateur = :player_id;", array(':id_tete' => intval ($_POST["tete"]), 'id_cheveux' => intval($_POST["cheveux"]), ':id_barbe' => intval($_POST["barbe"]), ':id_haut' => intval($_POST["haut"]), ':id_bas' => intval($_POST["bas"]), ':id_pied' => intval($_POST["pied"]), ':player_id' => intval($_SESSION['player_id'])), $debug=true);
            header('Location: jeu.php');
        }
        //print_r($_POST);

    ?>

    </body>
</html>