<?php
include "../includes/bdd.php";

$db = load_db();

?>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Editeur de map</title>
        <link href="editor.css" rel="stylesheet" />
    </head>
    <body>
        <!-- header -->
        <div>

            <div>

                <select>

                    <?php

                        // Il faudra peut-être changer les infos de la BDD
                        foreach(requete_prep($bdd, "SELECT id_region, nom_region FROM regions_map;") as $i=>$data){
                            $id = $data["id_region"];
                            $nom = $data["nom_region"];
                            echo "<option onclick='change_map($id)>$nom</option>";
                        }

                    ?>            

                </select>

            </div>


        </div>
        <!-- main -->
        <div class="row">

            <!-- map -->

            <div>
                <!-- TODO -->
            </div>

            <!-- tiles menu -->

            <div>

                <!-- TODO -->

            </div>

        </div>
    </body>
</html>