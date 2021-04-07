<?php

include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

$db = load_db("../../includes/config.json");


// aller sur cette page déconnecte le potentiel utilisateur
unset($_SESSION["id_admin"]);

if(isset($_POST["pseudo"]) && isset($_POST["password"])){
    $sql = "SELECT id_admin FROM comptes_administrateurs WHERE pseudo=:pseudo AND mdp=MD5(:mdp);";
    $args = array(":pseudo"=>$_POST["pseudo"], ":mdp"=>$_POST["password"]);
    $res = requete_prep($db, $sql, $args);
    if(count($res) > 0){
        $_SESSION["id_admin"] = $res[0]["id_admin"];
        header("Location: admin_accueil.php");
    }
    else{
        alert("Le mot de passe était erroné");
    }
}

if(isset($_SESSION["error"])){
    alert($_SESSION["error"]);
    unset($_SESSION["error"]);
}


?>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Editor Connection</title>
    </head>
    <body>
        <div class="column">
            <h1>Acess to admin pages :</h1>
        </div>
        <div>
            <form method="POST" action="admin_connect.php">
                <div class="row">
                    <label>Pseudo</label>
                    <input name="pseudo" type="text" placeholder="pseudo" />
                </div>
                <div class="row">
                    <label>Password</label>
                    <input name="password" type="password" placeholder="password" />
                </div>
                <div>
                   <input type="submit" value="submit"/>
                </div>
            </form>
        </div>
    </body>
</html>