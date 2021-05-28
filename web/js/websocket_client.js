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
    window.websocket = new WebSocket(ws_url);

    // Quand il y a des erreurs
    window.websocket.onerror = function() {
        // On affiche un message d'erreur
        alert("There was an error during connection");
        // On peut aussi renvoyer vers la page d'accueil
        window.location.href = "accueil.php";
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
    // console.log("get on websocket : ", data);
    // On traite les informations
    switch (data.action) {

        case 'prob_connection':
            alert(data["message"]);
            window.location.href = "accueil.php";
            break;

        case 'infos_perso':
            delete data['action']
            personnage = data;
            personnage.competences = JSON.parse(personnage.competences);

            if (en_chargement) {
                en_chargement = false;
                document.getElementById("loading").style.display = "none";
                aff();
            }

            update_competence();
            break;

        case 'position_perso':
            personnage.x = data.x;
            personnage.y = data.y;
            aff();
            break;

        case 'debug':
        case 'alert':
            alert(data.message);
            break;

        case 'joueur':
            var id_j = parseInt(data.id_perso);
            if (id_j != personnage.id_perso) {
                delete data['action'];
                autres_joueurs[id_j] = data;
                aff();
            }
            break;

        case 'vie':
            var value = parseInt(data.value);
            var max_v = parseInt(data.max_v);
            personnage.vie = value;
            personnage.vie_max = max_v;
            document.getElementById("progress_vie").value = value;
            document.getElementById("progress_vie").max = max_v;
            document.getElementById("text_vie").innerHTML = "" + value + "/" + max_v;
            break;

        case 'mana':
            var value = parseInt(data.value);
            var max_v = parseInt(data.max_v);
            personnage.mana = value;
            personnage.mana_max = max_v;
            document.getElementById("progress_mana").value = value;
            document.getElementById("progress_mana").max = max_v;
            document.getElementById("text_mana").innerHTML = "" + value + "/" + max_v;
            break;

        case 'j_leave':
            delete autres_joueurs[parseInt(data.id_perso)];
            var d = document.getElementById("player_" + data.id_perso);
            if (d != undefined) {
                d.parentNode.removeChild(d);
            }
            var dd = document.getElementById("infos_player_" + data.id_perso);
            if (dd != undefined) {
                dd.parentNode.removeChild(dd);
            }
            aff();
            break;

        case 'j_pos':
            var id_j = parseInt(data.id_perso);
            if (autres_joueurs[id_j]) {
                autres_joueurs[id_j].x = data.x;
                autres_joueurs[id_j].y = data.y;
                aff();
            }
            break;

        case 'infos_monstres':
            load_monstres(data.infos);
            aff();
            break;

        case 'new_monstre_pos':
            // On récupere les données
            var id_monstre_spawn = data.id_spawn;
            var x = data.x;
            var y = data.y;
            // On vérifie si on a bien le monstre
            // Et on lui change sa positione
            if (ennemis[id_monstre_spawn] != undefined) {
                ennemis[id_monstre_spawn]["x"] = x;
                ennemis[id_monstre_spawn]["y"] = y;
                aff();
            }
            break;

        case 'monstre_modif_vie':
            var id_monstre_spawn = data.id_monstre_spawn;
            var vie = data.vie;
            ennemis[id_monstre_spawn]["vie"] = vie;
            aff();
            break;

        case 'monstre_modif_etat':
            var id_monstre_spawn = data.id_monstre_spawn;
            var etat = data.etat;
            ennemis[id_monstre_spawn]["etat"] = etat;
            var en_c = document.getElementById("ennemi_" + id_monstre_spawn).firstChild;
            if (etat == "mort") {
                var img_en = "../imgs/ennemis/" + ennemis_data[ennemis[id_monstre_spawn]["id_monstre"]]["img_mort"];
            } else {
                var img_en = "../imgs/ennemis/" + ennemis_data[ennemis[id_monstre_spawn]["id_monstre"]]["img"];
            }
            en_c.setAttribute("xlink:href", img_en);
            aff();
            break;

        case 'vie_joueur':
            var id_joueur = data.id_joueur;
            var value = data.value;
            var max_v = data.max_v;
            if (Object.keys(autres_joueurs).includes(id_joueur)) {
                autres_joueurs[id_joueur].vie = value;
                autres_joueurs[id_joueur].vie_max = max_v;
            }
            break;

        case 'mana_joueur':
            var id_joueur = data.id_joueur;
            var value = data.value;
            var max_v = data.max_v;
            if (Object.keys(autres_joueurs).includes(id_joueur)) {
                autres_joueurs[id_joueur].mana = value;
                autres_joueurs[id_joueur].mana_max = max_v;
            }
            break;
        
        case 'cooldown_comp':
            //TODO
            break;

        case 'reload':
            window.location.href = "jeu.php";
            break;

        default:
            // Il faut faire attention aux types d'actions que l'on gère
            // Et ne pas oublier les "break;" à la fin de chaque cas
            console.error("unsupported event", data);
    }
}