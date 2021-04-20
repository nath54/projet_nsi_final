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
    var player = document.getElementById("player");
    var px = personnage.x * player.getAttribute("width");
    var py = personnage.y * player.getAttribute("height");
    player.setAttribute("x", px);
    player.setAttribute("y", py);
    // On affiche aussi tous les autres joueurs
    for (ap of Object.values(autres_joueurs)) {
        // var ap = autres_joueurs[k];
        var apx = ap.x * tc;
        var apy = ap.y * tc;
        var p = document.getElementById("player_" + ap.id_perso);
        console.log(ap.id_perso, " x : ", apx, " y : ", apy);
        if (p == undefined || p == null) {
            let newSvg = document.getElementById("player").cloneNode(true)
            newSvg.id = "player_" + ap.id_perso
            newSvg.setAttribute("x", apx)
            newSvg.setAttribute("y", apy - 20)
            newSvg.setAttribute("height", tc + 20)
            newSvg.firstChild.setAttribute("y", 20);
            // pseudo
            let text = document.createElementNS(svgns, "text");
            text.innerHTML = ap.nom;
            text.setAttribute("x", "20")
            text.setAttribute("y", "10")
            newSvg.appendChild(text);
            // pv
            let pv = document.createElementNS(svgns, "rect");
            pv.setAttribute("id", "pv_player_" + ap.id_perso);
            pv.setAttribute("x", 0);
            pv.setAttribute("y", 15);
            pv.setAttribute("width", ap.vie / ap.vie_max * tc);
            pv.setAttribute("height", 5);
            pv.setAttribute("fill", "red");
            newSvg.appendChild(pv);
            // pm
            let pm = document.createElementNS(svgns, "rect");
            pm.setAttribute("id", "pm_player_" + ap.id_perso);
            pm.setAttribute("x", 0);
            pm.setAttribute("y", 20);
            pm.setAttribute("width", ap.mana / ap.mana_max * tc);
            pm.setAttribute("height", 5);
            pm.setAttribute("fill", "blue");
            newSvg.appendChild(pm);
            // on ajoute
            document.getElementById("svg_autres_joueurs").appendChild(newSvg);
        } else {
            p.setAttribute("x", apx);
            p.setAttribute("y", apy - 20);
            document.getElementById("pv_player_" + ap.id_perso).setAttribute("width", ap.vie / ap.vie_max * tc)
            document.getElementById("pm_player_" + ap.id_perso).setAttribute("width", ap.mana / ap.mana_max * tc)
        }
    }
    //
    var v = document.getElementById("viewport");
    v.setAttribute("viewBox", "" + (px - tx / 2) + " " + (py - ty / 2) + " " + tx + " " + ty);
    // On va update les infos affichés à l'écran :
    var pv = document.getElementById("progress_vie")
    pv.value = personnage.vie
    pv.max = personnage.vie_max;
    var tv = document.getElementById("text_vie")
    tv.innerHTML = "" + personnage.vie + "/" + personnage.vie_max
        //
    var pm = document.getElementById("progress_mana")
    pm.value = personnage.mana
    pm.max = personnage.mana_max
    var tm = document.getElementById("text_mana")
    tm.innerHTML = "" + personnage.mana + "/" + personnage.mana_max
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