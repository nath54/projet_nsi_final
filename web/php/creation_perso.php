<!DOCTYPE html>
<!-- Entête page internet -->
<html>
<?php 
session_start();
print_r( $_SESSION['error'] ); ?>
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

    <body class="column">
        <!-- Header -->

        <div class="row">

            <div class="creation_perso">


                <!-- Menu de création -->
                <!-- Après le choix du sexe et de la classe -->
                <!-- &nbsp = espace -->
                <div class="menu_creation_perso column">
                    <div class="row">
                        <button onclick="clic(1,-1);">&#60</button><a>&nbsp Tete <span id="choix1">1</span>/6 &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic(1,+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic(2,-1);">&#60</button><a>&nbsp Cheveux <span id="choix2">1</span>/6 &nbsp</a><button onclick="clic(2,+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic(3,-1);">&#60</button><a>&nbsp Barbe <span id="choix3">1</span>/6 &nbsp&nbsp&nbsp</a><button onclick="clic(3,+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic(4,-1);">&#60</button><a>&nbsp Haut <span id="choix4">1</span>/6 &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic(4,+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic(5,-1);">&#60</button><a>&nbsp Bas <span id="choix5">1</span>/6 &nbsp&nbsp&nbsp&nbsp&nbsp</a><button onclick="clic(5,+1);">&#62</button>
                    </div>
                    <div class="row">
                        <button onclick="clic(6,-1);">&#60</button><a>&nbsp Pied <span id="choix6">1</span>/6 &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic(6,+1);">&#62</button>
                    </div>
                </div>


                <!-- Aperçu du sprite avec ses changements -->
                <div class="sprite_creation">

                    <!-- Bouton valier, qui enregistre toutes les modifs dans la BDD -->
                    <div class="valider_creation">
                        <button class="validation_perso_creation" href=""><a>VALIDER</a></button>
                    </div>


                    <!-- Bouton precedent, qui revient au formulaire d'inscription -->
                    <div class="precedent_creation">
                        <button class="precedent_perso_creation" href=""><a>PRECEDENT</a></button>
                    </div>

                </div>

            </div>

            <div id="sprite">
                <svg viewBox="0 0 128 128" style="border:1px solid black; width:500px;" id="viewport" xmlns="http://www.w3.org/2000/svg">
                    <image id="tete" x=0 y=0 width=128 height=128 xlink:href="../imgs/sprites/sprite_fixe_droit.png" />
                    <image id="cheveux" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="barbe" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="haut" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="bas" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                    <image id="pied" x=0 y=0 width=128 height=128 xlink:href="chemin-image" />
                </svg>
            </div>
        </div>
    </body>
</html>

<!-- Script qui permet d'afficher le numéro suivant des vetements  -->
<script>
    function clic(a,b){
        var ligne = document.getElementById("choix"+a);
        var n = parseInt(ligne.innerHTML);
        n = n+b;
        if (n>6){
            n=n-6;
            }
        if (n<=0){
        n = n+6;
        }
        ligne.innerHTML = n;
    }
</script>
