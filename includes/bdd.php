<?php

/**
 * Ouvre un fichier .json et renvoie son contenu
 *
 * @param string $file_path
 *      Chemin vers le fichier .json
 *
 * @return Array (str, str)
 *      Dictionnaire des données .json
 *
 * @author Nathan
**/
function open_json($file_path){
    if(file_exists($file_path)){
        $texte = file_get_contents($file_path);
        $data = json_decode($texte, true);
    }
    else{
		echo("File doesn't exists: " . $file_path);
        $data = [];
    }
    return $data;
}

/**
 * Charge la base de données
 *
 * @uses open_json()
 *
 * @return PDO
 *
 * @author Nathan
**/
function load_db($path="../includes/config.json"){
    $FILE_PATH = $path;
    $data_account = open_json($FILE_PATH);
    $pseudo = $data_account["user"];
    $password = $data_account["password"];
    $db_name = $data_account["database"];
    $port = $data_account["port"];

    try {
        $db = new PDO("mysql:host=localhost;port=".$port.";dbname=".$db_name.";charset=utf8", $pseudo, $password);
        // $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }
    catch(Exception $e) {
        die("Error: " . $e->getMessage());
    }
    return $db;
}

/*
function requete($db, $requested){
    $reponse = $db->query($requested);
    $tab = $reponse->fetchAll(PDO::FETCH_ASSOC);
    return $tab;
}
*/


/**
 * Exécute une requête préparée et renvoie son résultat.
 *
 * @param PDO $db
 *      Instance de la base de données
 * @param string $requested
 *      Requête SQL. Passer les arguments comme `?` ou `:arg`
 * @param array $vars
 *      Variables à passer dans la requête.
 *      Si les arguments sont passés comme `:arg`, alors format
 *      Array(":arg" => $_POST["pseudo"])
 *
 * @return Array
 *      Résultats de la requête
 *
 * @author Nathan
**/
function requete_prep($db, $requested, $vars=array(), $debug=false){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $reponse = $statement->execute($vars);
    if($debug){
        $statement->debugDumpParams();
    }
    $arr = $statement->fetchAll();
    return $arr;
}

/**
 * Exécute une requête préparée et renvoie si elle s'est bien passée
 *
 * @param PDO $db
 *      Instance de la base de données
 * @param string $requested
 *      Requête SQL. Passer les arguments comme `?`
 * @param array $vars
 *      Variables à passer dans la requête.
 *
 * @return bool
 *      true si l'action a bien été réussie, false sinon
 *
 * @author Nathan
**/
function action_prep($db, $requested, $vars=array(), $debug=false){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $succeed = $statement->execute($vars);
    if($debug){
        $statement->debugDumpParams();
        echo $statement->errorCode();
        print_r($statement->errorInfo());
    }
    return $succeed;
}

