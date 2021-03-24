<?php
//TODO: Utiliser des PDO au lieu de mysql_connect et tout, ça a été supprimé en PHP 7.0.0 et déprécié depuis PHP 5.5.0

session_start();

include_once "../../includes/bdd.php";
$db = load_db("../../includes/config.json");
// on teste si le joueur a soumis le formulaire
	if (isset($_POST['inscription']) && $_POST['inscription'] == 'Inscription') {
		// Si les variables n'existent pas, on le signale
		if (empty($_POST['pseudo']) OR empty($_POST['pseudo']) OR empty($_POST['mdp_confirm']))){
			$erreur = 'Une des variables est vide.';
		}
		// Sinon, on teste le mot de passe et la confirmation du mot de passe
		elseif ($_POST['mdp'] != $_POST['mdp_confirm']) {
			$erreur = 'Les 2 mots de passe sont différents.';
		}
		// Si tout se passe bien...
		else {  // on se connecte à un serveur SQL
			$base = mysql_connect ($port, 'pseudo', 'mdp');
			mysql_select_db ('projetclasse', $base);

			// on recherche si ce pseudo est déjà utilisé par un joueur
			$sql = 'SELECT count(*) FROM utilisateurs WHERE login="' . mysql_escape_string($_POST['pseudo']) . '"';
			$req = mysql_query($sql) or die('Erreur SQL !<br />'.$sql.'<br />'.mysql_error());
			$data = mysql_fetch_array($req);

			if ($data[0] == 0) {
				$sql = 'INSERT INTO utilisateurs VALUES("", "' . mysql_escape_string($_POST['pseudo']) . '", "' .
						mysql_escape_string(md5($_POST['mdp'])) . '")';
				$req = mysql_query($sql) or die('Erreur SQL !'.$sql.'<br />'.mysql_error());

				$_SESSION['pseudo'] = $_POST['pseudo'];
				header('Location: membre.php');
				exit();
			}
			else {
				$erreur = 'Un membre possède déjà ce pseudo.';
			}
		}
	}
?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Inscription</title>
    </head>

    <body>
        Inscription à l'espace membre :<br />
        <form action="inscription.php" method="post">

            <label for="pseudo"> Pseudo : </label> <input type="text" name="pseudo" value=" <?php if (isset($_POST['pseudo'])) echo htmlentities(trim($_POST['pseudo'])); ?> "> <br />

            <label for="mdp"> Mot de passe : </label> <input type="password" name="mdp" value=" <?php if (isset($_POST['mdp'])) echo htmlentities(trim($_POST['mdp'])); ?> "> <br />

            <label for="mdp_confirm"> Confirmation du mot de passe : </label> <input type="password" name="mdp_confirm" value=" <?php if (isset($_POST['mdp_confirm'])) echo htmlentities(trim($_POST['mdp_confirm'])); ?> "> <br /> 

            <!-- html entities convertit tous les caractères en entités HTML -->

            <input type="submit" name="inscription" value="Inscription">

        </form>

		<?php
			if (isset($erreur)) {
				echo '<br />' . $erreur;
			}
		?>
    </body>
</html>