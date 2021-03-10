// Ip auquel se connecter, a recevoir du menu principal
// Ici pour l'instant car il n'y a pas encore de menu principal
const IP = "localhost";
// Port auquel se connecter, a recevoir du menu principal
// Ici pour l'instant car il n'y a pas encore de menu principal
const PORT = 6546;

var websocket = null; // On prépare la variable globale

function start_websocket() {
    /**
     * Fonction qui initialise et lance le serveur websocket
     */

    // On se connecte au websocket
    websocket = new WebSocket("ws://" + IP + ":" + PORT + "/");

    // Quand il y a des erreurs
    websocket.onerror = function() {
        // On affiche un message d'erreur
        alert("There was an error during connection");
        // On peut aussi renvoyer vers la page d'accueil
    };

    // On relie le websocket a notre fonction qui gere les messages recus
    websocket.onmessage = on_message;
}

// Fonction pour envoyer des messages
function send_mes(message) {
    /**
     * Envoie un message au websocket en convertissant le message en JSON
     */
    // On convertit en json
    message = JSON.stringify(message);
    // On envoie le message
    websocket.send(message);
}

function on_message(event) {
    // On recoit les informations
    data = JSON.parse(event.data);
    // On traite les informations
    switch (data.action) {

        case 'exemple':
            // Exemple d'action que le serveur envoie
            break;

        case 'autre_exemple':
            // Autre exemple d'action à gerer
            break;

        default:
            // Il faut faire attention aux types d'actions que l'on gère
            // Et ne pas oublier les "break;" à la fin de chaque cas
            console.error("unsupported event", data);
    }
}