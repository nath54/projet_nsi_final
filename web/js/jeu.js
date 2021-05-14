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
};

// Dict autre_joueurs :
// key : id_utilisateur
// value : dictionnaire personnage
var autres_joueurs = {};

// Dict ennemis :
// key : id_ennemi_spawn
// value : dictionnaire ennemi
var ennemis = {};
var test_var = null;

var selectionne = null;

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
    //
    var v = document.getElementById("viewport");
    v.setAttribute("viewBox", "" + (px - tx / 2) + " " + (py - ty / 2) + " " + tx + " " + ty);
    // On affiche aussi tous les autres joueurs
    for (ap of Object.values(autres_joueurs)) {
        if (ap == undefined) {
            continue;
        }
        // var ap = autres_joueurs[k];
        var apx = ap.x * tc;
        var apy = ap.y * tc;
        var p = document.getElementById("player_" + ap.id_perso);
        if (p == undefined || p == null) {
            let newSvg = document.getElementById("player").cloneNode(true)
            newSvg.id = "player_" + ap.id_perso
            newSvg.setAttribute("x", apx);
            newSvg.setAttribute("y", apy);
            //
            for (child of newSvg.childNodes) {
                if (child.getAttribute("id") == "img_perso_tete") {
                    child.setAttribute("id", "img_autre_perso_tete_" + ap.id_perso);
                }
                if (child.getAttribute("id") == "img_perso_cheveux") {
                    child.setAttribute("id", "img_autre_perso_cheveux_" + ap.id_perso);
                }
                if (child.getAttribute("id") == "img_perso_barbe") {
                    child.setAttribute("id", "img_autre_perso_barbe_" + ap.id_perso);
                }
                if (child.getAttribute("id") == "img_perso_haut") {
                    child.setAttribute("id", "img_autre_perso_haut_" + ap.id_perso);
                }
                if (child.getAttribute("id") == "img_perso_bas") {
                    child.setAttribute("id", "img_autre_perso_bas_" + ap.id_perso);
                }
                if (child.getAttribute("id") == "img_perso_pied") {
                    child.setAttribute("id", "img_autre_perso_pied_" + ap.id_perso);
                }
            }
            // on ajoute
            document.getElementById("svg_autres_joueurs").appendChild(newSvg);
            // Les infos
            var svgInfos = document.createElementNS(svgns, "svg");
            svgInfos.setAttribute("id", "infos_player_" + ap.id_perso);
            svgInfos.setAttribute("x", apx);
            svgInfos.setAttribute("y", apy - 20);
            // Les images
            console.log(images_corps);
            document.getElementById("img_autre_perso_tete_" + ap.id_perso).setAttribute("xlink:href", "../imgs/custom_perso/" + images_corps["tete"][ap.id_tete - 1]);
            document.getElementById("img_autre_perso_cheveux_" + ap.id_perso).setAttribute("xlink:href", "../imgs/custom_perso/" + images_corps["cheveux"][ap.id_cheveux - 1]);
            document.getElementById("img_autre_perso_barbe_" + ap.id_perso).setAttribute("xlink:href", "../imgs/custom_perso/" + images_corps["barbe"][ap.id_barbe - 1]);
            document.getElementById("img_autre_perso_haut_" + ap.id_perso).setAttribute("xlink:href", "../imgs/custom_perso/" + images_corps["haut"][ap.id_haut - 1]);
            document.getElementById("img_autre_perso_bas_" + ap.id_perso).setAttribute("xlink:href", "../imgs/custom_perso/" + images_corps["bas"][ap.id_bas - 1]);
            document.getElementById("img_autre_perso_pied_" + ap.id_perso).setAttribute("xlink:href", "../imgs/custom_perso/" + images_corps["pied"][ap.id_pied - 1]);
            // pseudo
            let text = document.createElementNS(svgns, "text");
            text.innerHTML = ap.nom;
            text.setAttribute("x", 10)
            text.setAttribute("y", 15)
            svgInfos.appendChild(text);
            // pv
            let pv = document.createElementNS(svgns, "rect");
            pv.setAttribute("id", "pv_player_" + ap.id_perso);
            pv.setAttribute("x", 0);
            pv.setAttribute("y", 20);
            pv.setAttribute("width", ap.vie / ap.vie_max * tc);
            pv.setAttribute("height", 5);
            pv.setAttribute("fill", "red");
            pv.style.zIndex = 10;
            svgInfos.appendChild(pv);
            // pm
            let pm = document.createElementNS(svgns, "rect");
            pm.setAttribute("id", "pm_player_" + ap.id_perso);
            pm.setAttribute("x", 0);
            pm.setAttribute("y", 23);
            pm.setAttribute("width", ap.mana / ap.mana_max * tc);
            pm.setAttribute("height", 3);
            pm.setAttribute("fill", "blue");
            pm.style.zIndex = 10
            svgInfos.appendChild(pm);
            // on ajoute
            document.getElementById("svg_infos_autres_joueurs").appendChild(svgInfos);
        } else {
            p.setAttribute("x", apx);
            p.setAttribute("y", apy);
            document.getElementById("pv_player_" + ap.id_perso).setAttribute("width", ap.vie / ap.vie_max * tc)
            document.getElementById("pm_player_" + ap.id_perso).setAttribute("width", ap.mana / ap.mana_max * tc)
            var svgInfos = document.getElementById("infos_player_" + ap.id_perso);
            svgInfos.setAttribute("x", apx);
            svgInfos.setAttribute("y", apy - 20);
        }
    }
    // On va afficher les ennemis
    // On affiche aussi tous les autres joueurs
    for (en of Object.values(ennemis)) {
        // var ap = autres_joueurs[k];
        var enx = en.x * tc;
        var eny = en.y * tc;
        var ennemi = document.getElementById("ennemi_" + en.id_monstre_spawn);
        if (ennemi == undefined || ennemi == null) {
            let newSvg = document.getElementById("monstre_template").cloneNode(true);
            newSvg.setAttribute("id", "ennemi_" + en.id_monstre_spawn);
            newSvg.setAttribute("x", enx);
            newSvg.setAttribute("y", eny);
            newSvg.setAttribute("style", "display:initial;");
            //
            var ime = "../imgs/ennemis/" + ennemis_data[en.id_monstre]["img"];
            newSvg.firstChild.setAttribute("xlink:href", ime);
            // on ajoute
            document.getElementById("svg_ennemis").appendChild(newSvg);
            // Les infos
            var svgInfos = document.createElementNS(svgns, "svg");
            svgInfos.setAttribute("id", "infos_ennemi_" + en.id_monstre_spawn);
            svgInfos.setAttribute("x", enx);
            svgInfos.setAttribute("y", eny - 15);
            // nom
            let text = document.createElementNS(svgns, "text");
            text.innerHTML = en.vie;
            text.setAttribute("id", "pv_ennemi_" + en.id_monstre_spawn);
            text.setAttribute("x", 20);
            text.setAttribute("y", 30);
            svgInfos.appendChild(text);
            // Nom
            let text2 = document.createElementNS(svgns, "text");
            text2.innerHTML = en.nom;
            text2.setAttribute("x", 10);
            text2.setAttribute("y", 15);
            svgInfos.appendChild(text2);
            // on ajoute
            document.getElementById("svg_infos_ennemis").appendChild(svgInfos);
        } else {
            //
            //
            ennemi.setAttribute("x", enx);
            ennemi.setAttribute("y", eny);
            //
            if (selectionne != null && selectionne.type == "ennemi" && selectionne.id_monstre_spawn == en.id_monstre_spawn) {
                var sel = document.getElementById("selec_ennemi");
                sel.setAttribute("x", en.x * tc);
                sel.setAttribute("y", en.y * tc);
            }
            //
            document.getElementById("pv_ennemi_" + en.id_monstre_spawn).innerHTML = en.vie;
            var svgInfos = document.getElementById("infos_ennemi_" + en.id_monstre_spawn);
            svgInfos.setAttribute("x", enx);
            svgInfos.setAttribute("y", eny - 15);
        }
    }
    // On va update les infos affichés à l'écran :
    var pv = document.getElementById("progress_vie");
    pv.value = personnage.vie;
    pv.max = personnage.vie_max;
    var tv = document.getElementById("text_vie");
    tv.innerHTML = "" + personnage.vie + "/" + personnage.vie_max;
    //
    var pm = document.getElementById("progress_mana");
    pm.value = personnage.mana;
    pm.max = personnage.mana_max;
    var tm = document.getElementById("text_mana");
    tm.innerHTML = "" + personnage.mana + "/" + personnage.mana_max;
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


//en_chargement

function load_monstres(data) {
    for (key of Object.keys(data)) {
        ennemis[key] = data[key];
    }
}

/**
 *
 * BOUTONS POUR CHANGER LA DIV CHAT/BAG/...
 *
 */

function change_div(id_div) {
    for (i of["div_chat", "div_bag"]) {
        var aff = "none";
        if (id_div == i) {
            aff = "initial";
        }
        document.getElementById(i).style.display = aff;
    }
}

/**
 *
 * MOUSE INPUTS
 *
 */

document.body.addEventListener('mousedown', event => {
    // On récupère les coordonnées du click
    var v = document.getElementById("viewport");
    var c_x = v.clientWidth;
    var c_y = v.clientHeight;
    var xx = parseInt((tx / c_x) * event.clientX / tc) + personnage.x - parseInt(tx / 2 / tc);
    var yy = parseInt((ty / c_y) * event.clientY / tc) + personnage.y - parseInt(ty / 2 / tc);
    // alert("(" + xx + ", " + yy + ")");
    // ON VA ENLEVER L'ANCIEN SELECTIONNé
    if (selectionne != null) {
        document.getElementById("selec_ennemi").style.display = "none";
        document.getElementById("selec_objet").style.display = "none";
        document.getElementById("selec_terrain").style.display = "none";
    }
    //
    selec = null;
    // On va regarder s'il y a un ennemi sur la case
    for (en of Object.values(ennemis)) {
        if (en.x == xx && en.y == yy) {
            selec = { "type": "ennemi", "id_monstre_spawn": en.id_monstre_spawn };
            var sel = document.getElementById("selec_ennemi");
            sel.setAttribute("x", xx * tc);
            sel.setAttribute("y", yy * tc);
            sel.setAttribute("width", tc);
            sel.setAttribute("height", tc);
            sel.style.display = "initial";
        }
    }
    //
    var k = "" + xx + "_" + yy;
    // On va regarder s'il y a un objet sur la case
    if (Object.keys(cases_objets).includes(k)) {
        //
        selec = { "type": "objet", "x": xx, "y": yy };
        //
        var sel = document.getElementById("selec_objet");
        sel.setAttribute("x", xx * tc);
        sel.setAttribute("y", yy * tc);
        sel.setAttribute("width", tc);
        sel.setAttribute("height", tc);
        sel.style.display = "initial";
    }
    // On va regarder s'il y a un terrain sur la case
    if (Object.keys(cases_terrains).includes(k)) {
        selec = { "type": "terrain", "x": xx, "y": yy };
        var sel = document.getElementById("selec_terrain");
        sel.setAttribute("x", xx * tc);
        sel.setAttribute("y", yy * tc);
        sel.setAttribute("width", tc);
        sel.setAttribute("height", tc);
        sel.style.display = "initial";
    }
    //
    selectionne = selec;
});

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
        } else if (nomTouche === 'Escape') {
            if (document.getElementById("menu_princ").style.display == "none") {
                set_menu("menu_princ")
            } else {
                set_menu("")
            }
        } else if (nomTouche == "Alt") {
            if (selectionne != null) {
                document.getElementById("selec_ennemi").style.display = "none";
                document.getElementById("selec_objet").style.display = "none";
                document.getElementById("selec_terrain").style.display = "none";
                //
                selectionne = null;
            }
            //
        }
    }
}, false);

document.addEventListener('keyup', (event) => {
    const nomTouche = event.key;
}, false);

function set_menu(nom_menu) {
    for (im of["menu_princ", "menu_inv", "menu_stats"]) {
        var m = document.getElementById(im);
        if (im == nom_menu) {
            m.style.display = "initial";
        } else {
            m.style.display = "none";
        }
    }
}