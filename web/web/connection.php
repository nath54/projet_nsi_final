<!DOCTYPE html>
<?php

include_once "../includes/init.php";

// On va générer un petit token, pour vérifier que la requête provient bien de cette page là
// PS : On va aussi brouiller les pistes pour un éventuel hacker
$token = gen_key();
$_SESSION["token"] = $token;
$_SESSION["code_token"] = gen_key();

if(isset($_SESSION["erreur_connection"])){
    echo "<script>alert(\"".$_SESSION["erreur_connection"]."\");</script>";
    unset($_SESSION["erreur_connection"]);
}

?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Connection</title>
        <link href="../css/style.css" rel="stylesheet" />
    </head>
    <body>
        <div class="container">
            <form action="../includes/connection.php" method="POST">
                <!-- Titre -->
                <div>
                    <h1>Connection :</h1>
                </div>
                <!-- Pseudo / Email -->
                <div>
                    <label>Pseudo / Email : </label>
                    <input type="text" name="pseudo_email" />
                </div>
                <!-- Mot de Passe -->
                <div>
                    <label>Password : </label>
                    <input type="password" name="password" />
                </div>
                <!-- Bouton -->
                <div>
                    <input type="submit" value="Ok" class="bouton_form" />
                </div>
                <div>
                    <p>Vous n'avez pas de comptes ? <a href="../web/inscription.php">Inscrivez vous!</a></p>
                </div>
            </form>
        </div>
    </body>
</html>