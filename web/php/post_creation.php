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

    if(!isset($_POST["tete"]) && !isset($_POST["cheveux"]) && !isset($_POST["barbe"]) && !isset($_POST["haut"]) && !isset($_POST["bas"]) && !isset($_POST["pied"]){
        $_SESSION["error"] = 'Problèmes avec le formulaire';
    }

    $sql = 'INSERT INTO utilisateurs (id_tete, id_cheveux, id_barbe, id_haut, id_bas, id_pied) VALUES(?, ?, ?, ?, ?, ?)';