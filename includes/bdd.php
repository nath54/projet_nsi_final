<?php

/**
 * Ouvre un fichier .json et renvoie son contenu
 *
 * @param str $file_path
 *
 * @return Array (str, str)
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
function load_db(){
    $file_path = "config.json";
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
        die("Error: " . $e->getMessage());
    }
    return $db;
}

// function requete($db, $requested){
//     $reponse = $db->query($requested);
//     $tab = $reponse->fetchAll(PDO::FETCH_ASSOC);
//     return $tab;
// }


/**
 * Exécute une requête préparée et renvoie son résultat.
 *
 * @param PDO $db
 * @param string $requested : Requête SQL. Passer les arguments comme `?`
 * @param array $vars : Variables à passer dans la requête. 
 *
 * @return Array : Résultats de la requête
 *
 * @author Nathan
 */
function requete_prep($db, $requested, $vars=array()){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $reponse = $statement->execute($vars);
    // $statement->debugDumpParams();
    // die();
    $arr = $statement->fetchAll();
    return $arr;
}

/**
 * Exécute juste une requête préparée et renvoie si elle s'est bien passée
 *
 * @param PDO $db
 * @param string $requested : Requête SQL. Passer les arguments comme `?`
 * @param array $vars : Variables à passer dans la requête. 
 *
 * @return bool : Si l'action c'est bien passée
 *
 * @author Nathan
 */
function action_prep($db, $requested, $vars=array()){
    $statement = $db->prepare($requested, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $succeed = $statement->execute($vars);
    if($succeed){
        return true;
    }
    return false;
}