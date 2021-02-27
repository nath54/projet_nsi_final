<?php

// Fonction pour ouvrir un fichier json, et qui retourne un array en sortie
// Fonction utilisée dans load_db();
function open_json($file_path, $debug=false){
    if( file_exists($file_path) ){
        $texte = file_get_contents($file_path);
        $data = json_decode($texte, true);
    }
    else{
		if($debug){
            echo("File doesn't exists : ".$file_path);
        }
        $data=array();
    }
    return $data;
}

// Fonction pour récuperer la base de donnée
function load_db(){
    $file_path = "../includes/config.json"; // Le chemin vers le fichier de configuration
    $data_account = open_json($file_path); // On récupère les données
    $user = $data_account["user"]; // Le nom du compte qui a accès à la base de donnée
    $password = $data_account["password"]; // Le mot de passe du compte qui à accès à la base de donnée
    $db_name = $data_account["database"]; // Le nom de la base de donnée
    $port = $data_account["port"]; // Le port utilisé par le gestionnaire de base de donnée

    try {
        $db = new PDO("mysql:host=localhost;port=".$port.";dbname=".$db_name.";charset=utf8", $user, $password);
        // $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }
    catch(Exception $e) {
        die("Error : " . $e->getMessage());
    }
    return $db;
}

// Fonction pour faire plus facilement des requêtes préparées
// Rappel : Pour faire une requêtes préparée, ce cera sous la forme
//  $requested = "SELECT * FROM comptes WHERE id=:id", et $vars = array(":id"=>$id_du_compte)
function requete_prep($db, $requested, $vars=array()){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $reponse = $statement->execute($vars);
    // $statement->debugDumpParams(); // Pour débugger
    // die();
    $arr = $statement->fetchAll();
    return $arr;
}

// Fonction pour faire plus facilement des actions préparées
// Rappel : Pour faire une action préparée, ce cera sous la forme
//  $action = "INSERT INTO comptes SET nom=:nom, email=:email", et $vars = array(":nom"=>$nom, ":email"=>$email)
// Cette fonction renvoie s'il y a eu une erreur ou pas
function action_prep($db, $action, $vars=array()){
    $statement = $db->prepare($action, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $succeed = $statement->execute($vars);
    return $succeed;
}

?>