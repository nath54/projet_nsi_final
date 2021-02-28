<?php

include_once "../includes/init.php";

$db=load_db();

?>


<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Index</title>
        <link href="../css/style.css" rel="stylesheet" />
    </head>
    <body>
        <div class="container">
            <?php include "../includes/header.php"; ?>
            <div class="column">
                <?php
                    if(test_connected()){
                        echo "<a class='bouton' href='../web/game.php'>Jouer</a>";
                    }
                    else{
                        echo "<a class='bouton' href='../web/connection.php'>Se connecter</a>'";
                        echo "<a class='bouton' href='../web/inscription.php'>S'inscrire</a>'";
                    }
                ?>
            </div>
        </div>
    </body>
</html>