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
// On charge les données des objets :
$cases_objets = array();
$res = requete_prep($db, "SELECT x, y, id_objet, parametres FROM regions_objets WHERE id_region=:idr;", array(":idr"=>$id_region));
if($res==NULL){
    // echo("L'objet n'a pas pu charger");
    // die();
    $res = array();
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

// On va récuperer les infos sur les objets

$requete = "SELECT * FROM objets;";
$objets = array();
$r = requete_prep($db, $requete);
if($r==NULL){
    alert("Objet n'a pas chargé.");
}
// Pour chaque ligne, on stocke nom le nom et l'image dans l'Array $objets
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $objets[$data["id_objet"]] = array("nom"=>$nom, "img"=>$img, "z_index"=>$data["z_index"]);
}

// On va récuperer les infos sur les ennemis

$requete = "SELECT * FROM monstre;";
$ennemis = array();
$r = requete_prep($db, $requete);
if($r==NULL){
    alert("Ennemi n'a pas chargé.");
}
// Pour chaque ligne, on stocke nom le nom et l'image dans l'Array $ennemis
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["img_base"];
    $img_mort = $data["img_mort"];
    $ennemis[$data["id_monstre"]] = array("nom"=>$nom, "img"=>$img, "img_mort" => $img_mort);
}

// On va passer les infos des ennemis à js
if(count($ennemis)>0){
    $je = json_encode($ennemis);
    echo "<script>var ennemis_data = JSON.parse(`$je`); </script>";
    echo "<br/>";
}else{
    echo "<script>var ennemis_data = {}; </script>";
    echo "<br/>";
}

// On va passer les infos des cases des objets et des terrains à js

// On va préparer les cases_objets
$cases_objets_parametres = array();
$cases_objets_trait = array();
$cases_terrains_trait = array();
foreach($cases_objets as $i=>$data){
    $x = $data["x"];
    $y = $data["y"];
    $tp = $data["id_objet"];
    $p = $data["parametres"];
    if(json_last_error() != JSON_ERROR_NONE){
        echo json_last_error();
        echo json_last_error_msg();
        echo $p;
        die();
    }
    $cases_objets_trait[$x."_".$y] = $tp;
    $cases_objets_parametres[$x."_".$y] = $p;
}

foreach($cases_terrains as $i=>$data){
    $x = $data["x"];
    $y = $data["y"];
    $tp = $data["id_terrain"];
    $cases_terrains_trait[$x."_".$y] = $tp;
}
$jco = json_encode($cases_objets_trait);
$jct = json_encode($cases_terrains_trait);
$jpo = json_encode($cases_objets_parametres);
echo "<script>var cases_objets = JSON.parse(`$jco`); var cases_terrains = JSON.parse(`$jct`);</script>";
echo "<br/>";
script("var cases_objets_parametres = JSON.parse(`$jpo`);");
echo "<br/>";
script("
for(key of Object.keys(cases_objets_parametres)){
    var t = cases_objets_parametres[key];
    t = t.replaceAll(\"'\",'\"');
    cases_objets_parametres[key] = JSON.parse(t);
}");
echo "<br/>";

// On prépare les data des compétences et on les envoie au js

$competences = array();

$req = "SELECT * FROM competences;";
$res = requete_prep($db, $req);
foreach($res as $i=>$data){
    $competences[$data["id_competence"]] = $data;
}

$jc = json_encode($competences);
echo "<script>var competences = JSON.parse(`$jc`);</script>";

// On définit ici les infos relatives à l'affichage :

// $tx = 1280; // La taille horizontale du viewport
// $ty = 640; // La taille verticale du viewport
$tc = 64; // tc pour taille cases
// $tx = 18 * $tc;
// $ty = 10 * $tc;
$tx = 1280;
$ty = 840;
// Il y aura donc une grille de 10x5 affichée à l'écran
$px = $infos_players["position_x"] * $tc;
$py = $infos_players["position_y"] * $tc;
// On veut que le joueur soit au centre de l'écran
$vx = ($px-$tc/2) - ($tx/2); // Où commence le viewport sur l'axe des x
$vy = ($py-$tc/2) - ($ty/2); // Où commence le viewport sur l'axe des y
$vx2 = $vx+$tx;
$vy2 = $vy+$ty;
clog($px." ".$py." ".$vx." ".$vy." ".$vx2." ".$vy2." ".$tx." ".$ty);

?><!DOCTYPE HTML>
<html>

    <head>
        <meta charset="utf-8" />
        <title>Jeu</title>
        <link href="../css/style_jeu.css" rel="stylesheet" />
        <script src="../js/customisation_perso_data.js"></script>
    </head>

    

    <body onload="launch();">

        <div>
            <div id="ui">
                <!-- Menu Princ -->
                <div id="menu_princ" class="ui_box" style="display:none;">
                    <button onclick="set_menu('');" class="bt_x">X</button>
                    <div class="row" style="margin: 15px; text-align: center;">
                        <button class="bt_menu" onclick="window.location.href='accueil.php'">Quitter</button>
                        <button class="bt_menu" onclick="set_menu('menu_stats');">Stats</button>
                        <button class="bt_menu" onclick="set_menu('menu_inv');">Inventaire</button>
                    </div>
                </div>
                <!-- Menu inventaire -->
                <div id="menu_inv" class="ui_box" style="display:none;">
                    <button onclick="set_menu('');" class="bt_x">X</button>
                </div>
                <!-- Menu stats -->
                <div id="menu_stats" class="ui_box" style="display:none;">
                    <button onclick="set_menu('');" class="bt_x">X</button>
                    <div class="row">
                        <div class="column" style="width:50%">
                            <div class="row">
                                <b>Nom : </b>
                                <span id="player_name"></span>
                            </div>
                        </div>
                        <div class="column" style="width:50%">

                        </div>
                    </div>
                </div>
                <!-- Menu base -->
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
                    
                    <div id="div_actions" style="display:none;">
                        <h3>Actions : </h3>
                        <div class="column" id="liste_actions">
                        </div>
                    </div>

                    <div class="column_end full">

                        <div class="row_center">
                            <hr style="visibility:hidden;" />

                            <div>
                                <table>
                                    <tr>
                                        <td class="bt_1" id="bt_comp_1" onclick="lance_competence(1);"></td>
                                        <td class="bt_1" id="bt_comp_2" onclick="lance_competence(2);"></td>
                                        <td class="bt_1" id="bt_comp_3" onclick="lance_competence(3);"></td>
                                        <td class="bt_1" id="bt_comp_4" onclick="lance_competence(4);"></td>
                                    </tr>
                                </table>
                            </div>

                            <hr style="visibility:hidden;" />
                            <hr style="visibility:hidden;" />

                            <div>
                                <table>
                                    <tr>
                                        <td class="bt_1" id="bt_arme_1"></td>
                                        <td class="bt_1" id="bt_arme_2"></td>
                                        <td class="bt_1" id="bt_arme_3"></td>
                                        <td class="bt_1" id="bt_arme_4"></td>
                                    </tr>
                                </table>
                            </div>

                            <div style="width:10px;"></div>

                            <div>
                                <table>
                                    <tr>
                                        <td class="bt_1" id="bt_munition_1"></td>
                                        <td class="bt_1" id="bt_munition_2"></td>
                                        <td class="bt_1" id="bt_munition_3"></td>
                                        <td class="bt_1" id="bt_munition_4"></td>
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
                                $k = $x."_".$y;
                                echo "<image id='t$k' x=$x y=$y width=$ct height=$ct xlink:href=\"../imgs/tuiles/$img\" class=\"case\"></image>";
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
                                    $k = $x."_".$y;
                                    echo "<image id='o$k' x=$x y=$y width=$ct height=$ct xlink:href=\"../imgs/objets/$img\" class=\"case\"></image>";
                                }
                            }
                        ?>
                    </g>


                    <!-- Les ennemis -->
                    <g id="svg_ennemis">

                        <?php
                            echo "<svg x=0 y=0 width=$tc height=$tc id=\"monstre_template\" style=\"display:none;\">";
                            echo "<image width=$tc height=$tc xlink:href=\"../imgs/ennemis/inconu.png\"></image>";
                            echo "</svg>";

                        ?>

                    </g>

                    <!-- Le perso -->

                    <?php
                        $img_p = "../imgs/sprites/sprite_fixe_droit.png";
                        // On récupère les vetements du joueurs
                        $res = requete_prep($db, "SELECT id_tete, id_cheveux, id_barbe, id_haut, id_bas, id_pieds FROM utilisateurs WHERE id_utilisateur=:id_player", array(":id_player"=>$_SESSION["player_id"]));
                        if(count($res)==0){
                            $_SESSION["error"] = "Il y a eu une erreur lors de la création du personnage, votre compte a-t-il bien été créé ?";
                            header("Location: ../php/accueil.php");
                        }
                        $img_tete = "../imgs/custom_perso/".$images_corps["tete"][$res[0]['id_tete'] - 1];
                        $img_cheveux = "../imgs/custom_perso/".$images_corps["cheveux"][$res[0]["id_cheveux"] - 1];
                        $img_barbe = "../imgs/custom_perso/".$images_corps["barbe"][$res[0]["id_barbe"] - 1];
                        $img_haut = "../imgs/custom_perso/".$images_corps["haut"][$res[0]["id_haut"] - 1];
                        $img_bas = "../imgs/custom_perso/".$images_corps["bas"][$res[0]["id_bas"] - 1];
                        $img_pied = "../imgs/custom_perso/".$images_corps["pied"][$res[0]["id_pieds"] - 1];
                        //
                        echo "<svg x=$px y=$py width=$tc height=$tc id=\"player\">";
                        echo "<image id='img_perso_corps' width=$tc height=$tc xlink:href=\"$img_p\"></image>";
                        echo "<image id='img_perso_haut' width=$tc height=$tc xlink:href=\"$img_haut\"></image>";
                        echo "<image id='img_perso_bas' width=$tc height=$tc xlink:href=\"$img_bas\"></image>";
                        echo "<image id='img_perso_pied' width=$tc height=$tc xlink:href=\"$img_pied\"></image>";
                        echo "<image id='img_perso_barbe' width=$tc height=$tc xlink:href=\"$img_barbe\"></image>";
                        echo "<image id='img_perso_cheveux' width=$tc height=$tc xlink:href=\"$img_cheveux\"></image>";
                        echo "<image id='img_perso_tete' width=$tc height=$tc xlink:href=\"$img_tete\"></image>";
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
                                    $k = $x."_".$y;
                                    echo "<image id='o$k' x=$x y=$y width=$ct height=$ct xlink:href=\"../imgs/objets/$img\" class=\"case\"></image>";
                                }
                            }
                        ?>
                    </g>

                    <!-- Les infos des autres joueurs -->

                    <g id="svg_infos_autres_joueurs">

                    </g>

                    <!-- Les infos des ennemis -->

                    <g id="svg_infos_ennemis">

                    </g>

                    <!-- Les selecteurs -->

                    <g id="selecteurs">
                        <rect id="selec_terrain" x=0 y=0 width=0 height=0 fill="rgba(0,0,255,0.1)" style="display:none;">
                        </rect>
                        <rect id="selec_objet" x=0 y=0 width=0 height=0 fill="rgba(0,255,0,0.1)" style="display:none;">
                        </rect>
                        <rect id="selec_ennemi" x=0 y=0 width=0 height=0 fill="rgba(255,0,0,0.1)" style="display:none;">
                        </rect>
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

<?php
$data = open_json("../../includes/config.json");
$url_ws = $data["url_websocket"];

$token = random_str(50);

// On test s'il y a déjà une clé
$req = "SELECT token FROM tokens WHERE id_utilisateur = :id_user;";
$vars = array(":id_user" => $_SESSION["player_id"]);
$res = requete_prep($db, $req, $vars);
if(count($res)>0){
    // Il y a déjà une clé
    $req = "UPDATE tokens SET token = :token WHERE id_utilisateur = :id_user;";
    $vars = array(":id_user" => $_SESSION["player_id"], ":token" => $token);
    //
    $succeed = action_prep($db, $req, $vars);
    if(!$succeed){
        alert("Erreur !");
        die();
    }
}
else{
    // Il n'y a pas de clé
    $req = "INSERT INTO tokens SET token = :token, id_utilisateur = :id_user;";
    $vars = array(":id_user" => $_SESSION["player_id"], ":token" => $token);
    //
    $succeed = action_prep($db, $req, $vars);
    if(!$succeed){
        alert("Erreur !");
        die();
    }
}

// echo "alert(`$token`);";

script("var token = `$token`;");

?>

<script>

var en_chargement = true;
var ws_url = "<?php echo $url_ws; ?>";

tx = document.getElementById("viewport").clientWidth;
ty = document.getElementById("viewport").clientHeight;
tc = <?php echo $tc; ?>;

    </script>

<script>    

function launch(){
    start_websocket(ws_url);
}
function launch2(){
    // alert("id : "+<?php echo $id_player; ?>);
    // Websocket is ready
    ws_send({"action":"connection", "id_utilisateur":parseInt(<?php echo $id_player;?>), "token": token});
}

    </script>
</html>
