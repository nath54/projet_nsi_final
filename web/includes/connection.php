<?php

include_once "../includes/init.php";

if(!(isset($_SESSION["token"]) && isset($_SESSION["code_token"]) && isset($_POST[$_SESSION["code_token"]]) && $_SESSION["token"]==$_POST[$_SESSION["code_token"]])){
    disconnect(true);
}

$db = load_db();

if(!isset($_SESSION["pseudo_email"]) || !isset($_SESSION["password"])){
    disconnect(true);
}

$pseudo_email = $_POST["pseudo_email"];
$password = $_POST["password"];

$requested = "SELECT id_compte FROM comptes WHERE (pseudo=:pseudo_email OR email=:pseudo_email) AND password_=MD5(:password_)";
$vars = array(":pseudo_email"=>$pseudo_email, ":password_"=>$password);
$result = requete_prep($db, $requested, $vars);

// Si aucuns compte n'a le pseudo/email et le mot de passe demandé :
if(count($result)==0){
    disconnect();
    $_SESSION["erreur_connexion"] = "Le pseudo/email est faux ou le mot de passe est faux";
    header("Location: ../web/connection.php");
}

$id_compte = $result[0][0];
$key = gen_key();
$_SESSION["key_connected"] = $key;
$action = "UPDATE comptes SET key_connected=:key_connected WHERE id=:id_compte";
$vars = array(":id_compte"=>$_SESSION["id_compte"],
              ":key_connected"=>$key);
header("../web/index.php");

?>