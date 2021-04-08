/**
 *
 * PERSOS, MAPS, AUTRES INFOS
 *
 */

var svgns = "http://www.w3.org/2000/svg"

var tx = 100; // Ca sera changé (taille horizontale de la viewBox)
var ty = 100; // Ca sera changé (taille verticale de la viewBox)
var tc = 100; // Ca sera changé (taille d'une case)
var personnage = {
    "id_perso": 0,
    "nom": 0,
    "x": 0,
    "y": 0,
    "vie": 100,
    "vie_max": 100,
    "mana": 100,
    "mana_max": 100,
    "xp": 100,
    "xp_tot": 100,
    "region_actu": 1
}

// Dict autre_joueurs :
// key : id_utilisateur
// value : dictionnaire personnage
var autres_joueurs = {}

/**
 *
 * FONCTIONS POUR AFFICHER
 *
 */

function aff() {
    var p = document.getElementById("player");
    var px = personnage.x * p.getAttribute("width");
    var py = personnage.y * p.getAttribute("height");
    p.setAttribute("x", px);
    p.setAttribute("y", py);
    // On affiche aussi tous les autres joueurs
    for (k of Object.keys(autres_joueurs)) {
        var ap = autres_joueurs[k];
        var p = document.getElementById("player_" + ap.id_perso);
        if (!p) {

            var p = document.createElementNS(svgns, "svg");
            p.setAttributeNS(svgns, "x", ap.x);
            p.setAttributeNS(svgns, "y", ap.y);
            p.setAttributeNS(svgns, "width", tc);
            p.setAttributeNS(svgns, "height", tc);
            p.setAttribute("id", "player_" + ap.id_perso);

            var i = document.createElementNS(svgns, "image");
            i.setAttributeNS(svgns, "width", tc);
            i.setAttributeNS(svgns, "height", tc);
            i.setAttributeNS(svgns, "xlink:href", "../imgs/sprites/sprite_fixe_droit.png");
            p.appendChild(i);

            document.getElementById("svg_autres_joueurs").appendChild(p);
        }

        var apx = ap.x * p.getAttribute("width");
        var apy = ap.y * p.getAttribute("height");
        p.setAttribute("x", apx);
        p.setAttribute("y", apy);
    }
    //
    var v = document.getElementById("viewport");
    // avb = v.getAttribute("viewBox");
    // var b = avb.split(" ");
    // avtx = int(b[2]);
    // avty = int(b[3]);
    v.setAttribute("viewBox", "" + (px - tx / 2) + " " + (py - ty / 2) + " " + tx + " " + ty);
}

/**
 *
 * FONCTIONS POUR AFFICHER/METTRE A JOUR LES INFOS SUR LA PAGE
 *
 */


// function update_life(vie, vie_tot) {
//     document.getElementById("vie_value").innerHTML = "" + vie + "/" + vie_tot;
//     document.getElementById("progress_vie").value = vie / vie_tot * 100.0;
// }

// function update_mana(mana, mana_tot) {
//     document.getElementById("mana_value").innerHTML = "" + mana + "/" + mana_tot;
//     document.getElementById("progress_mana").value = mana / mana_tot * 100.0;
// }

// function update_xp(xp, xp_tot) {
//     document.getElementById("exp_value").innerHTML = "" + xp + "/" + xp_tot;
//     document.getElementById("progress_exp").value = xp / xp_tot * 100.0;
// }

// function update_niveau(niv) {
//     document.getElementById("niveau_profil").value = niv;
// }

// function update_region_name(name) {
//     document.getElementById("region_name").value = name;
// }

// function update_region_count(num) {
//     document.getElementById("region_player_number").value = num;
// }


/**
 *
 * BOUTONS POUR CHANGER LA DIV CHAT/BAG/...
 *
 */

function change_div(id_div) {
    for (i of["div_chat", "div_bag"]) {
        aff = "none";
        if (id_div == i) {
            aff = "initial";
        }
        document.getElementById(i).style.display = aff;
    }
}

/**
 *
 * KEY INPUTS
 *
 */


document.addEventListener('keydown', (event) => {
    if (!en_chargement) {
        const nomTouche = event.key;
        if (nomTouche === 'ArrowUp') {
            ws_send({ "action": "deplacement", "deplacement": [0, -1] });
        } else if (nomTouche === 'ArrowDown') {
            ws_send({ "action": "deplacement", "deplacement": [0, 1] });
        } else if (nomTouche === 'ArrowLeft') {
            ws_send({ "action": "deplacement", "deplacement": [-1, 0] });
        } else if (nomTouche === 'ArrowRight') {
            ws_send({ "action": "deplacement", "deplacement": [1, 0] });
        }
    }
}, false);

document.addEventListener('keyup', (event) => {
    const nomTouche = event.key;
}, false);