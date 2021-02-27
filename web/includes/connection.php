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




?>