<?php
// on teste si le visiteur a soumis le formulaire de connexion
// TODO: $_POST['connexion'] jamais définie (et est-ce utile ?)
if (isset($_POST['connexion']) && $_POST['connexion'] == 'Connexion') {
	if (!empty($_POST['login']) && !empty($_POST['pass'])) {
		include_once("../../includes/bdd.php");
		$db = load_db("../../includes/config.json");

		// on teste si une entrée de la base contient ce couple login / pass
		$sql = 'SELECT count(*) FROM utilisateurs WHERE pseudo=? AND mdp=MD5(?)';
		$data = requete_prep($db, $sql, array($_POST['login'], $_POST['pass']));

		$db = null;

		// si on obtient une réponse, alors l'utilisateur est un membre
		if ($data[0] == 1) {
			session_start();
			$_SESSION['login'] = $_POST['login'];
			header('Location: membre.php');
			exit();
		}
		// Si on ne trouve rien, mauvais login / mot de passe
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
        <form method="POST" action="">

            <section class="login">
                <div class="titre">Maths Quest</div>
                <form action="accueil.php" method="post">
                    <div class="soustitre">Nom d'utilisateur: </div>
                    <input type="text" required title="Username" placeholder="Nom d'utilisateur" name="login" data-icon="U" class="bouton">
					</br>
                    <div class="soustitre">Mot de passe: </div>
                    <input type="password" required title="Password" placeholder="Mot de passe" data-icon="x" name="pass" class="bouton">
                    </br>
					</br>
                    <a href="post_accueil.php" class="envoyer">Valider</a>
					
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