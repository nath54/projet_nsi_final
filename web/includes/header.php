<?php

include_once "../includes/init.php";

$db=load_db();

?>

<div class="header">
    <div class="row">
        <?php
            if(test_connected()){
                $pseudo = requete_prep($db, "SELECT pseudo FROM comptes WHERE id=:id", array(":id"=>$_SESSION["id_compte"]))[0][0];
                echo "<p>Connecté en tant que : $pseudo</p>";
                echo "<a class='bouton' href='../includes/disconnect.php'>Se déconnecter</a>";
            }
            else{
                echo "<a class='bouton' href='../web/connection.php'>Se connecter</a>";
            }
        ?>
    </div>
</div>