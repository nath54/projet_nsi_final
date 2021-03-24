<?php

include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

$db = load_db("../../includes/config.json");

$_SESSION["player_id"] = 1;
$id_player = $_SESSION["player_id"];

// On récupère les infos du joueur :
$res = requete_prep($db, "SELECT * FROM utilisateurs WHERE id_utilisateur=?", array($id_player));
if($res == NULL || count($res) == 0){
    echo ("Les infos du joueur n'ont pas pu être chargée.");
    die();
}

$infos_players = $res[0];
$nom_player = $infos_players["pseudo"];

// On récupère l'id de la région où le joueur est
$id_region = $infos_players["region_actu"];

// On récupère des infos sur la région
$res = requete_prep($db, "SELECT * FROM regions WHERE id_region=?;", array($id_region));
if($res == NULL || count($res) == 0){
    alert("La région n'a pas pu être chargée.");
    die();
}
$infos_region = $res[0];
$nom_region = $infos_region["nom"];

// On charge les données du terrain :
$cases_terrains = array();
$res = requete_prep($db, "SELECT x, y, id_terrain FROM regions_terrains;");
if($res==NULL){
    echo("Le terrain n'a pas pu charger");
    die();
}

foreach($res as $i=>$data){
    $cases_terrains[$i] = $data;
}

// On va récuperer les infos sur les tiles

$requete = "SELECT * FROM terrain;";
$terrains = array();

$r = requete_prep($db, $requete);
if($r==NULL){
    alert("Terrain n'a pas chargé.");
}
// Pour chaque ligne, on stocke nom le nom et l'image dans l'Array $terrains
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $terrains[$data["id_terrain"]] = array("nom"=>$nom, "img"=>$img);
}


// On définit ici les infos relatives à l'affichage :

// $tx = 1280; // La taille horizontale du viewport
// $ty = 640; // La taille verticale du viewport
$tc = 64; // tc pour taille cases
$tx = 11 * $tc;
$ty = 6 * $tc;
// Il y aura donc une grille de 10x5 affichée à l'écran
$px = $infos_players["position_x"] * $tc;
$py = $infos_players["position_y"] * $tc;
// On veut que le joueur soit au centre de l'écran
$vx = ($px-$tc/2) - ($tx/2); // Où commence le viewport sur l'axe des x
$vy = ($py-$tc/2) - ($ty/2); // Où commence le viewport sur l'axe des y
$vx2 = $vx+$tx;
$vy2 = $vy+$ty;
clog($px." ".$py." ".$vx." ".$vy." ".$vx2." ".$vy2." ".$tx." ".$ty);

?>
<html>

    <head>
        <meta charset="utf-8" />
        <title>Jeu</title>
        <link href="../css/style_jeu.css" rel="stylesheet" />
    </head>

    <body onload="launch();">

        <div class="row">

            <div class="column" id="div_row_1">

                <div class="row">
                    <p>You are actually in <span id="region_name"><?php echo $nom_region; ?></span></p>
                    <hr style="color:rgba(0,0,0,0)" />
                    <p>There is <span id="region_player_number">1</span> people in this region</p>
                </div>

                <div id="div_viewport">
                    <svg viewBox="<?php echo "$vx $vy $tx $ty"; ?>" id="viewport" xmlns="http://www.w3.org/2000/svg">

                        <!-- On va construire la map -->
                        <?php
                            foreach($cases_terrains as $i=>$data){
                                $x = $data["x"] * $tc;
                                $y = $data["y"] * $tc;
                                $img = $terrains[$data["id_terrain"]]["img"];
                                echo "<image x=$x y=$y width=$tc height=$tc xlink:href=\"../../imgs/tuiles/$img\" class=\"case\"></image>";
                            }
                        ?>

                        <?php
                            $img_p = "../imgs/sprites/test6.gif";
                            echo "<g x=$px y=$py width=$tc height=$tc id=\"player\">";
                            echo "<image width=$tc height=$tc xlink:href=\"$img_p\"></image>";
                            echo "</g>";

                        ?>

                    </svg>

                </div>

            </div>

            <div class="column" id="div_row_2">
                <div id="div_account">
                    <div class="row">
                        <div class="column" id="progress_div">
                            <div id="pseudo_div">
                                <b><?php echo $nom_player; ?></b>
                            </div>
                            <div class="column">
                                <label for="progress_exp">Experience : <span id="exp_value">0/100</span></label>
                                <progress id="progress_exp" max="100" value="0"></progress>
                                <b>Niveau <span id="niveau_profil">1</span></b>
                            </div>
                            <hr />
                            <div class="column">
                                <label for="progress_vie">Vie : <span id="vie_value">100/100</span></label>
                                <progress id="progress_vie" max="100" value="100"></progress>
                            </div>
                            <div class="column">
                                <label for="progress_mana">Mana : <span id="mana_value">100/100</span></label>
                                <progress id="progress_mana" max="100" value="100"></progress>
                            </div>
                        </div>
                        <div class="column" id="pp_and_buttons">
                            <div id="image_profile">
                                <img class="profile_picture" src="../../imgs/tests/pp_null.png">
                            </div>
                            <div id="row_buttons_ui_1" class="row">
                                <button id="bag_button" onclick="change_div('div_bag');" class="button_ui_game_1"></button>
                                <button id="chat_button" onclick="change_div('div_chat');" class="button_ui_game_1"></button>
                                <button id="button_3" class="button_ui_game_1">?</button>
                            </div>
                        </div>
                    </div>

                </div>

                <div id="div_bag" style="display:none;">
                    <b>Bag :</b>
                    <table>
                        <tr>
                            <td><div id="bag_0_0" onclick="on_case_bag(0,0);" class="case_bag"></div></td>
                            <td><div id="bag_1_0" onclick="on_case_bag(1,0);" class="case_bag"></div></td>
                            <td><div id="bag_2_0" onclick="on_case_bag(2,0);" class="case_bag"></div></td>
                            <td><div id="bag_3_0" onclick="on_case_bag(3,0);" class="case_bag"></div></td>
                            <td><div id="bag_4_0" onclick="on_case_bag(4,0);" class="case_bag"></div></td>
                        </tr>
                        <tr>
                            <td><div id="bag_0_1" onclick="on_case_bag(0,1);" class="case_bag"></div></td>
                            <td><div id="bag_1_1" onclick="on_case_bag(1,1);" class="case_bag"></div></td>
                            <td><div id="bag_2_1" onclick="on_case_bag(2,1);" class="case_bag"></div></td>
                            <td><div id="bag_3_1" onclick="on_case_bag(3,1);" class="case_bag"></div></td>
                            <td><div id="bag_4_1" onclick="on_case_bag(4,1);" class="case_bag"></div></td>
                        </tr>
                        <tr>
                            <td><div id="bag_0_2" onclick="on_case_bag(0,2);" class="case_bag"></div></td>
                            <td><div id="bag_1_2" onclick="on_case_bag(1,2);" class="case_bag"></div></td>
                            <td><div id="bag_2_2" onclick="on_case_bag(2,2);" class="case_bag"></div></td>
                            <td><div id="bag_3_2" onclick="on_case_bag(3,2);" class="case_bag"></div></td>
                            <td><div id="bag_4_2" onclick="on_case_bag(4,2);" class="case_bag"></div></td>
                        </tr>
                    </table>
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
    <script src="../js/webscocket_client.js"></script>
    <script src="../js/jeu.js"></script>
    <script>

<?php
$data = open_json("../../includes/config.json");
$url_ws = $data["url_websocket"];
?>
var ws_url = "<?php echo $url_ws; ?>";

function launch(){
    start_websocket(ws_url);
}

    </script>
</html>