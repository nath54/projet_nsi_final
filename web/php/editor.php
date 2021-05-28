<style>

.bta{
    text-decoration: none;
    color: black;
    background-color: rgb(250,250,250);
    border:1px solid black;
    padding: 5px;
}.bta:hover{
    background-color: rgb(240,240,240);
}.bta:active{
    background-color: rgb(200,200,200);
}

</style>
<?php
include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

$db = load_db("../../includes/config.json");

// Pour l'instant, on va rester simple
// après, on pourra utiliser des tokens, des clés des sessions etc...
// Pour l'instant, juste admin
// Par contre, il faudra aussi veiller a ce que le compte ne reste pas trop inactif.
if(!isset($_SESSION["id_admin"])){
    $_SESSION["error"] = "Vous n'êtes pas connecté en tant qu'administrateur !";
    header("Location: admin_connect.php");
    die();
}


$dec_x = 0;
$dec_y = 0;

/**
 * ON CHARGE LES INFOS DES TERRAINS
 */
$requete = "SELECT * FROM terrain;";
$terrains = array();
$r = requete_prep($db, $requete);
if($r == NULL){
    alert("Il y a eu une erreur !");
}
foreach($r as $i => $data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $terrains[$data["id_terrain"]] = array("nom"=>$nom, "img"=>$img);
}


/**
 * ON CHARGE LES INFOS DES OBJETS
 */

$requete = "SELECT * FROM objets;";
$objets = array();
$r = requete_prep($db, $requete);
if($r == NULL){
    alert("Il y a eu une erreur !");
}
foreach($r as $i => $data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $objets[$data["id_objet"]] = array("id_objet"=>$data["id_objet"], "nom"=>$nom,
                                       "img"=>$img, "z_index"=>$data["z_index"]);
}


/**
 * ON CHARGE LES INFOS DES MONSTRES
 */

$requete = "SELECT * FROM monstre ORDER BY id_monstre;";
$ennemis = array();
$r = requete_prep($db, $requete);
if($r == NULL){
    alert("Il y a eu une erreur !");
}
foreach($r as $i => $data){
    $nom = $data["nom"];
    $img = $data["img_base"];
    $ennemis[$data["id_monstre"]] = array("id_monstre"=>$data["id_monstre"], "nom"=>$nom,
                                       "img_base"=>$img);
}



/**
 * ON CHARGE LES INFOS DES regions
 */

$liste_regions = array();
foreach(requete_prep($db, "SELECT * FROM regions") as $i=>$data){
    $liste_regions[$data["id_region"]]=$data["nom"];
}


/**
 * ON REGARDE SI LA REQUETE CONTIENT LE DECALAGE
 */

if(isset($_POST["dec_x"]) && isset($_POST["dec_y"])){
    $dec_x = $_POST["dec_x"];
    $dec_y = $_POST["dec_y"];
}


/**
 * ON REGARDE SI LA REQUETE EST DE TYPE SELECTIONNER UNE REGION
 */

$region_selected = "";
$id_region = 0;
if(isset($_POST["region_selected"])){
    if(in_array($_POST["region_selected"], array_keys($liste_regions))){
        $region_selected = $_POST["region_selected"];
        $id_region = $liste_regions[$region_selected];
    }
}

/**
 * ON REGARDE SI LA REQUETE EST DE TYPE UPDATE PARAMETERS
 */

if(isset($_POST["update_parameters"])){
    $new_params = $_POST["update_parameters"];
    $id_region = $_POST["id_region"];
    $x = $_POST["x"];
    $y = $_POST["y"];
    //
    $req = "UPDATE regions_objets SET parametres=:params WHERE x=:x AND y=:y AND id_region=:idr";
    $vars = array(":params"=>$new_params, ":x"=>$x, ":y"=>$y, ":idr"=>$id_region);
    $succes = action_prep($db, $req, $vars);
    if(!$succes){
        alert("Il y a eu une erreur lors de l'update des parametres !");
    }
}

/**
 * ON REGARDE SI LA REQUETE EST DE TYPE SUPPRIMER UNE REGION
 */

if(isset($_POST["delete_region"])){
    if(in_array($_POST["delete_region"], array_keys($liste_regions))){
        $idr = $_POST["delete_region"];
        //
        $query = "DELETE FROM regions WHERE id_region=:idr";
        $vars = array(":idr"=>$idr);
        $query2 = "DELETE FROM regions_terrains WHERE id_region=:idr";
        $vars2 = array(":idr"=>$idr);
        $query3 = "DELETE FROM regions_objets WHERE id_region=:idr";
        $vars3 = array(":idr"=>$idr);
        $query4 = "DELETE FROM regions_monstres WHERE id_region=:idr";
        $vars4 = array(":idr"=>$idr);
        if(!action_prep($db, $query3, $vars3) || !action_prep($db, $query2, $vars2) || !action_prep($db, $query, $vars) || !action_prep($db, $query4, $vars4)){
            alert("Il y a eu une erreur lors de la suppression de la région !");
        }
        else{
            unset($liste_regions[$_POST["delete_region"]]);
        }
    }
    else{
        alert("La région n'existe pas !");
    }
}

/**
 * ON REGARDE SI LA REQUETE EST DE TYPE NOUVELLE REGION
 */
if(isset($_POST["new_region"])){
    if($_POST["new_region"]!="" && !in_array($_POST["new_region"], array_values($liste_regions))){
        $query = "INSERT INTO regions SET nom=:nom";
        $vars = array(":nom"=>$_POST["new_region"]);
        if(!action_prep($db, $query, $vars)){
            die();
            alert("Il y a eu une erreur lors de la création de la région !");
        }
        else{
            $region_selected = $db->lastInsertId();
            $liste_regions[$db->lastInsertId()]=$_POST["new_region"];
        }
    }
    else{
        alert("Une région porte déjà le même nom !");
    }
}


/**
 * ON INITIALISE LES VARIABLES QUI CONTIENDRONT LES INFORMATIONS DES CASES DE LA REGION
 */

$cases_terrains = array();
$cases_objets = array();
$cases_ennemis = array();

/**
 * ON REGARDE SI LA REQUETE EST DE TYPE SAUVEGARDE DE REGIONS
 */

if(
  isset($_POST["save_terrain"]) &&
  isset($_POST["delete_terrains"]) &&
  isset($_POST["update_terrains"]) &&
  isset($_POST["new_terrains"])  &&
  isset($_POST["delete_objets"]) &&
  isset($_POST["update_objets"])  &&
  isset($_POST["new_objets"]) &&
  isset($_POST["delete_ennemis"]) &&
  isset($_POST["update_ennemis"])  &&
  isset($_POST["new_ennemis"])
  ){
    $idr = $_POST["save_terrain"];
    $region_selected = $idr;
    // Pour changer si on veut passer en requetes préparée, plus de calcul, mais plus de sécurité
    $mode = 0; // normal = 0 sinon préparé = 1
    $delete_t = json_decode($_POST["delete_terrains"], true);
    $delete_o = json_decode($_POST["delete_objets"], true);
    $delete_e = json_decode($_POST["delete_ennemis"], true);
    $update_t = json_decode($_POST["update_terrains"], true);
    $update_o = json_decode($_POST["update_objets"], true);
    $update_e = json_decode($_POST["update_ennemis"], true);
    $new_t = json_decode($_POST["new_terrains"], true);
    $new_o = json_decode($_POST["new_objets"], true);
    $new_e = json_decode($_POST["new_ennemis"], true);
    $iu_t = $new_t + $update_t;
    $iu_o = $new_o + $update_o;
    $iu_e = $new_e + $update_e;
    /***************** DELETE TERRAINS : *******************/
    if(count($delete_t)>0){
        $req = "DELETE FROM regions_terrains WHERE (x,y,id_region) IN ( ";
        $virgule = false;
        $vars = array();
        // Pour requete_prep:
        $compteur = 0;
        foreach($delete_t as $i => $data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            // pour requete non préparée
            if($mode == 0){
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $data["id_region"] . " )";
            }
            else{
                $req .= "(:x_$compteur, :y_$compteur, :idr_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idr_$compteur"] = $data["id_region"];
                $compteur += 1;
            }
        }
        $req .= " );";
        // echo "delete terrains : $req <br />";
        if(!action_prep($db, $req, $vars)){
            echo "probleme delete terrains <br />";
            die();
        }
    }

    /***************** DELETE OBJETS : *******************/
    if(count($delete_o)>0){
        $req = "DELETE FROM regions_objets WHERE (x,y,id_region) IN ( ";
        $virgule = false;
        $vars = array();
        // Pour requete_prep:
        $compteur = 0;
        foreach($delete_o as $i=>$data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            // pour requete non préparée
            if($mode == 0){
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $data["id_region"] . " )";
            }
            else{
                $req .= "(:x_$compteur, :y_$compteur, :idr_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idr_$compteur"] = $data["id_region"];
                $compteur += 1;
            }
        }
        $req .= " );";
        // echo "delete objets : $req <br />";
        if(!action_prep($db, $req, $vars)){
            echo "probleme delete objets <br />";
            die();
        }
    }

    /***************** DELETE ENNEMIS : *******************/
    if(count($delete_e)>0){
        $req = "DELETE FROM regions_monstres WHERE (x,y,id_region) IN ( ";
        $virgule = false;
        $vars = array();
        // Pour requete_prep:
        $compteur = 0;
        foreach($delete_e as $i=>$data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            // pour requete non préparée
            if($mode == 0){
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $data["id_region"] . " )";
            }
            else{
                $req .= "(:x_$compteur, :y_$compteur, :idr_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idr_$compteur"] = $data["id_region"];
                $compteur += 1;
            }
        }
        $req .= " );";
        // echo "delete objets : $req <br />";
        if(!action_prep($db, $req, $vars)){
            echo "probleme delete objets <br />";
            die();
        }
    }

    /***************** INSERT/UPDATE NEW TERRAINS : *******************/
    if(count($iu_t)>0){
        $req = "INSERT INTO regions_terrains (x,y,id_region,id_terrain) VALUES ";
        $virgule = false;
        $vars = array();
        $compteur = 0; // Pour requete_prep:
        foreach($iu_t as $i=>$data){
            if(!$virgule){
                $virgule=true;
            }
            else{
                $req .= ", ";
            }
            if($mode == 0){ // pour requete non préparée
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $data["id_region"] . ", " .
                        $data["id_terrain"] . " )";
            }
            else{  // Pour requete_prep:
                $req .= "(:x_$compteur, :y_$compteur, :idr_$compteur, :idt_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idr_$compteur"] = $data["id_region"];
                $vars[":idt_$compteur"] = $data["id_terrain"];
                $compteur += 1;
            }
        }
        $req .= " ON DUPLICATE KEY UPDATE id_terrain=VALUES(id_terrain);";
        if(!action_prep($db, $req, $vars)){
            echo "probleme insert/update terrains  <br />";
            die();
        }
    }


    /***************** INSERT/UPDATE NEW OBJETS : *******************/
    if(count($iu_o)>0){
        $req = "INSERT INTO regions_objets (x,y,id_region,id_objet) VALUES ";
        $virgule = false;
        $vars = array();
        $compteur = 0; // Pour requete_prep:
        foreach($iu_o as $i => $data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            if($mode == 0){ // pour requete non préparée
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $data["id_region"] . ", " .
                        $data["id_objet"] . " )";
            }
            else{ // Pour requete_prep:
                $req .= "(:x_$compteur, :y_$compteur, :idr_$compteur, :ido_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idr_$compteur"] = $data["id_region"];
                $vars[":ido_$compteur"] = $data["id_objet"];
                $compteur += 1;
            }
        }
        $req .= " ON DUPLICATE KEY UPDATE id_objet=VALUES(id_objet);";
        if(!action_prep($db, $req, $vars)){
            echo "probleme insert/update objets <br />";
            die();
        }
    }

    /***************** INSERT/UPDATE NEW ENNEMIS : *******************/
    if(count($iu_e)>0){
        $req = "INSERT INTO regions_monstres (x,y,id_region,id_monstre) VALUES ";
        $virgule = false;
        $vars = array();
        $compteur = 0; // Pour requete_prep:
        foreach($iu_e as $i => $data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            if($mode == 0){ // pour requete non préparée
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $data["id_region"] . ", " .
                        $data["id_monstre"] . " )";
            }
            else{ // Pour requete_prep:
                $req .= "(:x_$compteur, :y_$compteur, :idr_$compteur, :ide_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idr_$compteur"] = $data["id_region"];
                $vars[":ide_$compteur"] = $data["id_monstre"];
                $compteur += 1;
            }
        }
        $req .= " ON DUPLICATE KEY UPDATE id_monstre=VALUES(id_monstre);";
        if(!action_prep($db, $req, $vars)){
            echo "probleme insert/update ennemis <br />";
            die();
        }
    }

}

if(isset($_POST["import_data"]) && isset($_POST["import_region"])){
    $content = $_POST["import_data"];
    $data = json_decode($content, true);
    $cases_terrains = $data["terrains"];
    $cases_objets = $data["objets"];
    $cases_ennemis = $data["ennemis"];
    $id_region = $_POST["import_region"];
    // Pour changer si on veut passer en requetes préparée, plus de calcul, mais plus de sécurité
    $mode = 0; // normal = 0 sinon préparé = 1
    // On supprime tout:
    $query = "DELETE FROM regions_terrains WHERE id_region=:idr;";
    $query2 = "DELETE FROM regions_objets WHERE id_region=:idr;";
    $query3 = "DELETE FROM regions_monstres WHERE id_region=:idr;";
    $vars = array(":idr"=>$id_region);
    //
    if(!action_prep($db, $query, $vars)){
        echo "probleme delete regions_terrains <br />";
        die();
    }
    if(!action_prep($db, $query2, $vars)){
        echo "probleme delete regions_objets <br />";
        die();
    }
    if(!action_prep($db, $query3, $vars)){
        echo "probleme delete regions_ennemis <br />";
        die();
    }
    // On crée tout


    if(count($cases_terrains)>0){
        $req = "INSERT INTO regions_terrains (x,y,id_region,id_terrain) VALUES ";
        $virgule = false;
        $vars = array();
        if($mode == 1){
            $vars[":idr"]=$id_region;
        }
        // Pour requete_prep:
        $compteur = 0;
        foreach($cases_terrains as $i => $data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req.=", ";
            }
            // pour requete non préparée
            if($mode == 0){
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $id_region . ", " . $data["id_terrain"] . " )";
            }
            else{
                $req .= "(:x_$compteur, :y_$compteur, :idr, :idt_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":idt_$compteur"] = $data["id_terrain"];
                $compteur += 1;
            }
        }
        $req .= ";";
        // echo "insert objets : $req <br />";
        if(!action_prep($db, $req, $vars)){
            echo "probleme import insert terrain <br />";
            die();
        }
    }

    if(count($cases_objets)>0){
        $req = "INSERT INTO regions_objets (x,y,id_region,id_objet) VALUES ";
        $virgule = false;
        $vars = array();
        if($mode == 1){
            $vars[":idr"] = $id_region;
        }
        // Pour requete_prep:
        $compteur = 0;
        foreach($cases_objets as $i => $data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            // pour requete non préparée
            if($mode == 0){
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $id_region . ", " . $data["id_objet"] . " )";
            }
            else{
                $req .= "(:x_$compteur, :y_$compteur, :idr, :ido_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":ido_$compteur"] = $data["id_objet"];
                $compteur += 1;
            }
        }
        $req .= ";";
        // echo "insert objets : $req <br />";
        if(!action_prep($db, $req, $vars)){
            echo "probleme import insert objets <br />";
            die();
        }
    }



    if(count($cases_ennemis)>0){
        $req = "INSERT INTO regions_monstres (x,y,id_region,id_monstre) VALUES ";
        $virgule = false;
        $vars = array();
        if($mode == 1){
            $vars[":idr"] = $id_region;
        }
        // Pour requete_prep:
        $compteur = 0;
        foreach($cases_ennemis as $i => $data){
            if(!$virgule){
                $virgule = true;
            }
            else{
                $req .= ", ";
            }
            // pour requete non préparée
            if($mode == 0){
                $req .= "( " . $data["x"] . ", " . $data["y"] . ", " . $id_region . ", " . $data["id_monstre"] . " )";
            }
            else{
                $req .= "(:x_$compteur, :y_$compteur, :idr, :ide_$compteur)";
                $vars[":x_$compteur"] = $data["x"];
                $vars[":y_$compteur"] = $data["y"];
                $vars[":ide_$compteur"] = $data["id_monstre"];
                $compteur += 1;
            }
        }
        $req .= ";";
        // echo "insert objets : $req <br />";
        if(!action_prep($db, $req, $vars)){
            echo "probleme import insert ennemis <br />";
            die();
        }
    }


    $region_selected = $id_region;

}

/**
 * S'IL Y A BIEN UNE REGION SELECTIONNEE
 */

if($region_selected != ""){
    // LES TERRAINS
    $requested = "SELECT * FROM regions_terrains WHERE id_region=:idr";
    $vars = array(":idr" => $region_selected);
    foreach(requete_prep($db, $requested, $vars) as $i=>$data){
        $x = $data["x"];
        $y = $data["y"];
        $tile = $data["id_terrain"];
        $cases_terrains["$x-$y"] = array("x" => $x, "y" => $y, "id_terrain" => $tile);
    }
    // LES OBJETS
    $requested = "SELECT * FROM regions_objets WHERE id_region=:idr";
    $vars = array(":idr" => $region_selected);
    foreach(requete_prep($db, $requested, $vars) as $i => $data){
        $x = $data["x"];
        $y = $data["y"];
        $ido = $data["id_objet"];
        $params = $data["parametres"];
        $cases_objets["$x-$y"] = array("x" => $x, "y" =>$y , "id_objet" => $ido, "parametres" => $params);
    }
    // LES ENNEMIS
    $requested = "SELECT * FROM regions_monstres WHERE id_region=:idr";
    $vars = array(":idr" => $region_selected);
    foreach(requete_prep($db, $requested, $vars) as $i => $data){
        $x = $data["x"];
        $y = $data["y"];
        $ido = $data["id_monstre"];
        $cases_ennemis["$x-$y"] = array("x" => $x, "y" =>$y , "id_monstre" => $ido);
    }
    // alert("aaa  ".$cases_objets["15-6"]["parametres"]);
    script("var nom_region=\"" . $liste_regions[$region_selected] . "\"");
}
else{
    script("var nom_region=\"\"");
}


/**
 * ON TRANSFERE LES DONNES VERS JS GRACE A JSON
 */


//
script("var region_selected = $region_selected;");

// Les données du terrain
$jsone = json_encode($terrains);
script("var terrains = JSON.parse(`$jsone`);");

// Les données des objets
$jsone = json_encode($objets);
script("var objets = JSON.parse(`$jsone`);");

// Les données des ennemis
$jsone = json_encode($ennemis);
script("var ennemis = JSON.parse(`$jsone`);");

// Les données des cases de terrain
if(count($cases_terrains) > 0){
    $jsone = json_encode($cases_terrains);
    script("var cases_terrains = JSON.parse(`$jsone`);");
}
else{
    script("var cases_terrains = {};");
}

// Les données des cases des objets
if(count($cases_objets) > 0){
    $jsone = json_encode($cases_objets);
    // $jsone = str_replace("'", "_", $jsone);
    $jsone = str_replace("\\\"", "'", $jsone);    
    script("var cases_objets = JSON.parse(`$jsone`);");
}
else{
    script("var cases_objets = {};");
}


// Les données des cases des ennemis
if(count($cases_ennemis) > 0){
    $jsone = json_encode($cases_ennemis);
    script("var cases_ennemis = JSON.parse(`$jsone`);");
}
else{
    script("var cases_ennemis = {};");
}


$tc = 5; // LARGEUR DES CASES

?>
<html>
    <style>
body {
    overflow: hidden;
}

    </style>
    <head>
        <meta charset="UTF-8" />
        <title>Editeur de map</title>
        <link href="../css/editor.css" rel="stylesheet" />
    </head>
    <body onload="aff();">
        <!-- header -->
        <div>

            <div class="row">

                <select id="region_sel" onchange="change_map()">

                    <option value="" <?php if($region_selected == ""){ echo "selected"; } ?>>Aucune</option>
                    <?php

                        /**
                         * ON RECUPERE LA LISTE DES REGIONS ET ON LES METS DANS LA LISTE DEROULANTE
                         */

                        foreach($liste_regions as $idr => $nom){
                            $sel = "";
                            if($idr == $region_selected){
                                $sel = "selected";
                            }
                            echo "<option value=$idr $sel>" . $liste_regions[$idr] . "</option>";
                        }

                    ?>

                </select>

                <div>
                    <?php


                    /**
                     * S'IL Y A UNE REGION SELECTIONNE ON AFFICHE LES BOUTONS
                     * PERMETTANT DE SUPPRIMER LA REGION ET SAUVEGARDER LES MODIFICATIONS
                     */

                    if($region_selected != ""){
                        echo "<button onclick=\"delete_region();\">Supprimer la région choisie</button>";
                        echo "<button onclick=\"save_tiles();\">Sauvegarder la région choisie</button>";
                    }

                    ?>
                </div>

                <div class="row">
                    <label>New region</label>
                    <!-- INPUT POUR CHOISIR LE NOM DE LA NOUVELLE REGION -->
                    <input id="new_region_name" type="text" placeholder="nom de la region">
                    <!-- BOUTON POUR CREER LA NOUVELLE REGION -->
                    <button onclick="new_region();">Créer</button>
                </div>

                <div class="row">
                    <!-- BOUTON POUR EXPORTER LA REGION -->
                    <button onclick="export_region();">Export region</button>
                    <!-- INPUT POUR CHOISIR LE FICHIER A IMPORTER -->
                    <input id="file_import" style="display:none;" type="file" accept=".json">
                    <!-- BOUTON POUR IMPORTER LES DONNEES -->
                    <button onclick="import_region();">Import region</button>
                </div>

            </div>


        </div>
        <!-- main -->
        <div class="row">

            <!-- map -->

            <div style="overflow:auto;width:100%;height:90%;">

            <?php
                if($region_selected!=""){
                    echo "<svg viewBox=\"0 0 100 80\" id=\"viewport\" onmouseleave=\"is_clicking=false;\" style=\"background:white;border:1px solid black;\" xmlns=\"http://www.w3.org/2000/svg\">";

                    $tx = 20; // NOMBRE DE CASES HORIZONTABLES QUE L'ECRAN AFFICHE
                    $ty = 16; // NOMBRE DE CASES VERTICALES QUE L'ECRAN AFFICHE
                    $dx = 0; // VARIABLE DE DEPLACEMENT X DANS LA MAP
                    $dy = 0; // VARIABLE DE DEPLACEMENT Y DANS LA MAP
                    // case de tests
                    $ct = $tc + 0.15;
                    echo "<image id=\"case_test\" style=\"display:none;\" x=\"0\" y=\"0\" width=\"$ct\" height=\"$ct\" class=\"case\"></image>";
                    // terrains
                    // ON CREE LA GRILLE POUR LES TERRAINS
                    for($x = 0; $x < $tx; $x++){
                        for($y = 0; $y < $ty; $y++){
                            $cx = $x * $tc + $dx;
                            $cy = $y * $tc + $dy;
                            $idd = "$x-$y";
                            $src="../imgs/tuiles/vide.png";
                            if(isset($cases_terrains[$idd])){
                                $img = $terrains[$cases_terrains[$idd]["id_terrain"]]["img"];
                                $src = "../imgs/tuiles/$img";
                            }
                            echo "<image z_index=0 id=\"$x-$y\" xlink:href=\"$src\" x=\"$cx\" y=\"$cy\" width=\"$ct\" height=\"$ct\" onclick=\"mclick($x,$y);\"  onmouseover=\"mo($x,$y);\" onmouseout=\"ml($x,$y);\" class=\"case\"></image>";
                        }
                    }
                    // objets
                    // ON CREE LA GRILLE POUR LES OBJETS
                    for($x = 0; $x < $tx; $x++){
                        for($y = 0; $y < $ty; $y++){
                            $cx = $x * $tc + $dx;
                            $cy = $y * $tc + $dy;
                            $idd = "$x-$y";
                            $src = "";
                            if(isset($cases_objets[$idd])){
                                $img = $objets[$cases_objets[$idd]["id_objet"]]["img"];
                                $src = "../imgs/objets/$img";
                            }
                            $ct = $tc + 0.15;
                            echo "<image z_index=0 id=\"o_$x-$y\" xlink:href=\"$src\" x=\"$cx\" y=\"$cy\" width=\"$ct\" height=\"$ct\" onclick=\"mclick($x,$y);\" onmouseover=\"mo($x,$y);\" onmouseout=\"ml($x,$y);\" class=\"case\"></image>";
                        }
                    }
                    // ennemis
                    // ON CREE LA GRILLE POUR LES ENNEMIS
                    for($x = 0; $x < $tx; $x++){
                        for($y = 0; $y < $ty; $y++){
                            $cx = $x * $tc + $dx;
                            $cy = $y * $tc + $dy;
                            $idd = "$x-$y";
                            $src = "";
                            if(isset($cases_ennemis[$idd])){
                                $img = $ennemis[$cases_ennemis[$idd]["id_monstre"]]["img_base"];
                                $src = "../imgs/ennemis/$img";
                            }
                            $ct = $tc + 0.15;
                            echo "<image z_index=0 id=\"e_$x-$y\" xlink:href=\"$src\" x=\"$cx\" y=\"$cy\" width=\"$ct\" height=\"$ct\" onclick=\"mclick($x,$y);\"  onmouseover=\"mo($x,$y);\" onmouseout=\"ml($x,$y);\" class=\"case\"></image>";
                        }
                    }
                    // On va créer l'indice de selection pour les parametres
                    echo "<rect id=\"selection_params\" x=0 y=0 width=$tc height=$tc style=\"stroke: green; stroke-width: 0.2; fill:none; display:none;\"></rect>";
                    //
                    echo "</svg>";
                }
                else{
                    echo "<p>Aucune région n'a été choisie</p>";
                }
            ?>

            <!-- INFORMATIONS DES MODIFICATIONS -->
            <div class="row">
                <p>Case hover: <span id="hover_case">aucune</span></p>
                <hr />
                <p>Nombre de modifications: <span id="nb_modifs">0</span></p>
                <hr />
                <b id="alert_modifs" style="color:red; display:none;">Vous avez fait plus de 100 modifs, il faudrait peut-être penser à sauvegarder !</b>
            </div>
            </div>

            <!-- tiles menu -->

            <div style="overflow:scroll;width:100%;height:500px;">

                <!-- tile selected to paint -->
                <div>

                </div>

                <!-- Select tiles -->

                <div class="liste_tiles">

                    <div class="row">
                        <!-- BOUTONS POUR CHOISIR LE MENU DE PLACEMENT -->
                        <button onclick="set_selection('terrains');">Cases</button>
                        <button onclick="set_selection('objets_parametres');">Parametres des Objets</button>
                    </div>

                    <div class="row">
                        <div id="bts_placer">
                            <!-- BOUTONS POUR CHOISIR LE MENU DE PLACEMENT -->
                            <button onclick="set_selection('terrains');">Terrains</button>
                            <button onclick="set_selection('objets');">Objets</button>
                            <button onclick="set_selection('ennemis');">Ennemis</button>
                        </div>
                        <div id="bts_params" style="display:none;">
                            <button onclick="save_parameters();">Update parameter</button>
                        </div>
                    </div>

                    <div id="terrains">
                        <!-- INPUT POUR CHERCHER LES TYPES DE CASES DE TERRAINS QUI COMMENCENT PAR UNE CERTAINE CHAINE DE CARACTERES -->
                        <div class="row"> <input id="search_t" type="text" placeholder="search" onkeypress="search_t();" onchange="search_t();" /> <p>Press Enter to search</p></div>
                        <?php
                            // ON CHARGE TOUTES LES DONNEES DES TYPES DE TERRAINS
                            foreach($terrains as $i=>$data){
                                $img = $data["img"];
                                $nom = $data["nom"];
                                $sel = "";
                                if($i == 0){ // au début, l'herbe sera selectionne par defaut
                                    $sel = "liste_element_selectione";
                                }
                                echo "<div value=\"$nom\" id=\"liste_elt_$i\" class=\"liste_terrains liste_element $sel\" onclick=\"select_tile($i);\"><img class=\"img_liste_element\" src=\"../imgs/tuiles/$img\" /><label>$nom</label></div>";
                            }
                        ?>
                    </div>

                    <div id="objets_parametres" style="display:none; padding: 25px;">
                        <p id="texte_objets"></p>
                        <br />
                        <textarea id="object_parameters" placeholder="{}" value="" >
                        </textarea>
                        <br />
                        <b style="color:red;">Attention ! Veuillez d'abords sauvegarder les autres changements avant de modifier les parametres des objets, sinon, vous allez perdre des modifications !</b>
                        <br />
                        <b style="color:blue;">Encore Attention ! Pour les chaines de caractères utilisez '' au lieu de "", et ne mettez pas d'apostrophes dans vos chaines de caractères !</b>
                    </div>

                    <div id="objets" style="display:none;">
                        <!-- INPUT POUR CHERCHER LES TYPES DE CASES D'OBJETS QUI COMMENCENT PAR UNE CERTAINE CHAINE DE CARACTERES -->
                        <div class="row"> <input id="search_o" type="text" placeholder="search" onkeypress="search_o();" onchange="search_o();" /> <p>Press Enter to search</p></div>
                        <?php
                            // ON CHARGE TOUTES LES DONNEES DES TYPES D'OBJETS
                            foreach($objets as $i=>$data){
                                $img = $data["img"];
                                $nom = $data["nom"];
                                $sel = "";
                                // $ido = $data["id_objet"];
                                echo "<div value=\"$nom\" id=\"liste_obj_$i\" class=\"liste_objets liste_element $sel\" onclick=\"select_objets($i);\"><img class=\"img_liste_element\" src=\"../imgs/objets/$img\" /><label>$nom</label></div>";
                            }

                        ?>

                    </div>

                    <div id="ennemis" style="display:none;">
                        <!-- INPUT POUR CHERCHER LES TYPES DE CASES D'OBJETS QUI COMMENCENT PAR UNE CERTAINE CHAINE DE CARACTERES -->
                        <div class="row"> <input id="search_o" type="text" placeholder="search" onkeypress="search_e();" onchange="search_o();" /> <p>Press Enter to search</p></div>
                        <?php
                            // ON CHARGE TOUTES LES DONNEES DES TYPES D'OBJETS
                            foreach($ennemis as $i=>$data){
                                $img = $data["img_base"];
                                $nom = $data["nom"];
                                $sel = "";
                                echo "<div value=\"$nom\" id=\"liste_enn_$i\" class=\"liste_ennemi liste_element $sel\" onclick=\"select_ennemis($i);\"><img class=\"img_liste_element\" src=\"../imgs/ennemis/$img\" /><label>$nom</label></div>";
                            }

                        ?>

                    </div>

                </div>

            </div>


        </div>
    </body>
</html>
<?php
echo "<script>const tc = $tc;</script>"
?>
<script>

// L'id de la region que l'on a chargée dans l'editeur
const id_region = <?php if($region_selected != ""){ echo $region_selected; } else { echo "null"; } ?>;

// Le décalage de l'affichage
var dcx = null;
var dcy = null;

var mode = "placer"; // Modes : placer / parametres

var tile_selected = 0;
var tp_selected = "terrains";
var dec_x = <?php echo $dec_x; ?>;
var dec_y = <?php echo $dec_y; ?>;

var is_clicking = false;
var hx=null;
var hy=null;

var selected_x = null;
var selected_y = null;
var selec_dec_x = 0;
var selec_dec_y = 0;


if(document.getElementById("viewport")){
    var viewport = document.getElementById("viewport");
}
else{
    var viewport = null;
}

var compteur_modif = 0; // Cette fonction va enregistrer le nombre de modifications faites

// Variables pour sauvegarder les modifs du terrain dans la bdd
var update_t = {};
var new_t = {};
var delete_t = {};

// Variables pour sauvegarder les modifs des objets dans la bdd
var update_o = {};
var new_o = {};
var delete_o = {};

// Variables pour sauvegarder les modifs des objets dans la bdd
var update_e = {};
var new_e = {};
var delete_e = {};

/**
 * FONCTION POUR CHANGER LA REGION SELECTIONNEE
 */

function change_map(){
    var nom = document.getElementById("region_sel").value;
    var f = document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i = document.createElement("input");
    i.setAttribute("name", "region_selected");
    i.value = nom;
    f.appendChild(i);
    document.body.appendChild(f);
    f.submit();
}


/**
 * FONCTION POUR CHANGER L'ITEM SELECTIONNE
 */

function select_tile(id_tile){
    if(id_tile == tile_selected && tp_selected == "terrains"){
        return;
    }
    if(tp_selected == "terrains"){
        var ad = document.getElementById("liste_elt_" + tile_selected);
    }
    else if(tp_selected == "objets"){
        var ad = document.getElementById("liste_obj_" + tile_selected);
    }
    else if(tp_selected == "ennemis"){
        var ad = document.getElementById("liste_enn_" + tile_selected);
    }
    ad.classList.remove("liste_element_selectione");
    var d = document.getElementById("liste_elt_" + id_tile);
    d.classList.add("liste_element_selectione");
    tile_selected = id_tile;
    tp_selected = "terrains";
}

function select_objets(id_tile){
    if(id_tile == tile_selected && tp_selected == "objets"){
        return;
    }
    if(tp_selected == "terrains"){
        var ad = document.getElementById("liste_elt_" + tile_selected);
    }
    else if(tp_selected == "objets"){
        var ad = document.getElementById("liste_obj_" + tile_selected);
    }
    else if(tp_selected == "ennemis"){
        var ad = document.getElementById("liste_enn_" + tile_selected);
    }
    ad.classList.remove("liste_element_selectione");
    var d = document.getElementById("liste_obj_" + id_tile);
    d.classList.add("liste_element_selectione");
    tile_selected = id_tile;
    tp_selected = "objets";
}

function select_ennemis(id_monstre){
    if(id_monstre == tile_selected && tp_selected == "ennemis"){
        return;
    }
    if(tp_selected == "terrains"){
        var ad = document.getElementById("liste_elt_" + tile_selected);
    }
    else if(tp_selected == "objets"){
        var ad = document.getElementById("liste_obj_" + tile_selected);
    }
    else if(tp_selected == "ennemis"){
        var ad = document.getElementById("liste_enn_" + tile_selected);
    }
    ad.classList.remove("liste_element_selectione");
    var d = document.getElementById("liste_enn_" + id_monstre);
    d.classList.add("liste_element_selectione");
    tile_selected = id_monstre;
    tp_selected = "ennemis";
}



/**
 * FONCTION POUR CHANGER UNE CASE
 */

function change_case(x, y){
    if(mode != "placer"){
        return;
    }
    //
    // console.log(x,y);
    //
    var cx = x + dec_x;
    var cy = y + dec_y;
    dcx, dcy = cx, cy;
    var i = "" + cx + "-" + cy;
    if(tile_selected == 0){
        // Terrains
        if(tp_selected == "terrains"){
            if(Object.keys(cases_terrains).includes(i)){
                if(Object.keys(update_t).includes(i)){
                    delete update_t[i];
                    compteur_modif -= 1;
                }
                if(!Object.keys(delete_t).includes(i)){
                    delete_t[i] = {"x": cx, "y": cy, "id_region": id_region};
                    compteur_modif += 1;
                }
                var e = document.getElementById("" + x + "-" + y);
                e.setAttribute("xlink:href", "../imgs/tuiles/vide.png");
            }
            else{
                if(Object.keys(new_t).includes(i)){
                    delete new_t[i];
                    compteur_modif -= 1;
                }
                var e = document.getElementById("" + x + "-" + y);
                e.setAttribute("xlink:href","../imgs/tuiles/vide.png");
            }
        }
        // Objets
        else if(tp_selected == "objets"){
            if(Object.keys(cases_objets).includes(i)){
                if(Object.keys(update_o).includes(i)){
                    delete update_o[i];
                    compteur_modif -= 1;
                }
                if(!Object.keys(delete_o).includes(i)){
                    delete_o[i] = {"x": cx, "y": cy, "id_region": id_region};
                    compteur_modif += 1;
                }
                var e = document.getElementById("o_" + x + "-" + y);
                e.setAttribute("xlink:href","../imgs/objets/rien.png");
            }
            else{
                if(Object.keys(new_o).includes(i)){
                    delete new_o[i];
                    compteur_modif -= 1;
                }
                var e = document.getElementById("o_"+x+"-"+y);
                e.setAttribute("xlink:href","../imgs/objets/rien.png");
            }
        }
        // Ennemis
        else if(tp_selected == "ennemis"){
            if(Object.keys(cases_ennemis).includes(i)){
                if(Object.keys(update_e).includes(i)){
                    delete update_e[i];
                    compteur_modif -= 1;
                }
                if(!Object.keys(delete_e).includes(i)){
                    delete_e[i] = {"x": cx, "y": cy, "id_region": id_region};
                    compteur_modif += 1;
                }
                var e = document.getElementById("e_" + x + "-" + y);
                e.setAttribute("xlink:href","../imgs/objets/rien.png");
            }
            else{
                if(Object.keys(new_e).includes(i)){
                    delete new_e[i];
                    compteur_modif -= 1;
                }
                var e = document.getElementById("e_"+x+"-"+y);
                e.setAttribute("xlink:href","../imgs/objets/rien.png");
            }
        }
    }
    else{
        // Terrains
        if(tp_selected=="terrains"){
            if(Object.keys(cases_terrains).includes(i)){
                if(cases_terrains[i]["id_terrain"]!=tile_selected){
                    if(!Object.keys(update_t).includes(i)){
                        compteur_modif += 1;
                    }
                    update_t[i] = {"x":cx, "y":cy, "id_terrain":tile_selected, "id_region": id_region};
                }
            }
            else{
                if(!Object.keys(new_t).includes(i)){
                    compteur_modif += 1;
                }
                new_t[i] = {"x":cx, "y":cy, "id_terrain":tile_selected, "id_region": id_region};
            }
            // cases_terrains[i] = {"x":cx, "y":cy, "id_terrain":tile_selected};
            var e = document.getElementById(""+x+"-"+y);
            e.setAttribute("xlink:href","../imgs/tuiles/"+terrains[tile_selected]["img"]);
        }
        // Objets
        else if(tp_selected=="objets"){
            // cases_objets[i] = {"x":cx, "y":cy, "id_objet":tile_selected};
            if(Object.keys(cases_objets).includes(i)){
                if(cases_objets[i]["id_objet"] != tile_selected){
                    if(!Object.keys(update_o).includes(i)){
                        compteur_modif += 1;
                    }
                    update_o[i] = {"x": cx, "y": cy, "id_objet": tile_selected, "id_region": id_region};
                }
            }
            else{
                if(!Object.keys(new_o).includes(i)){
                    compteur_modif += 1;
                }
                new_o[i] = {"x": cx, "y": cy, "id_objet": tile_selected, "id_region": id_region};
            }
            var e = document.getElementById("o_" + x + "-" + y);
            e.setAttribute("xlink:href", "../imgs/objets/" + objets[tile_selected]["img"]);
        }
        // Ennemis
        else if(tp_selected=="ennemis"){
            if(Object.keys(cases_ennemis).includes(i)){
                if(cases_objets[i]["id_monstre"] != tile_selected){
                    if(!Object.keys(update_e).includes(i)){
                        compteur_modif += 1;
                    }
                    update_e[i] = {"x": cx, "y": cy, "id_monstre": tile_selected, "id_region": id_region};
                }
            }
            else{
                if(!Object.keys(new_e).includes(i)){
                    compteur_modif += 1;
                }
                new_e[i] = {"x": cx, "y": cy, "id_monstre": tile_selected, "id_region": id_region};
            }
            var e = document.getElementById("e_" + x + "-" + y);
            e.setAttribute("xlink:href", "../imgs/ennemis/" + ennemis[tile_selected]["img_base"]);
        }
    }
    // Modifs
    document.getElementById("nb_modifs").innerHTML = compteur_modif;
    if(compteur_modif >= 100){
        document.getElementById("alert_modifs").style.display = "initial";
    }
    else{
        document.getElementById("alert_modifs").style.display = "none";
    }
}

/**
 * FONCTION POUR AFFICHER/RAFRAICHIR LE VIEWPORT
 */

function aff(){
    var tx = 20;
    var ty = 16;
    var tc = 5;
    //
    if(selected_x != null && selected_y != null){
        document.getElementById("selection_params").setAttribute("x", (selected_x + selec_dec_x) * tc);
        document.getElementById("selection_params").setAttribute("y", (selected_y + selec_dec_y) * tc);
    }
    //
    for(x = 0; x < tx; x++){
        for(y = 0; y < ty; y++){
            //
            var cx = x + dec_x;
            var cy = y + dec_y;
            var ii = "" + cx + "-" + cy;
            // LES TERRAINS
            img = "vide.png";
            if(Object.keys(cases_terrains).includes(ii) && !Object.keys(delete_t).includes(ii)){
                if(Object.keys(update_t).includes(ii)){
                    img = terrains[update_t[ii]["id_terrain"]]["img"];
                }else{
                    img = terrains[cases_terrains[ii]["id_terrain"]]["img"];
                }
            }
            if(Object.keys(new_t).includes(ii) ){
                img = terrains[new_t[ii]["id_terrain"]]["img"];
            }
            document.getElementById("" + x + "-" + y).setAttribute("xlink:href","../imgs/tuiles/" + img);
            // LES OBJETS
            img = "rien.png"
            if(Object.keys(cases_objets).includes(ii) && !Object.keys(delete_o).includes(ii)){
                if(Object.keys(update_o).includes(ii)){
                    img = objets[update_o[ii]["id_objet"]]["img"];
                }else{
                    img = objets[cases_objets[ii]["id_objet"]]["img"];
                }
            }
            if(Object.keys(new_o).includes(ii) ){
                img = objets[new_o[ii]["id_objet"]]["img"];
            }
            document.getElementById("o_" + x + "-" + y).setAttribute("xlink:href","../imgs/objets/" + img);
            // LES ENNEMIS
            img = "rien.png"
            if(Object.keys(cases_ennemis).includes(ii) && !Object.keys(delete_e).includes(ii)){
                if(Object.keys(update_e).includes(ii)){
                    img = ennemis[update_e[ii]["id_monstre"]]["img_base"];
                }else{
                    img = ennemis[cases_ennemis[ii]["id_monstre"]]["img_base"];
                }
            }
            if(Object.keys(new_e).includes(ii) ){
                img = ennemis[new_e[ii]["id_monstre"]]["img_base"];
            }
            document.getElementById("e_" + x + "-" + y).setAttribute("xlink:href","../imgs/ennemis/" + img);
        }
    }
}

/**
 * FONCTION POUR CREER UNE NOUVELLE REGION
 */

function new_region(){
    var nom = document.getElementById("new_region_name").value;
    var f = document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i = document.createElement("input");
    i.setAttribute("name", "new_region");
    i.value = nom;
    f.appendChild(i);
    document.body.appendChild(f);
    f.submit();
}

/**
 * FONCTION POUR SUPPRIMER UNE REGION
 */

function delete_region(){
    var nom = "<?php echo $region_selected; ?>";
    var f = document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i = document.createElement("input");
    i.setAttribute("name", "delete_region");
    i.value = nom;
    f.appendChild(i);
    document.body.appendChild(f);
    f.submit();
}

/**
 * FONCTION POUR SAUVEGARDER LES MODIFICATIONS
 */

function save_tiles(){
    var idr = "<?php echo $region_selected; ?>";
    var f = document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i = document.createElement("input");
    i.setAttribute("name", "save_terrain");
    i.setAttribute("value", idr);
    f.appendChild(i);
    var i = document.createElement("input");
    i.setAttribute("name", "dec_x");
    i.setAttribute("value", dec_x);
    f.appendChild(i);
    var i = document.createElement("input");
    i.setAttribute("name", "dec_y");
    i.setAttribute("value", dec_y);
    f.appendChild(i);

    var liste_donnees = [
        ["delete_terrains", delete_t],
        ["update_terrains", update_t],
        ["new_terrains", new_t],

        ["delete_objets", delete_o],
        ["update_objets", update_o],
        ["new_objets", new_o],

        ["delete_ennemis", delete_e],
        ["update_ennemis", update_e],
        ["new_ennemis", new_e],
    ]

    for([nom,data] of liste_donnees){
        var ii = document.createElement("input");
        ii.setAttribute("name", nom);
        ii.setAttribute("value", JSON.stringify(data));
        // ii.value=JSON.stringify(data);
        f.appendChild(ii);
    }

    document.body.appendChild(f);
    console.log(f);
    f.submit();
}

/**
 * FONCTION POUR CHANGER DE MENU D'ITEMS
 */

function set_selection(ii){
    for(i of ["terrains", "objets", "ennemis", "objets_parametres"]){
        if(i == ii){
            document.getElementById(i).style.display = "initial";
        }
        else{
            document.getElementById(i).style.display = "none";
        }
    }
    //
    if(ii == "objets_parametres"){
        mode = "parametres";
        document.getElementById("bts_placer").style.display="none";
        document.getElementById("bts_params").style.display="initial";
    }
    else{
        mode = "placer";
        document.getElementById("bts_placer").style.display="initial";
        document.getElementById("bts_params").style.display="none";
    }
}

/**
 * FONCTIONS POUR GERER L'IMPORT ET EXPORT
 */

function download_text(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function export_region(){
    var texte = {"terrains": cases_terrains, "objets": cases_objets, "ennemis": cases_ennemis};
    var texte = JSON.stringify(texte);
    if(compteur_modif == 0 || confirm("Ceci n'exportera pas les dernières modifications non sauvegardées, voulez-vous quand même exporter cette région ?")){
        download_text("exported_region_" + nom_region + "_.json", texte);
    }
}

function handleFileSelect (e) {
    var files = e.target.files;
    if (files.length < 1) {
        alert('select a file...');
        return;
    }
    var file = files[0];
    var reader = new FileReader();
    reader.onload = onFileLoaded;
    reader.readAsDataURL(file);
}

function onFileLoaded (e) {
    var match = /^data:(.*);base64,(.*)$/.exec(e.target.result);
    // var match = e.target.result;
    if (match == null) {
        throw 'Could not parse result'; // should not happen
    }
    var mimeType = match[1];
    var content = atob(match[2]);
    var confirmation = confirm("Êtes vous bien sur de remplacer tout le contenu de la région actuelle par le contenu du fichier ?");
    if(confirmation){
        var f = document.createElement("form");
        f.setAttribute("method", "POST");
        f.setAttribute("action", "editor.php");
        f.style.display = "none";
        var i = document.createElement("input");
        i.setAttribute("name", "import_data");
        i.setAttribute("value", content);
        f.appendChild(i);
        var ii = document.createElement("input");
        ii.setAttribute("name", "import_region");
        ii.setAttribute("value", id_region);
        f.appendChild(ii);
        document.body.appendChild(f);
        f.submit();
    }

}

function save_parameters(){
    if(selected_x == null || selected_y == null){
        alert("Error, nothing is selected !");
        return;
    }
    var new_parameters = document.getElementById("object_parameters").value;
    var x = selected_x;
    var y = selected_y;
    //
    var f = document.createElement("form");
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    f.style.display = "none";
    //
    var i = document.createElement("input");
    i.setAttribute("name", "update_parameters");
    i.setAttribute("value", new_parameters);
    f.appendChild(i);
    //
    var ii = document.createElement("input");
    ii.setAttribute("name", "id_region");
    ii.setAttribute("value", id_region);
    f.appendChild(ii);
    //
    var ii = document.createElement("input");
    ii.setAttribute("name", "region_selected");
    ii.setAttribute("value", region_selected);
    f.appendChild(ii);
    //
    var i = document.createElement("input");
    i.setAttribute("name", "x");
    i.setAttribute("value", x);
    f.appendChild(i);
    //
    var i = document.createElement("input");
    i.setAttribute("name", "y");
    i.setAttribute("value", y);
    f.appendChild(i);
    // decalage
    var i = document.createElement("input");
    i.setAttribute("name", "dec_x");
    i.setAttribute("value", dec_x);
    f.appendChild(i);
    var i = document.createElement("input");
    i.setAttribute("name", "dec_y");
    i.setAttribute("value", dec_y);
    f.appendChild(i);
    //
    
    //
    document.body.appendChild(f);
    f.submit();
}

var fi = document.getElementById("file_import");
fi.onchange = handleFileSelect;

function import_region(){
    fi.click();
}

/**
 * FONCTIONS POUR GERER LA RECHERCHE D'ELEMENTS
 */

function search_t(){
    var research = document.getElementById("search_t").value;
    for(el of document.getElementsByClassName("liste_terrains")){
        if(el.getAttribute("value").startsWith(research)){
            el.style.display = "inline-flex";
        }
        else{
            el.style.display = "none";
        }
    }
}

function search_o(){
    var research = document.getElementById("search_o").value;
    for(el of document.getElementsByClassName("liste_objets")){
        if(el.getAttribute("value").startsWith(research)){
            el.style.display = "inline-flex";
        }
        else{
            el.style.display = "none";
        }
    }
}

function search_e(){
    var research = document.getElementById("search_e").value;
    for(el of document.getElementsByClassName("liste_ennemis")){
        if(el.getAttribute("value").startsWith(research)){
            el.style.display = "inline-flex";
        }
        else{
            el.style.display = "none";
        }
    }
}

/**
 * FONCTIONS POUR GERER LE CLAVIER
 */

document.addEventListener('keydown', (event) => {
    const nomTouche = event.key;
    if(document.activeElement.getAttribute("id") != "object_parameters"){
        if (nomTouche === 'ArrowUp') {
            dec_y -= 1;
            selec_dec_y += 1;
            aff();
        }
        else if (nomTouche === 'ArrowDown') {
            dec_y += 1;
            selec_dec_y -= 1;
            aff();
        }
        else if (nomTouche === 'ArrowLeft') {
            dec_x -= 1;
            selec_dec_x += 1;
            aff();
        }
        else if (nomTouche === 'ArrowRight') {
            dec_x += 1;
            selec_dec_x -= 1;
            aff();
        }
    }
}, false);

document.addEventListener('keyup', (event) => {
    const nomTouche = event.key;
}, false);


/**
 * FONCTIONS POUR GERER LA SOURIS
 */
if(viewport != null){
    viewport.addEventListener('mousedown', e => {
        dcx, dcy = null, null;
        if(hx != null && hy != null){
            if(mode == "placer"){
                change_case(hx,hy);
            }
            
        }
        is_clicking = true;
    });

    viewport.addEventListener('mousemove', e => {
        if (is_clicking === true && (dcx != hx || dcy != hy)) {
            if(hx != null && hy != null){
                if(mode == "placer"){
                    change_case(hx,hy);
                }
            }
        }
    });

    viewport.addEventListener('mouseup', e => {
        //
        
        if (is_clicking === true) {
            is_clicking = false;
        }
    });
}

function mclick(cx,cy){
    var xx = cx + dec_x;
    var yy = cy + dec_y;
    //
    if(mode == "parametres"){
        selected_x = xx;
        selected_y = yy;
        selec_dec_x = -dec_x;
        selec_dec_y = -dec_y;
        //
        var k = ""+selected_x+"-"+selected_y;
        console.log(k);
        //
        if(Object.keys(cases_objets).includes(k)){
            document.getElementById("selection_params").style.display = "initial";
            document.getElementById("selection_params").setAttribute("x", (selected_x + selec_dec_x) * tc);
            document.getElementById("selection_params").setAttribute("y", (selected_y + selec_dec_y) * tc);
            document.getElementById("object_parameters").value = cases_objets[k]["parametres"];
            document.getElementById("texte_objets").innerHTML = "Vous avez sélectionné une objet de type : "+objets[cases_objets[k]["id_objet"]]["nom"];
        }
    }
    else{
        selected_x = null;
        selected_y = null;
        document.getElementById("object_parameters").value = "";
        document.getElementById("texte_objets").innerHTML = "";
        document.getElementById("selection_params").style.display = "none";
    }
}

function mo(cx,cy){
    hx = cx;
    hy = cy;
}

function ml(cx,cy){
    document.getElementById("hover_case").innerHTML = "x : " + (dec_x + cx) + " , y : " + (dec_y + cy);
    if(hx == cx && hy == cy){
        hx = null;
        hy = null;
    }
}

</script>