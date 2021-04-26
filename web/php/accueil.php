<?php

include_once("../../includes/init.php");
include_once("../../includes/bdd.php");
$db = load_db("../../includes/config.json");

if(isset($_SESSION["error"])){
	alert($_SESSION["error"]);
	unset($_SESSION["error"]);
}

// On déconnecte quiconque vient ici
unset($_SESSION['player_id']);

// on teste si le visiteur a soumis le formulaire de connexion
// TODO: $_POST['connexion'] jamais définie (et est-ce utile ?)
if (isset($_POST['connexion']) && $_POST['connexion'] == 'Connexion') {
	if (!empty($_POST['pseudo']) && !empty($_POST['mdp'])) {

		// on teste si une entrée de la base contient ce couple pseudo / mdp
		$sql = 'SELECT id_utilisateur FROM utilisateurs WHERE pseudo=? AND mdp=MD5(?)';
		$data = requete_prep($db, $sql, array($_POST['pseudo'], $_POST['mdp']));

		$db = null;

		// si on obtient une réponse, alors l'utilisateur est un membre
		if (count($data) > 0) {
			$_SESSION['player_id'] = $data[0]["id_utilisateur"];
			header('Location: membre.php');
			exit();
		}
		// Si on ne trouve rien, mauvais pseudo / mot de passe
		elseif ($data[0][0] == 0) {
			$erreur = 'Compte non reconnu.';
		}
		// sinon, alors la, il y a un gros problème :)
		else {
			$erreur = 'Probème dans la base de données : plusieurs membres ont les mêmes identifiants de connexion.';
		}
	}
	else {
		$erreur = 'Au moins un des champs est vide.';
	}
}
?>

<html>
	<head>
		<meta charset="utf-8" />
        <title>Accueil</title>
        <link href="../css/style_co.css" rel="stylesheet" />
    </head>
    <body>
		<div id="bouton_header">
			<div class="compte_bouton">
				<a href="../php/creation_perso.php">
				<img class="login1" src="../imgs/header/login.png">
				</a>
			</div>

			<div class="parametre_bouton">
				<img class="engrenage" src="../imgs/header/engrenage.png">
			</div>
		</div>

        <form method="POST" action="post_accueil.php">

            <section class="login">
                <div class="titre">Maths Quest</div>
                <form action="accueil.php" method="post">
                    <div class="soustitre">Nom d'utilisateur: </div>
                    <input type="text" required title="Username" placeholder="Nom d'utilisateur" name="pseudo" data-icon="U" class="bouton">
					</br>
                    <div class="soustitre">Mot de passe: </div>
                    <input type="password" required title="Password" placeholder="Mot de passe" data-icon="x" name="mdp" class="bouton">
                    </br>
					</br>
					<input type="submit" class="envoyer" value="Valider" />
					<div class="oubli">
                        <div class="col"><a href="#" title="Retrouver mot de passe">Forgot Password ?</a></div>
                    </div>
					<a href="inscription.php" class="inscr">Si vous n'avez pas de compte, inscrivez vous !</a>

                </form>
            </section>
        </form>
		<?php
			// TODO: Retirer pour la version finale
			if (!empty($erreur)){
				echo($erreur);
			}
		?>
    </body>
</html>