<?php
include_once "../includes/init.php";
include_once "../includes/bdd.php";

$db = load_db();

$requete = "SELECT * FROM terrain;";
$terrains = array();

$r = requete_prep($db, $requete);
if(!$r!=NULL){
    alert("Il y a eu une erreur !");
}
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $terrains[$i] = array("nom"=>$nom, "img"=>$img);
}


//

$liste_regions = array();
foreach(requete_prep($db, "SELECT * FROM regions") as $i=>$data){
    $liste_regions[$data["nom"]]=$data["id_region"];
}

$region_selected = "";
if(isset($_POST["region_selected"])){
    if(in_array($_POST["region_selected"], array_keys($liste_regions))){
        $region_selected = $_POST["region_selected"];
    }
}

if(isset($_POST["delete_region"])){
    if(in_array($_POST["delete_region"], array_keys($liste_regions))){
        $query = "DELETE FROM regions WHERE nom=:nom";
        $vars = array(":nom"=>$_POST["delete_region"]);
        if(!action_prep($db, $query, $vars)){
            alert("Il y a eu une erreur lors de la suppression de la région !");
        }
        else{
            unset($liste_regions[$_POST["delete_region"]]);
        }
    }
    else{
        alert("La region n'existe pas !");
    }
}


if(isset($_POST["new_region"])){
    if($_POST["new_region"]!="" && !in_array($_POST["new_region"], $liste_regions)){
        $query = "INSERT INTO regions SET nom=:nom, tx=100, ty=100;";
        $vars = array(":nom"=>$_POST["new_region"]);
        if(!action_prep($db, $query, $vars)){
            alert("Il y a eu une erreur lors de la création de la région !");
        }
        else{
            $region_selected = $_POST["new_region"];
            $liste_regions[$_POST["new_region"]]=$db->lastInsertId();
        }
    }
    else{
        alert("Une région porte déjà le même nom !");
    }
}

$cases_terrains = array();

if(isset($_POST["save_terrain"]) && isset($_POST["data_terrain"])){
    $nom_region = $_POST["save_terrain"];
    $datas = json_decode($_POST["data_terrain"], true);
    // echo $_POST["data_terrain"];
    // On nettoie
    $query = "DELETE FROM regions_terrains WHERE id_terrain=:idr";
    $vars = array(":idr"=>$liste_regions[$nom_region]);
    if(!action_prep($db, $query, $vars)){
        console.log("probleme suppression");
    }
    // On remplace
    foreach($datas as $i=>$data){
        $query = "INSERT INTO regions_terrains SET x=:x, y=:y, id_terrain=:tile, id_region=:idr";
        // echo $data["x"].", ".$data["y"]." : ".$data["tile"]." - ";
        $vars = array(":x"=>$data["x"], ":y"=>$data["y"], ":tile"=>$data["tile"], ":idr"=>$liste_regions[$nom_region]);
        if(!action_prep($db, $query, $vars)){
            console.log("probleme insertion");
        }
    }
    $region_selected = $nom_region;
}


if($region_selected!=""){
    $requested = "SELECT * FROM regions_terrains WHERE id_region=:idr";
    $vars = array(":idr"=>$liste_regions[$region_selected]);
    foreach(requete_prep($db, $requested, $vars) as $i=>$data){
        $x=$data["x"];
        $y=$data["y"];
        $tile=$data["id_terrain"];
        $cases_terrains["$x-$y"]=array("x"=>$x, "y"=>$y, "tile"=>$tile);
    }
}


$jsone = json_encode($terrains);
script("var terrains = JSON.parse('$jsone');");



if(count($cases_terrains)>0){
    $jsone = json_encode($cases_terrains);
    script("var cases_terrains = JSON.parse('$jsone');");
}
else{
    script("var cases_terrains = {};");
}

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

            <div class="row">

                <select id="region_sel" onchange="change_map()">

                    <option value="" <?php if($region_selected==""){ echo "selected"; } ?>>Aucune</option>
                    <?php

                        // Il faudra peut-être changer les infos de la BDD
                        foreach($liste_regions as $nom=>$id){
                            $sel="";
                            if($nom==$region_selected){
                                $sel="selected";
                            }
                            echo "<option $sel>$nom</option>";
                        }

                    ?>

                </select>

                <div>
                    <?php

                    if($region_selected!=""){
                        echo "<button onclick=\"delete_region();\">Supprimer la région choisie</button>";
                        echo "<button onclick=\"save_tiles();\">Sauvegarder la région choisie</button>";
                    }

                    ?>
                </div>

                <div class="row">
                    <label>New region</label>
                    <input id="new_region_name" type="text" placeholder="nom de la region">
                    <button onclick="new_region();">Créer</button>
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
                    $tx = 20;
                    $ty = 16;
                    $tc = 5;
                    $dx = 0;
                    $dy = 0;
                    for($x=0; $x<$tx; $x++){
                        for($y=0; $y<$ty; $y++){
                            $cx = $x * $tc + $dx;
                            $cy = $y * $tc + $dy;
                            $idd = "$x-$y";
                            $src="../imgs/tuiles/vide.png";
                            if(isset($cases_terrains[$idd])){
                                $img = $terrains[$cases_terrains[$idd]["tile"]]["img"];
                                $src="../imgs/tuiles/$img";
                            }
                            echo "<image id=\"$x-$y\" xlink:href=\"$src\" x=\"$cx\" y=\"$cy\" width=\"$tc\" height=\"$tc\" onmouseover=\"mo($x,$y);\" onmouseout=\"ml($x,$y);\" class=\"case\"></image>";
                        }
                    }
                    echo "</svg>";
                }
                else{
                    echo "<p>Aucune région n'a été choisie</p>";
                }
            ?>
            </div>

            <!-- tiles menu -->

            <div style="overflow:auto;width:100%;height:90%;">

                <!-- tile selected to paint -->
                <div>

                </div>

                <!-- Select tiles -->

                <div class="liste_tiles">

                    <?php

                        foreach($terrains as $i=>$data){
                            $img = $data["img"];
                            $nom = $data["nom"];
                            $sel = "";
                            if($i==0){ // au début, l'herbe sera selectionne par defaut
                                $sel = "liste_element_selectione";
                            }
                            echo "<div id=\"liste_elt_$i\" class=\"liste_element $sel\" onclick=\"select_tile($i);\"><img class=\"img_liste_element\" src=\"../imgs/tuiles/$img\" /><label>$nom</label></div>";
                        }

                    ?>

                </div>

            </div>

        </div>
    </body>
</html>
<script>

var dcx = null;
var dcy = null;

var tile_selected = 0;
var dec_x = 0;
var dec_y = 0;

var is_clicking = false;
var hx=null;
var hy=null;
var viewport = document.getElementById("viewport");

function arrayRemove(arr, value) {
    return arr.filter(function(ele){
        return ele != value;
    });
}

viewport.addEventListener('mousedown', e => {
    dcx,dcy=null,null;
    if(hx!=null && hy!=null){
        change_case(hx,hy);
    }
    is_clicking = true;
});

viewport.addEventListener('mousemove', e => {
    if (is_clicking === true && (dcx!=hx || dcy!=hy)) {
        if(hx!=null && hy!=null){
            change_case(hx,hy);
        }
    }
});

viewport.addEventListener('mouseup', e => {
    if (is_clicking === true) {
        is_clicking = false;
    }
});

function mo(cx,cy){
    hx = cx;
    hy = cy;
}

function ml(cx,cy){
    if(hx==cx && hy==cy){
        hx=null;
        hy=null;
    }
}


function change_map(){
    var nom=document.getElementById("region_sel").value;
    var f=document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i=document.createElement("input");
    i.setAttribute("name", "region_selected");
    i.value=nom;
    f.appendChild(i);
    document.body.appendChild(f);
    f.submit();
}

function change_case(x, y){
    //
    // console.log(x,y);
    //
    var cx = x + dec_x;
    var cy = y + dec_y;
    dcx,dcy=cx,cy;
    var i = ""+cx+"-"+cy;
    if(tile_selected==0){
        if(Object.keys(cases_terrains).includes(i)){
            delete cases_terrains[i];
        }
    }
    else{
        cases_terrains[i] = {"x":cx, "y":cy, "tile":tile_selected};
    }
    var i = document.getElementById(""+x+"-"+y);
    i.setAttribute("xlink:href","../imgs/tuiles/"+terrains[tile_selected]["img"]);
}

function aff(){
    var tx = 20;
    var ty = 16;
    var tc = 5;
    for(x=0; x<tx; x++){
        for(y=0; y<ty; y++){
            var cx = x + dec_x;
            var cy = y + dec_y;
            img = "vide.png";
            if(Object.keys(cases_terrains).includes(""+cx+"-"+cy)){
                img=terrains[cases_terrains[""+cx+"-"+cy]["tile"]]["img"];
            }
            document.getElementById(""+x+"-"+y).setAttribute("xlink:href","../imgs/tuiles/"+img);
        }
    }
}

function new_region(){
    var nom = document.getElementById("new_region_name").value;
    var f=document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i=document.createElement("input");
    i.setAttribute("name", "new_region");
    i.value=nom;
    f.appendChild(i);
    document.body.appendChild(f);
    f.submit();
}

function delete_region(){
    var nom = "<?php echo $region_selected; ?>";
    var f=document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i=document.createElement("input");
    i.setAttribute("name", "delete_region");
    i.value=nom;
    f.appendChild(i);
    document.body.appendChild(f);
    f.submit();
}

function select_tile(id_tile){
    if(id_tile==tile_selected){
        return;
    }
    var ad = document.getElementById("liste_elt_"+tile_selected);
    ad.classList.remove("liste_element_selectione");
    var d = document.getElementById("liste_elt_"+id_tile);
    d.classList.add("liste_element_selectione");
    tile_selected = id_tile;
}

function save_tiles(){
    var nom = "<?php echo $region_selected; ?>";
    var f=document.createElement("form");
    f.setAttribute("style","display:none;")
    f.setAttribute("method", "POST");
    f.setAttribute("action", "editor.php");
    var i=document.createElement("input");
    i.setAttribute("name", "save_terrain");
    i.value=nom;
    f.appendChild(i);
    var ii=document.createElement("input");
    ii.setAttribute("name", "data_terrain");
    ii.value=JSON.stringify(cases_terrains);
    f.appendChild(ii);
    document.body.appendChild(f);
    f.submit();
}

document.addEventListener('keydown', (event) => {
    const nomTouche = event.key;
    if (nomTouche === 'ArrowUp') {
        dec_y-=1;
        aff();
    }
    else if (nomTouche === 'ArrowDown') {
        dec_y+=1;
        aff();
    }
    else if (nomTouche === 'ArrowLeft') {
        dec_x-=1;
        aff();
    }
    else if (nomTouche === 'ArrowRight') {
        dec_x+=1;
        aff();
    }
}, false);

document.addEventListener('keyup', (event) => {
    const nomTouche = event.key;
}, false);

</script>