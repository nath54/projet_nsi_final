<?php
include_once "../includes/init.php";
include_once "../includes/bdd.php";

$db = load_db();

$tx = 0;
$ty = 0;

$requete = "SELECT * FROM terrain;";
$terrains = array();
$style = "<style>";


$r = requete_prep($db, $requete);
if(!$r!=NULL){
    alert("Il y a eu une erreur !");
}
foreach($r as $i=>$data){
    $nom = $data["nom"];
    $img = $data["image_"];
    $terrains[$i] = $nom;
    $style.=".$nom{ background-img:url(\"../imgs/tuiles/$img.png\"); }\n";
}
$style.="</style>";


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
    if(in_array($_POST["delete_region"], $liste_regions)){
        $query = "DELETE FROM regions WHERE nom=:nom";
        $vars = array(":nom"=>$_POST["delete_region"]);
        if(!action_prep($db, $query, $vars)){
            alert("Il y a eu une erreur lors de la suppression de la région !");
        }
    }
    else{
        alert("La region n'existe pas !");
    }
}


if(isset($_POST["new_region"])){
    alert($_POST["new_region"]);
    if($_POST["new_region"]!="" && !in_array($_POST["new_region"], $liste_regions)){
        $query = "INSERT INTO regions SET nom=:nom, tx=100, ty=100;";
        $vars = array(":nom"=>$_POST["new_region"]);
        if(!action_prep($db, $query, $vars)){
            alert("Il y a eu une erreur lors de la création de la région !");
        }
    }
    else{
        alert("Une région porte déjà le même nom !");
    }
}



?>
<script>

var tuile_selected = "herbe";

</script>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Editeur de map</title>
        <link href="editor.css" rel="stylesheet" />
        <?php echo $style; ?>
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

            <div>
                <!-- TODO -->
                <svg viewBox="0 0 100 100" id="kln" style="display:block;margin:auto;background:white;border:1px solid black;" xmlns="http://www.w3.org/2000/svg">
                    <?php
                        for($x=0; $x<$tx; $x++){
                            for($y=0; $y<$ty; $y++){
                                $cx = $x * $tc;
                                $cy = $y * $tc;
                                echo "<rect x=\"$cx\" y=\"$cy\" width=\"$tc\" height=\"$tc\" id=\"\"onclick=\"change_case($cx, $cy); \" style=\"herbe\"></rect>";
                            }
                        }
                    ?>
                </svg>
            </div>

            <!-- tiles menu -->

            <div>

                <!-- TODO -->

            </div>

        </div>
    </body>
</html>
<script>

function change_map(){
    var nom=document.getElementById("region_sel").value;
    var f=document.createElement("form");
    f.setAttribute("method", "POST");;
    f.setAttribute("action", "editor.php");;
    var i=document.createElement("input");
    i.setAttribute("name", "region_selected");
    i.value=nom;
    document.body.appendChild(f);
    f.submit();
}

function change_case(x, y){
    //
}

function new_region(){
    var nom = document.getElementById("new_region_name").value;
    var f=document.createElement("form");
    f.setAttribute("method", "POST");;
    f.setAttribute("action", "editor.php");;
    var i=document.createElement("input");
    i.setAttribute("name", "new_region");
    i.value=nom;
    document.body.appendChild(f);
    f.submit();
}

function delete_region(){
    var nom = "<?php echo $region_selected; ?>";
    var f=document.createElement("form");
    f.setAttribute("method", "POST");;
    f.setAttribute("action", "editor.php");;
    var i=document.createElement("input");
    i.setAttribute("name", "delete_region");
    i.value=nom;
    document.body.appendChild(f);
    f.submit();
}

</script>