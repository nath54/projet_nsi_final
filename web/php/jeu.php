<?php


?>
<html>

    <head>
        <meta charset="utf-8" />
        <title>Jeu</title>
        <link href="../css/style_jeu.css" rel="stylesheet" />
    </head>

    <body>

        <div class="row">

            <div class="column" id="div_row_1">

                <div class="row">
                    <p>Nom de la région actuelle</p>
                    <p>Nombre de personne qu'il y a dans la région</p>
                </div>

                <div id="div_viewport">

                    <svg viewBox="0 0 100 50" id="viewport" xmlns="http://www.w3.org/2000/svg">
                    </svg>

                </div>

            </div>

            <div class="column" id="div_row_2">
                <div id="div_account">
                    <div class="row">
                        <div class="column" id="progress_div">
                            <div id="pseudo_div">
                                <b>Pseudo</b>
                            </div>
                            <div class="column">
                                <label for="progress_exp">Experience : <span id="exp_value">70/100</span></label>
                                <progress id="progress_exp" max="100" value="20"></progress>
                                <b>Niveau <span id="niveau_profil">1</span></b>
                            </div>
                            <hr />
                            <div class="column">
                                <label for="progress_vie">Vie : <span id="vie_value">70/100</span></label>
                                <progress id="progress_vie" max="100" value="70"></progress>
                            </div>
                            <div class="column">
                                <label for="progress_mana">Mana : <span id="mana_value">70/100</span></label>
                                <progress id="progress_mana" max="100" value="70"></progress>
                            </div>
                        </div>
                        <div class="column" id="pp_and_buttons">
                            <div id="image_profile">
                                <img class="profile_picture" src="../../imgs/tests/pp_null.png">
                            </div>
                            <div id="row_buttons_ui_1" class="row">
                                <button id="bag_button" class="button_ui_game_1"></button>
                                <button id="button_2" class="button_ui_game_1">?</button>
                                <button id="button_3" class="button_ui_game_1">?</button>
                            </div>
                        </div>
                    </div>

                </div>

                <div id="div_chat">
                    <b>Chat :</b>
                    <div id="chat_mess">
                        <p><b class="cl_chat_system">Système : </b>Bienvenue dans le jeu !</p>
                    </div>
                    <div>
                        <input id="input_chat" type="text" placeholder="Message à envoyer">
                        <button>Envoyer</button>
                    </div>
                </div>

            </div>

        </div>

    </body>

</html>