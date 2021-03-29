<!DOCTYPE html>
<!-- Entête page internet -->
<html>
    <head>
        <meta charset="utf-8">
        <title>Nom jeu - Création personnage</title>

        <link rel="stylesheet" href="../css/style_crea_perso.css">
    </head>
    <div class="creation_perso">
    <!-- Titre création du personnage -->
        <h1>Creation personnage</h1>

            
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
                        <button class="validation_perso_creation" href="">VALIDER</button>
                    </div>


                    
        </div>

    </body>
</html>