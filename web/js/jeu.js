/**
 *
 * PERSOS, MAPS, AUTRES INFOS
 *
 */

var tx = 100; // Ca sera changé
var ty = 100; // Ca sera changé
var personnage = {
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

/**
 *
 * FONCTIONS POUR AFFICHER
 *
 */

function aff() {
    var p = document.getElementById("perso");
    p.setAttribute("x", personnage.x);
    p.setAttribute("y", personnage.y);
    var v = document.getElementById("viewport");
    v.setAttribute("x", )
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