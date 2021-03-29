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

            
                <!-- Menu de création -->
                <!-- Après le choix du sexe et de la classe -->
                <!-- &nbsp = espace -->
                <div class="menu_creation_perso column">
                    <div class="row">
                        <button onclick="clic(1,-1);"><</button><a>&nbsp Tete<span id="choix1">1</span>/6 &nbsp&nbsp&nbsp&nbsp</a><button onclick="clic(1,+1);">></button>
                    </div>
                    <div class="row">
                        <button><</button><a>&nbsp Cheveux<span id="num_cheveux_sel">1</span>/6 &nbsp</a><button onclick="clic(1,+1);">></button>
                    </div>
                    <div class="row">
                        <button><</button><a>&nbsp Barbe<span id="num_barbe_sel">1</span>/6 &nbsp&nbsp&nbsp</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>&nbsp Haut<span id="num_haut_sel">1</span>/6 &nbsp&nbsp&nbsp&nbsp</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>&nbsp Bas<span id="num_bas_sel">1</span>/6 &nbsp&nbsp&nbsp&nbsp&nbsp</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>&nbsp Pied<span id="num_pied_sel">1</span>/6 &nbsp&nbsp&nbsp&nbsp</a><button>></button>
                    </div>
                </div>

                
            <!-- Aperçu du sprite avec ses changements -->
            <div class="sprite_creation">


                    <!-- Bouton valier, qui enregistre toutes les modifs dans la BDD -->
                    <div class="valider_creation">
                        <button class="validation_perso_creation" href="">VALIDER</button>
                    </div>

                    


                    
        </div>

    </body>
</html>