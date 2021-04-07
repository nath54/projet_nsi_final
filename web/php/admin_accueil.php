<?php


include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

// TODO:
// Pour l'instant, on va rester simple
// après, on pourra utiliser des tokens, des clés des sessions etc...
// Pour l'instant, juste admin
// Par contre, il faudra aussi veiller a ce que le compte ne reste pas trop inactif.
if(!isset($_SESSION["id_admin"])){
    $_SESSION["error"]="Vous n'êtes pas connecté en tant qu'administrateur !";
    header("Location: admin_connect.php");
    die();
}

?>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Admin accueil</title>
    </head>

    <body>

        <h1>Admin Accueil : </h1>

        <p>Vous avez ici accès aux outils administrateurs, </p>

        <ul>
            <li><a href="editor.php">Editeur de map</a></li>
        </ul>

        <a href="admin_connect.php">Se déconnecter</a>

    </body>

</html>