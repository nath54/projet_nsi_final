<?php

include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

$db = load_db("../../includes/config.json");

$_SESSION["player_id"] = 1;
$id_player = $_SESSION["player_id"];

// On récupère les infos du joueur :
$res = requete_prep($db, "SELECT * FROM utilisateurs WHERE id_utilisateur=:id", array(":id", $id_player));
if($res==NULL || count($res)!=1){
    alert("il y a eu une erreur !");
    die();
}

$infos_players = $res[0];

// On récupère l'id de la région où le joueur est
$id_region = $infos_players["region_actu"];

// On charge les données du terrain :
$cases_terrains = array();
$res = requete_prep($db, "SELECT (x,y,id_terrain) FROM regions_terrains");
if($res==NULL){
    alert("Il y a eu une erreur!");
    die();
}

foreach($res as $i=>$data){
    $cases_terrains[$i]=$data;
}

// On va récuperer les infos sur les tiles

$requete = "SELECT * FROM terrain;";
$terrains = array();

$r = requete_prep($db, $requete);
if($r==NULL){
    alert("Il y a eu une erreur !");
}
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $terrains[$data["id_terrain"]] = array("nom"=>$nom, "img"=>$img);
}


// On définit ici les infos relatives à l'affichage :

$tx = 1280; // La taille horizontale du viewport
$ty = 640; // La taille verticale du viewport
$tc = 128; // tc pour taille cases
// Il y aura donc une grille de 10x5 affichée à l'écran
$px = $infos_players["position_x"];
$py = $infos_players["position_y"];
// On veut que le joueur soit au centre de l'écran
$vx = $px - $tx/2; // Où commence le viewport sur l'axe des x
$vy = $py - $ty/2; // Où commence le viewport sur l'axe des y

?>
<html>

    <head>
        <meta charset="utf-8" />
        <title>Jeu</title>
        <link href="../css/style_jeu.css" rel="stylesheet" />
    </head>

    <body>

        <div class="row">

            <div class="column" id="div_row_1">

                <div class="row">
                    <p>You are actually in <span id="region_name">(Region Name)</span></p>
                    <hr style="color:rgba(0,0,0,0)" />
                    <p>There is <span id="region_player_number">1</span> people in this region</p>
                </div>

                <div id="div_viewport">

                    <svg viewBox="<?php echo $vx." ".$vy." ".$vx+$tx." ".$vy+$ty; ?>" id="viewport" xmlns="http://www.w3.org/2000/svg">

                        <!-- On va construire la map -->
                        <?php
                            foreach($cases_terrains as $i=>$data){
                                $x = $data["x"] * $tc;
                                $y = $data["y"] * $tc;
                                $img = $terrains[$data["id_terrain"]]["image"];
                                echo "<image x=$x y=$y width=$tc height=$tc xlink:href=\"../../imgs/tuiles/$img\" class=\"case\"></image>";
                            }
                        ?>

                    </svg>

                </div>

            </div>

            <div class="column" id="div_row_2">
                <div id="div_account">
                    <div class="row">
                        <div class="column" id="progress_div">
                            <div id="pseudo_div">
                                <b>Pseudo</b>
                            </div>
                            <div class="column">
                                <label for="progress_exp">Experience : <span id="exp_value">20/100</span></label>
                                <progress id="progress_exp" max="100" value="20"></progress>
                                <b>Niveau <span id="niveau_profil">1</span></b>
                            </div>
                            <hr />
                            <div class="column">
                                <label for="progress_vie">Vie : <span id="vie_value">70/100</span></label>
                                <progress id="progress_vie" max="100" value="70"></progress>
                            </div>
                            <div class="column">
                                <label for="progress_mana">Mana : <span id="mana_value">70/100</span></label>
                                <progress id="progress_mana" max="100" value="70"></progress>
                            </div>
                        </div>
                        <div class="column" id="pp_and_buttons">
                            <div id="image_profile">
                                <img class="profile_picture" src="../../imgs/tests/pp_null.png">
                            </div>
                            <div id="row_buttons_ui_1" class="row">
                                <button id="bag_button" class="button_ui_game_1"></button>
                                <button id="button_2" class="button_ui_game_1">?</button>
                                <button id="button_3" class="button_ui_game_1">?</button>
                            </div>
                        </div>
                    </div>

                </div>

                <div id="div_chat">
                    <b>Chat :</b>
                    <div id="chat_mess">
                        <p><b class="cl_chat_system">Système : </b>Bienvenue dans le jeu !</p>
                    </div>
                    <div>
                        <input id="input_chat" type="text" placeholder="Message à envoyer">
                        <button>Envoyer</button>
                    </div>
                </div>

            </div>

        </div>

    </body>

</html>