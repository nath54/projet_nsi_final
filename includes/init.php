<?php
$debug = true;
session_start();

if($debug){
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
}

/**
 * Crée une boîte de dialogue contenant `$texte`
 *
 * @param string $texte
 *      Texte devant être écrit dans la boîte de dialogue
 *
 * @return void
 *
 * @author Nathan
**/
function alert($texte){
    $texte = htmlspecialchars($texte);
    script("alert(\"$texte\");");
}

/**
 * Écrit `$texte` dans la console du navigateur
 *
 * @param string $texte
 *      Texte à écrire pour le debug
 *
 * @return void
 *
 * @author Nathan
**/
function clog($texte){
    $texte = htmlspecialchars($texte);
    script("console.log(\"$texte\");");
}


/**
 * Crée une balise script dans le code, contenant `$texte`.
 *
 * @param string $texte
 *      Instructions à exécuter.
 *
 * @return void
 *
 * @author Nathan
**/
function script($texte){
    echo "<script>$texte</script>";
}

?>