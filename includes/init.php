<?php

session_start();

if(true){
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
}

function alert($texte){
    $texte = htmlspecialchars($texte);
    script("alert(\"$texte\");");
}

function clog($texte){
    $texte = htmlspecialchars($texte);
    script("console.log(\"$texte\");");
}

function script($texte){
    echo "<script>$texte</script>";
}

?>