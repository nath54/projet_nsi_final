// // Ip auquel se connecter, a recevoir du menu principal
// // Ici pour l'instant car il n'y a pas encore de menu principal
// const IP = "localhost";
// // Port auquel se connecter, a recevoir du menu principal
// // Ici pour l'instant car il n'y a pas encore de menu principal
// const PORT = 6546;

// !!! important !!!
// On initiera la variable ws_url avec le php avant d'insérer ce script
// !!! important !!!

window.websocket = null; // On prépare la variable globale

function start_websocket(ws_url) {
    /**
     * Fonction qui initialise et lance le serveur websocket
     *
     * @author Nathan
     */

    // On se connecte au websocket
    // websocket = new WebSocket("ws://" + IP + ":" + PORT + "/");
    ws_url += "/";
    console.log(ws_url);
    window.websocket = new WebSocket(ws_url);

    // Quand il y a des erreurs
    window.websocket.onerror = function() {
        // On affiche un message d'erreur
        alert("There was an error during connection");
        // On peut aussi renvoyer vers la page d'accueil
    };

    // On relie le websocket a notre fonction qui gere les messages recus
    window.websocket.onmessage = on_message;

    // On attent qu'il soit pret
    window.websocket.onopen = launch2;
}

// Fonction pour envoyer des messages
function ws_send(message) {
    /**
     * Envoie un message au websocket en convertissant le message en JSON
     *
     * @params message : Message a envoyer, sous la forme d'un dictionnaire
     *
     * @author Nathan
     */
    // On convertit en json
    message = JSON.stringify(message);
    // On envoie le message
    window.websocket.send(message);
}

function on_message(event) {
    /**
     * Fonction qui gere tous les messages recus du serveur
     *
     * @params event : Evenement message géré par js
     *
     * @author Nathan
     */
    // On recoit les informations
    data = JSON.parse(event.data);
    console.log("get on websocket : ", data);
    // On traite les informations
    switch (data.action) {

        case 'infos_perso':
            for (cle of["x", "y", "vie", "vie_max", "mana", "mana_max", "exp", "exp_max", "region_actu"]) {
                personnage[cle] = data[cle];
            }

            if (en_chargement) {
                en_chargement = false;
                aff();
            }
            break;

        case 'position_perso':
            personnage.x = data.x;
            personnage.y = data.y;
            aff();
            break;

        default:
            // Il faut faire attention aux types d'actions que l'on gère
            // Et ne pas oublier les "break;" à la fin de chaque cas
            console.error("unsupported event", data);
    }
}