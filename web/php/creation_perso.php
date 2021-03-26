<!DOCTYPE html>
<!-- Entête page internet -->
<html>
    <head>
        <meta charset="utf-8">
        <title>Nom jeu - Création personnage</title>
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <div class="creation_perso">
    <!-- Titre création du personnage -->
        <h1>Creation personnage</h1>


        <!-- Menu choix sexe et classe -->

        <!-- Bouton continuer, qui enregistre nos choix et nous redirige vers le menu de création -->
        <!-- En sauvegardant nos choix de classe et de sexe, et nous propose des tenues adapté -->
            <div class="continuer_creation">
            <button class="bouton_continuer_creation">CONTINUER</button>
            </div>


            
                <!-- Menu de création -->
                <!-- Après le choix du sexe et de la classe -->
                <div class="menu_creation_perso column">
                    <div class="row">
                        <button><</button><a>Tete<span id="num_tete_sel">1</span>/6</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>Couleur de peau<span id="num_cdp_sel">1</span>/6</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>Cheveux<span id="num_cheveux_sel">1</span>/6</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>Barbe<span id="num_barbe_sel">1</span>/6</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>Haut<span id="num_haut_sel">1</span>/6</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>Bas<span id="num_bas_sel">1</span>/6</a><button>></button>
                    </div>
                    <div class="row">
                        <button><</button><a>Pied<span id="num_pied_sel">1</span>/6</a><button>></button>
                    </div>
                </div>

                
            <!-- Aperçu du sprite avec ses changements -->
            <div class="sprite_creation">


                    <!-- Bouton valier, qui enregistre toutes les modifs dans la BDD -->
                    <div class="valider_creation">
                    </div>

            <div class="">

            </div>

        </div>

    </body>
</html>