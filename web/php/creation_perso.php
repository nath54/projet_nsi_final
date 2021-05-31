<!DOCTYPE html>
<!-- Entête page internet -->
<html>
<?php

include_once "../../includes/init.php";
include_once "../../includes/bdd.php";

$db = load_db("../../includes/config.json");

// On récupère les vêtements du joueurs dans la base de données
$req = "SELECT id_tete, id_cheveux, id_barbe, id_haut, id_bas, id_pieds FROM utilisateurs WHERE id_utilisateur=:id_player";
$vars = array(":id_player"=>$_SESSION["player_id"]);

$res = requete_prep($db, $req, $vars)[0];
if(count($res)==0){
    $_SESSION["error"] = "Il y a eu une erreur lors de la création du personnage, votre compte a-t-il bien été créé ?";
    header("Location: ../php/accueil.php");
}

$tete = $res['id_tete'];
$cheveux = $res["id_cheveux"];
$barbe = $res["id_barbe"];
$haut = $res["id_haut"];
$bas = $res["id_bas"];
$pied = $res["id_pieds"];

$txt = "<script>";
$txt.="var selectionnes = {";
$txt.="'tete':$tete,";
$txt.="'cheveux':$cheveux,";
$txt.="'barbe':$barbe,";
$txt.="'haut':$haut,";
$txt.="'bas':$bas,";
$txt.="'pied':$pied";
$txt.="}";
$txt.="</script>";

echo $txt;

?>
    <script src="../js/customisation_perso_data.js"></script>
    <body class="column" onload="init_imgs();">
    <head>
        <div>
            <!-- Div des boutons -->
            <div id="bouton_header">

                <!-- Bouton accueil -->
                <div class="accueil_bouton">
                    <a href="accueil.php"><img class="maison" src="../imgs/header/maison.png"></a>
                </div>

                <!-- Bouton compte -->
                <div class="compte_bouton">
                    <a href="inscription.php"><img class="login" src="../imgs/header/login.png"></a>
                </div>

                <!-- Bouton parametre -->
                <div class="parametre_bouton">
                    <img class="engrenage" src="../imgs/header/engrenage.png">
                </div>
            </div>

            <!-- Titre création du personnage -->
            <h1>Creation personnage</h1>
        </div>
            <!-- Nom du jeu + reliement au css -->
            <meta charset="utf-8">
            <title>Nom jeu - Création personnage</title>
            <link rel="stylesheet" href="../css/style_crea_perso.css">

            <!-- Importation des fonts -->
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    </head>

        <!-- Header -->

        <div class="row">

            <div class="creation_perso">


                <!-- Menu de création -->
                <!-- Après le choix du sexe et de la classe -->
                <!-- &nbsp = espace -->
                <div class="menu_creation_perso column">
                    <div class="row">
                        <button onclick="clic('tete',-1);">&#60</button><a>&nbsp Tete <span id="choix_tete">1</span>/<span id="taille_tete">1</span> &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic('tete',+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic('cheveux',-1);">&#60</button><a>&nbsp Cheveux <span id="choix_cheveux">1</span>/<span id="taille_cheveux">1</span> &nbsp</a><button onclick="clic('cheveux',+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic('barbe',-1);">&#60</button><a>&nbsp Barbe <span id="choix_barbe">1</span>/<span id="taille_barbe">1</span> &nbsp&nbsp&nbsp</a><button onclick="clic('barbe',+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic('haut',-1);">&#60</button><a>&nbsp Haut <span id="choix_haut">1</span>/<span id="taille_haut">1</span> &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic('haut',+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic('bas',-1);">&#60</button><a>&nbsp Bas <span id="choix_bas">1</span>/<span id="taille_bas">1</span> &nbsp&nbsp&nbsp&nbsp&nbsp</a><button onclick="clic('bas',+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic('pied',-1);">&#60</button><a>&nbsp Pied <span id="choix_pied">1</span>/<span id="taille_pied">1</span> &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic('pied',+1);">&#62</button>
                    </div>
                </div>


                <!-- Aperçu du sprite avec ses changements -->
                <div class="sprite_creation">

                    <!-- Bouton valier, qui enregistre toutes les modifs dans la BDD -->
                    <div class="valider_creation">
                        <form method="POST" action="post_creation.php">
                            <input id="reponse_tete" name="tete" type="hidden">
                            <input id="reponse_cheveux" name="cheveux" type="hidden">
                            <input id="reponse_barbe" name="barbe" type="hidden">
                            <input id="reponse_haut" name="haut" type="hidden">
                            <input id="reponse_bas" name="bas" type="hidden">
                            <input id="reponse_pied" name="pied" type="hidden">
                            <button class="validation_perso_creation" onclick="submit()"><a>VALIDER</a></button>
                        </form>
                    </div>


                    <!-- Bouton precedent, qui revient au formulaire d'inscription -->
                    <div class="precedent_creation">
                        <button class="precedent_perso_creation" href="accueil.php"><a>PRECEDENT</a></button>
                    </div>

                </div>
            </div>

            <div id="sprite">
                <svg viewBox="0 0 128 128" style="border:1px solid black; width:500px;" id="viewport" xmlns="file:///C:/Users/El%C3%A8ve/Downloads/sprite_test.svg">
                    <image id="img_corps" x=0 y=0 width=128 height=128 xlink:href="../imgs/sprites/sprite_fixe_droit.png" />
                    <image id="img_haut" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="img_bas" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="img_pied" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="img_barbe" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="img_cheveux" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="img_tete" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                </svg>
            </div>
        </div>
    </body>
</html>

<!-- Script qui permet d'afficher le numéro suivant des vetements  -->
<script>
    function clic(cat, delta){
        var taille = images_corps[cat].length;
        selectionnes[cat]+=delta;
        if(selectionnes[cat] <= 0) selectionnes[cat]=taille;
        if(selectionnes[cat] > taille) selectionnes[cat]=1;
        //
        var img = "../imgs/custom_perso/"+images_corps[cat][selectionnes[cat]-1];
        document.getElementById("img_"+cat).setAttribute("xlink:href", img);
        //
        document.getElementById("choix_"+cat).innerHTML = selectionnes[cat];
        document.getElementById("reponse_"+cat).value = selectionnes[cat];
    }

function init_imgs(){
    for(cat of Object.keys(selectionnes)){
        var taille = images_corps[cat].length;
        document.getElementById("taille_"+cat).innerHTML = taille;
        document.getElementById("choix_"+cat).innerHTML = selectionnes[cat];
        var img = "../imgs/custom_perso/"+images_corps[cat][selectionnes[cat]-1];
        document.getElementById("img_"+cat).setAttribute("xlink:href", img);
        document.getElementById("reponse_"+cat).value = selectionnes[cat];
    }
}

</script>
