<?php
include_once "db.php"; // Il ne faudra pas include le fichier de base de donnée une deuxième fois
session_start(); // On lance la session ici

if(true){ // a enlever quand le projet sera fini, on peut le désactiver/activer rapidement
    // On affiche les erreurs
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
}

// Fonction pour se déconnecter, pour vider les variables de sessions et de cookies
function disconnect($redirect=false){
    $potentiels_sessions_names = ["id_compte", "token", "code_token", "erreur_inscription", "code_email"];
    foreach($potentiels_sessions_names as $i=>$nom){
        if(isset($_SESSION[$nom])){
            unset($_SESSION[$nom]);
        }
    }
    $potentiels_cookies_names = [];
    foreach($potentiels_cookies_names as $i=>$nom){
        if(isset($_COOKIE[$nom])){
            unset($_COOKIE[$nom]);
        }
    }
    // Si on veut directement rediriger vers l'index lors de la déconnexion
    if($redirect){
        header("Location: ../web/index.php");
    }
}

// fonction pour tester si un utilisateur est connecté
// a appeler au début d'un fichier php si ce fichier nécessite que l'utilisateur soit connecté
function test_connected($redirect=false){
    if(isset($_SESSION["id"]) && isset($_SESSION["key"])){
        $id = $_SESSION["id_compte"];
        $key = $_SESSION["key"];
        // on va tester la clé de connection enregistrée dans la session
        $bdd = load_db();
        $data = requete_prep($bdd, "SELECT key_connected FROM comptes WHERE id=:id", array(":id"=>$id));
        if(count($data)!=0 && $data[0]["key_connected"]==$key){
            return true;
        }
        else{
            return false;
            disconnect($redirect);
        }
    }
    else{
        // au cas où un petit $_SESSION["id"] ou un cookie qui trainerai ou autre
        disconnect($redirect);
        return false;
    }
    disconnect($redirect);
    return false;
}

// Fonction qui va générer une clé (chaine de caractères)
function gen_key($taille=16){
    // On va génerer une chaine de charactère
    $chars = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "&", "*", "_", "-");
    //
    $cle = "";
    for($x=0; $x<$taille; $x++){
        $cle .= $chars[array_rand($chars)];
    }
    return $cle;
}


?>