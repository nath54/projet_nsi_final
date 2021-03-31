<!DOCTYPE html>
<!-- Entête page internet -->
<html>
    <head>
        <!-- Nom du jeu + reliement au css -->
        <meta charset="utf-8">
        <title>Nom jeu - Création personnage</title>
        <link rel="stylesheet" href="../css/style_crea_perso.css">

        <!-- Importation des fonts -->
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet"> 



    </head>
    <div class="creation_perso">
    <!-- Titre création du personnage -->
        <h1>Creation personnage</h1>



<!--                 <script>
                function clic(a,b){
                    var ligne = document.getElementById("choix"+a);
                    var n = parseInt(ligne.innerHTML);
                    n = n+b;
                    if n>6{
                        n=n-6
                        }
                    if n=<0{
                    ligne.innerHTML = n;
                    }
                }              -->

                <!-- Script qui permet d'afficher le numéro suivant du choix -->
                <script>
                function clic(a,b){
                    var ligne = document.getElementById("choix"+a);
                    var n = parseInt(ligne.innerHTML);
                    n = ((n+b-1)%6)+1;
                    ligne.innerHTML = n;
                }               
                </script>
            
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

    </body>
</html>