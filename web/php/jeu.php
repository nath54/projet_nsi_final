<?php

include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

$db = load_db("../../includes/config.json");

if(!isset($_SESSION["player_id"])){
    $_SESSION["error"] = "Vous n'êtes pas connecté !";
    header("Location: accueil.php");
    die();
}
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
$res = requete_prep($db, "SELECT x, y, id_terrain FROM regions_terrains WHERE id_region=:idr;", array(":idr"=>$id_region));
if($res==NULL){
    echo("Le terrain n'a pas pu charger");
    die();
}
foreach($res as $i=>$data){
    $cases_terrains[$i] = $data;
}
// On charge les données du terrain :
$cases_objets = array();
$res = requete_prep($db, "SELECT x, y, id_objet FROM regions_objets WHERE id_region=:idr;", array(":idr"=>$id_region));
if($res==NULL){
    echo("L'objet n'a pas pu charger");
    die();
}
foreach($res as $i=>$data){
    $cases_objets[$i] = $data;
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

$requete = "SELECT * FROM objets;";
$objets = array();
$r = requete_prep($db, $requete);
if($r==NULL){
    alert("Objet n'a pas chargé.");
}
// Pour chaque ligne, on stocke nom le nom et l'image dans l'Array $terrains
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $objets[$data["id_objet"]] = array("nom"=>$nom, "img"=>$img, "z_index"=>$data["z_index"]);
}


// On définit ici les infos relatives à l'affichage :

// $tx = 1280; // La taille horizontale du viewport
// $ty = 640; // La taille verticale du viewport
$tc = 64; // tc pour taille cases
$tx = 18 * $tc;
$ty = 10 * $tc;
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

        <div>
            <div id="ui">
                <div class="box full">
                    <div class="row_center">

                        <!-- VIES  -->
                        <div class="column progress_bars">
                            <div>
                                <progress id="progress_vie" max="100" value="300"></progress>
                                <span class="above_text" id="text_vie">100/100</span>
                            </div>
                            <div>
                                <progress id="progress_mana" max="100" value="300"></progress>
                                <span class="above_text" id="text_mana">100/100</span>
                            </div>
                        </div>

                    </div>

                    <div class="column_end full">

                        <div class="row_center">
                            <hr style="visibility:hidden;" />

                            <div>
                                <table>
                                    <tr>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                    </tr>
                                </table>
                            </div>

                            <hr style="visibility:hidden;" />
                            <hr style="visibility:hidden;" />

                            <div>
                                <table>
                                    <tr>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                    </tr>
                                </table>
                            </div>

                            <div style="width:10px;"></div>

                            <div>
                                <table>
                                    <tr>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                        <td class="bt_1"></td>
                                    </tr>
                                </table>
                            </div>

                            <hr style="visibility:hidden;" />

                        </div>

                        <div>
                            <progress id="progress_exp" max="100" value="0"></progress>
                        </div>

                    </div>
                </div>

            </div>

                <svg viewBox="<?php echo "$vx $vy $tx $ty"; ?>" id="viewport" xmlns="http://www.w3.org/2000/svg">

                    <!-- On va construire la map -->

                    <!-- Les terrains(sols) -->
                    <g>
                        <?php
                            foreach($cases_terrains as $i=>$data){
                                $x = $data["x"] * $tc;
                                $y = $data["y"] * $tc;
                                $img = $terrains[$data["id_terrain"]]["img"];
                                $ct = $tc + 1; // On essaie d'enlever les lignes noires entre les tiles
                                echo "<image z-index=\"1\" x=$x y=$y width=$ct height=$ct xlink:href=\"../imgs/tuiles/$img\" class=\"case\"></image>";
                            }
                        ?>
                    </g>

                    <!-- Les objets de z-index 2 -->

                    <g>
                        <?php
                            foreach($cases_objets as $i=>$data){
                                $x = $data["x"] * $tc;
                                $y = $data["y"] * $tc;
                                $img = $objets[$data["id_objet"]]["img"];
                                $zindex = $objets[$data["id_objet"]]["z_index"];
                                $ct = $tc + 1; // On essaie d'enlever les lignes noires entre les tiles
                                if($zindex==1){
                                    echo "<image x=$x y=$y width=$ct height=$ct xlink:href=\"../imgs/objets/$img\" class=\"case\"></image>";
                                }
                            }
                        ?>
                    </g>

                    <!-- Le perso -->

                    <?php
                        $img_p = "../imgs/sprites/sprite_fixe_droit.png";
                        echo "<svg x=$px y=$py width=$tc height=$tc id=\"player\">";
                        echo "<image width=$tc height=$tc xlink:href=\"$img_p\"></image>";
                        echo "</svg>";

                    ?>

                    <!-- Les autres joueurs -->

                    <g id="svg_autres_joueurs">
                    </g>

                    <!-- Les objets de z-index 4 -->

                    <g>
                        <?php
                            foreach($cases_objets as $i=>$data){
                                $x = $data["x"] * $tc;
                                $y = $data["y"] * $tc;
                                $img = $objets[$data["id_objet"]]["img"];
                                $zindex = $objets[$data["id_objet"]]["z_index"];
                                $ct = $tc + 1; // On essaie d'enlever les lignes noires entre les tiles
                                if($zindex==3){
                                    echo "<image x=$x y=$y width=$ct height=$ct xlink:href=\"../imgs/objets/$img\" class=\"case\"></image>";
                                }
                            }
                        ?>
                    </g>

                </svg>


        </div>


        <div id="loading" style="background-color:black; z-index:10;  text-align: center;">

            <h2 style="color: white; text-align: center; margin-top:100px;">Loading ...</h2>

            <div class=" text-align: center;">
                <img src="../imgs/loading.gif" width=200px height=200px style=" text-align: center;" />
            </div>

        </div>

    </body>
    <script src="../js/websocket_client.js"></script>
    <script src="../js/jeu.js"></script>
    <script>

<?php
$data = open_json("../../includes/config.json");
$url_ws = $data["url_websocket"];
?>
var ws_url = "<?php echo $url_ws; ?>";

var en_chargement = true;
tx = <?php echo $tx; ?>;
ty = <?php echo $ty; ?>;
tc = <?php echo $tc; ?>;

function launch(){
    // make a simple rectangle

    start_websocket(ws_url);
}
function launch2(){
    // alert("id : "+<?php echo $id_player; ?>);
    // Websocket is ready
    ws_send({"action":"connection", "id_utilisateur":parseInt(<?php echo $id_player;?>)});
}


    </script>
</html>
