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

var actions = {};

var touches_actions = ["u", "i", "o", "p"]; // Il ne faudra jamais faire plus de 4 actions en meme temps sur le meme objet
var touches_competences = ["&", "é", "\"", "'"];
var touches_armes = ["(", "-", "è", "_"];
var touches_munitions = ["j", "k", "l", "m"];
var touche_selec_enn_plus_proche = "e";

/**
 *
 * FONCTIONS POUR AFFICHER
 *
 */

function aff() {
    tx = document.getElementById("viewport").clientWidth;
    ty = document.getElementById("viewport").clientHeight;
    //
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
        if (ap == undefined || ap.region_actu!=personnage.region_actu) {
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
            //newSvg.setAttribute("opacity", 1);
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

            if (en.etat == "mort") {
                var ime = "../imgs/ennemis/" + ennemis_data[ennemis[en.id_monstre_spawn]["id_monstre"]]["img_mort"];
            } else {
                var ime = "../imgs/ennemis/" + ennemis_data[ennemis[en.id_monstre_spawn]["id_monstre"]]["img"];
            }
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
            if (en.etat != "vivant") {
                svgInfos.style.display = "none";
            } else {
                svgInfos.style.display = "initial";
            }
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

function update_actions(){
    actions = {};
    var div_list = document.getElementById("liste_actions");
    // On nettoie
    for(c of div_list.children){
        div_list.removeChild(c);
    }
    div_list.innerHTML = "";
    // On teste s'il y a un objet selectionné 
    // selec = { "type": "objet", "x": xx, "y": yy };
    if(selec != null && selec["type"]=="objet"){
        var visible = false;
        var compteur_action = 0;
        k = ""+selec.x+"_"+selec.y;
        if(Object.keys(cases_objets_parametres).includes(k)){
            var ps = cases_objets_parametres[k];
            for(act of Object.keys(ps)){
                tact = null;
                if(act == "change_region"){
                    tact = "change region";
                }
                //
                if(tact != null && compteur_action<=3){
                    var touche_action = touches_actions[compteur_action];
                    visible = true;
                    var ndiv = document.createElement("div");
                    ndiv.classList.add("action_possible");
                    ndiv.classList.add("row");
                    var nspan = document.createElement("span");
                    nspan.innerHTML = "<span>- [<b>"+touche_action+"</b>] : "+tact;
                    ndiv.appendChild(nspan);
                    document.getElementById("liste_actions").appendChild(ndiv);
                    actions[touche_action] = {"action": act, "x": selec.x, "y": selec.y};
                    if(act=="change_region"){
                        actions[touche_action]["id_region"] = ps["change_region"];
                        actions[touche_action]["npx"] = ps["x"];
                        actions[touche_action]["npy"] = ps["y"];
                    }
                    compteur_action ++;
                }
            }
        }
        if(visible){
            document.getElementById("div_actions").style.display = "initial";
        }
        else{
            document.getElementById("div_actions").style.display = "none";
        }
    }
}

function update_competence() {
    var comp = personnage.competences;
    for (ic of Object.keys(comp)) {
        var c = comp[ic];
        if (ic < 1 || ic > 4) {
            continue;
        }

        var b = document.getElementById("bt_comp_" + ic);
        //
        for (enfant of b.children) {
            b.removeChild(enfant);
        }
        //
        if (c != null) {
            var img = document.createElement("img");
            img.setAttribute("src", "../imgs/icones_ui/" + competences[c]["img_icon"]);
            img.classList.add("img_comp");
            b.appendChild(img);
        }
    }
}

function lance_competence(num_comp) {
    var data_comp = competences[personnage.competences[num_comp]];
    // Messages d'erreur
    if (data_comp.type_cible == "ennemi" && (selectionne == null || selectionne["type"] != "ennemi")) {
        alert("Vous devez selectionner un ennemi !");
        return;
    } else if (data_comp.type_cible == "terrain" && (selectionne == null || selectionne["type"] != "terrain")) {
        alert("Vous devez selectionner un terrain !");
        return;
    } else if (data_comp.type_cible == "objet" && (selectionne == null || selectionne["type"] != "objet")) {
        alert("Vous devez selectionner un objet !");
        return;
    } else if (data_comp.type_cible == "joueur" && data_comp.nom != "premiers_secours" && (selectionne == null || selectionne["type"] != "joueur")) {
        alert("Vous devez selectionner un joueur !");
        return;
    }
    //
    if (data_comp.nom == "premiers_secours") {
        if (selectionne == null) {
            var mes = { "action": "competence", "id_competence": parseInt(data_comp.id_competence) };
            ws_send(mes);
        } else if (selectionne.type == "joueur") {
            var mes = { "action": "competence", "id_competence": parseInt(data_comp.id_competence), "joueur_cible": selectionne.id_joueur };
            ws_send(mes);
        }
    } else if (data_comp.type_cible == "ennemi") {
        var mes = { "action": "competence", "id_competence": parseInt(data_comp.id_competence), "id_monstre_spawn": selectionne.id_monstre_spawn };
        ws_send(mes);
    } else if (data_comp.type_cible == "terrain" || data_comp.type_cible == "objet") {
        var mes = { "action": "competence", "id_competence": parseInt(data_comp.id_competence), "x": selectionne.x, "y": selectionne.y };
        ws_send(mes);
    }
}

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
    const vb = v.viewBox.baseVal;
    const cam_x = vb.x;
    const cam_y = vb.y;
    //
    if (event.clientY >= v.clientHeight - 65) {
        return
    }
    //
    // La souris est sur le viewport car il englobe tout le body
    //
    const xx = Math.floor((cam_x + event.clientX) / tc);
    const yy = Math.floor((cam_y + event.clientY) / tc);
    //
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
    if (selec == null && Object.keys(cases_objets).includes(k)) {
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
    if (selec == null && Object.keys(cases_terrains).includes(k)) {
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
    update_actions();
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
        } else if (nomTouche == "Control") {
            if (selectionne != null) {
                document.getElementById("selec_ennemi").style.display = "none";
                document.getElementById("selec_objet").style.display = "none";
                document.getElementById("selec_terrain").style.display = "none";
                //
                selectionne = null;
            }
            //
        }
        /**
         * ACTIONS
         */
        for(touche of Object.keys(actions)){
            if(nomTouche == touche){
                var data = {"action": "action", "nom_action": actions[touche]["action"]};
                for(key of Object.keys(actions[touche])){
                    if(key!="action"){
                        data[key] = actions[touche][key];
                    }
                }
                ws_send(data);
            }
        }
        /**
         * COMPETENCES
         */

        /**
         * ARMES
         */

        /**
         * MUNITIONS
         */
        

        /**
         * SELECTION ENNEMI PLUS PROCHE
         */
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