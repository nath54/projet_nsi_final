<?php


function open_json($file_path){
    if( file_exists($file_path) ){
        $texte = file_get_contents($file_path);
        $data = json_decode($texte, true);
    }
    else{
		echo("File doesn't exists : ".$file_path);
        $data=[];
    }
    return $data;
}


function load_db(){
    $file_path = $_SESSION["path_includes"]."config.json";
    $data_account = open_json($file_path);
    $pseudo = $data_account["user"];
    $password = $data_account["password"];
    $db_name = $data_account["database"];
    $port = $data_account["port"];

    try {
        $db = new PDO("mysql:host=localhost;port=".$port.";dbname=".$db_name.";charset=utf8", $pseudo, $password);
        // $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }
    catch(Exception $e) {
        die("Error : " . $e->getMessage());
    }
    return $db;
}

// function requete($db, $requested){
//     $reponse = $db->query($requested);
//     $tab = $reponse->fetchAll(PDO::FETCH_ASSOC);
//     return $tab;
// }

function requete_prep($db, $requested, $vars=array()){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $reponse = $statement->execute($vars);
    // $statement->debugDumpParams();
    // die();
    $arr = $statement->fetchAll();
    return $arr;
}

function action_prep($db, $requested, $vars=array()){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $statement->execute($vars);
}

?>