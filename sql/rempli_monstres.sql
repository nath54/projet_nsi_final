INSERT INTO monstre SET
    id_monstre = 0,
    nom = "rien",
    niveau = 0,
    pv = "{\"forme\":\"value\", \"value\":0}",
    dgt = "{\"forme\":\"value\", \"value\":0}",
    loot = "[]",
    img_base = "rien.png",
    img_negatif = "rien.png",
    img_en_combat = "rien.png",
    temps_bouger = 0,
    rayon_detect = 0,
    rayon_perdu = 0,
    portee_attaque = 0,
    agressif = 0
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 1,
    nom = "rat nv.1",
    niveau = 1,
    pv = "{\"forme\":\"random between\", \"values\":[1, 5]}",
    dgt = "{\"forme\":\"random between\", \"values\":[0, 1]}",
    loot = "[]",
    img_base = "rat_base.png",
    img_negatif = "rat_base.png",
    img_en_combat = "rat_base.png",
    temps_bouger = 1.5,
    rayon_detect = 3,
    rayon_perdu = 6,
    portee_attaque = 1,
    agressif = 0
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 2,
    nom = "cobra nv.5",
    niveau = 5,
    pv = "{\"forme\":\"random between\", \"values\":[5, 10]}",
    dgt = "{\"forme\":\"random between\", \"values\":[2, 4]}",
    loot = "[]",
    img_base = "cobra_base.png",
    img_negatif = "cobra_base.png",
    img_en_combat = "cobra_base.png",
    temps_bouger = 1,
    rayon_detect = 4,
    rayon_perdu = 6,
    portee_attaque = 1,
    agressif = 0
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 3,
    nom = "araignée nv.10",
    niveau = 10,
    pv = "{\"forme\":\"random between\", \"values\":[15, 25]}",
    dgt = "{\"forme\":\"random between\", \"values\":[5, 8]}",
    loot = "[]",
    img_base = "araignee_base.png",
    img_negatif = "araignee_base.png",
    img_en_combat = "araignee_base.png",
    temps_bouger = 1.2,
    rayon_detect = 3,
    rayon_perdu = 5,
    portee_attaque = 1,
    agressif = 1
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 4,
    nom = "champignon moche nv.3",
    niveau = 3,
    pv = "{\"forme\":\"random between\", \"values\":[3, 6]}",
    dgt = "{\"forme\":\"random between\", \"values\":[1, 3]}",
    loot = "[]",
    img_base = "champignon_moche_base.png",
    img_negatif = "champignon_moche_base.png",
    img_en_combat = "champignon_moche_base.png",
    temps_bouger = 2,
    rayon_detect = 3,
    rayon_perdu = 3,
    portee_attaque = 1,
    agressif = 1
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 5,
    nom = "champignon beau nv.3",
    niveau = 3,
    pv = "{\"forme\":\"random between\", \"values\":[2, 5]}",
    dgt = "{\"forme\":\"random between\", \"values\":[1, 2]}",
    loot = "[]",
    img_base = "champignon.png",
    img_negatif = "champignon.png",
    img_en_combat = "champignon.png",
    temps_bouger = 2,
    rayon_detect = 3,
    rayon_perdu = 3,
    portee_attaque = 1,
    agressif = 0
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 6,
    nom = "blob nv.4",
    niveau = 4,
    pv = "{\"forme\":\"random between\", \"values\":[5, 8]}",
    dgt = "{\"forme\":\"random between\", \"values\":[2, 4]}",
    loot = "[]",
    img_base = "blob.png",
    img_negatif = "blob.png",
    img_en_combat = "blob.png",
    temps_bouger = 1.25,
    rayon_detect = 2,
    rayon_perdu = 8,
    portee_attaque = 2,
    agressif = 1
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 7,
    nom = "fantôme gentil nv.5",
    niveau = 5,
    pv = "{\"forme\":\"random between\", \"values\":[4, 7]}",
    dgt = "{\"forme\":\"random between\", \"values\":[3, 8]}",
    loot = "[]",
    img_base = "fantomegentil.png",
    img_negatif = "fantomegentil.png",
    img_en_combat = "fantomegentil.png",
    temps_bouger = 1.1,
    rayon_detect = 3,
    rayon_perdu = 5,
    portee_attaque = 1,
    agressif = 0
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 8,
    nom = "fantôme méchant nv.4",
    niveau = 5,
    pv = "{\"forme\":\"random between\", \"values\":[5, 8]}",
    dgt = "{\"forme\":\"random between\", \"values\":[4, 9]}",
    loot = "[]",
    img_base = "fantomemechant.png",
    img_negatif = "fantomemechant.png",
    img_en_combat = "fantomemechant.png",
    temps_bouger = 1,
    rayon_detect = 4,
    rayon_perdu = 6,
    portee_attaque = 1,
    agressif = 1
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 9,
    nom = "pie gentil nv.6",
    niveau = 6,
    pv = "{\"forme\":\"random between\", \"values\":[10, 13]}",
    dgt = "{\"forme\":\"random between\", \"values\":[9, 12]}",
    loot = "[]",
    img_base = "pie.png",
    img_negatif = "pie.png",
    img_en_combat = "pie.png",
    temps_bouger = 0.75,
    rayon_detect = 4,
    rayon_perdu = 7,
    portee_attaque = 3,
    agressif = 0
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 10,
    nom = "pie méchant nv.8",
    niveau = 8,
    pv = "{\"forme\":\"random between\", \"values\":[12, 15]}",
    dgt = "{\"forme\":\"random between\", \"values\":[11, 14]}",
    loot = "[]",
    img_base = "pie_mechant.png",
    img_negatif = "pie_mechant.png",
    img_en_combat = "pie_mechant.png",
    temps_bouger = 0.5,
    rayon_detect = 5,
    rayon_perdu = 8,
    portee_attaque = 4,
    agressif = 1
    pacifique = 0;

INSERT INTO monstre SET
    id_monstre = 11,
    nom = "plante carnivore nv.13",
    niveau = 13,
    pv = "{\"forme\":\"random between\", \"values\":[15, 17]}",
    dgt = "{\"forme\":\"random between\", \"values\":[14, 16]}",
    loot = "[]",
    img_base = "plante_carnivore.png",
    img_negatif = "plante_carnivore.png",
    img_en_combat = "plante_carnivore.png",
    temps_bouger = 1.5,
    rayon_detect = 2,
    rayon_perdu = 4,
    portee_attaque = 2,
    agressif = 1
    pacifique = 0;

    INSERT INTO monstre SET
    id_monstre = 12,
    nom = "patate nv.4",
    niveau = 4,
    pv = "{\"forme\":\"random between\", \"values\":[2, 5]}",
    dgt = "{\"forme\":\"random between\", \"values\":[1, 4]}",
    loot = "[]",
    img_base = "patate_base.png",
    img_negatif = "patate_base.png",
    img_en_combat = "patate_base.png",
    temps_bouger = 1,
    rayon_detect = 2,
    rayon_perdu = 4,
    portee_attaque = 1,
    agressif = 1
    pacifique = 0;

    INSERT INTO monstre SET
    id_monstre = 13,
    nom = "gargouille nv.15",
    niveau = 15,
    pv = "{\"forme\":\"random between\", \"values\":[10, 20]}",
    dgt = "{\"forme\":\"random between\", \"values\":[5, 15]}",
    loot = "[]",
    img_base = "gargouille_base.png",
    img_negatif = "gargouille_base.png",
    img_en_combat = "gargouille_base.png",
    temps_bouger = 4,
    rayon_detect = 8,
    rayon_perdu = 9,
    portee_attaque = 2,
    agressif = 1
    pacifique = 0;

    INSERT INTO monstre SET
    id_monstre = 14,
    nom = "troll nv.15",
    niveau = 15,
    pv = "{\"forme\":\"random between\", \"values\":[10, 20]}",
    dgt = "{\"forme\":\"random between\", \"values\":[5, 15]}",
    loot = "[]",
    img_base = "troll_base.png",
    img_negatif = "troll_base.png",
    img_en_combat = "troll_base.png",
    temps_bouger = 2,
    rayon_detect = 2,
    rayon_perdu = 3,
    portee_attaque = 1,
    agressif = 1
    pacifique = 0;

    INSERT INTO monstre SET
    id_monstre = 15,
    nom = "démon nv.20",
    niveau = 20,
    pv = "{\"forme\":\"random between\", \"values\":[15, 25]}",
    dgt = "{\"forme\":\"random between\", \"values\":[10, 20]}",
    loot = "[]",
    img_base = "demon_base.png",
    img_negatif = "demon_base.png",
    img_en_combat = "demon_base.png",
    temps_bouger = 0.5,
    rayon_detect = 10,
    rayon_perdu = 9,
    portee_attaque = 3,
    agressif = 1
    pacifique = 0;

    INSERT INTO monstre SET
    id_monstre = 16,
    nom = "mille pates nv.10",
    niveau = 10,
    pv = "{\"forme\":\"random between\", \"values\":[10, 15]}",
    dgt = "{\"forme\":\"random between\", \"values\":[5, 10]}",
    loot = "[]",
    img_base = "mille_pates_base.png",
    img_negatif = "mille_pates_base.png",
    img_en_combat = "mille_pates_base.png",
    temps_bouger = 0.5,
    rayon_detect = 3,
    rayon_perdu = 4,
    portee_attaque = 1,
    agressif = 0
    pacifique = 0;