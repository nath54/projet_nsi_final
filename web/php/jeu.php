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
                        <div class="column">
                            <div>
                                <p>Pseudo</p>
                            </div>
                            <div>
                                <label>Vie</label>
                                <progress></progress>
                            </div>
                            <div>
                                <label>Mana</label>
                                <progress></progress>
                            </div>
                        </div>
                        <div class="column">
                            <div>
                                <p>Image de profil</p>
                                <img>
                            </div>
                            <div>
                                <button>Inventaire</button>
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