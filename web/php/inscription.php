<?php
include_once "../../includes/bdd.php";
$db = load_db();
// on teste si le joueur a soumis le formulaire
	if (isset($_POST['inscription']) && $_POST['inscription'] == 'Inscription') {
		// on cherche à savoir si les variables existent
		if ((isset($_POST['pseudo']) && !empty($_POST['pseudo'])) && (isset($_POST['pseudo']) && !empty($_POST['pseudo'])) && (isset($_POST['mdp_confirm']) && !empty($_POST['mdp_confirm']))){

		}
		// on teste les deux mots de passe
		if ($_POST['mdp'] != $_POST['mdp_confirm']) {
			$erreur = 'Les 2 mots de passe sont différents.';
		}
		else {  // on se connecte à un serveur SQL
			$base = mysql_connect ($port, 'pseudo', 'mdp');
			mysql_select_db ('projetclasse', $base);

			// on recherche si ce pseudo est déjà utilisé par un joueur
			$sql = 'SELECT count(*) FROM utilisateurs WHERE login="'.mysql_escape_string($_POST['pseudo']).'"'; // on cherche dans la table utilisateur si le pseudo entré existe
			$req = mysql_query($sql) or die('Erreur SQL !<br />'.$sql.'<br />'.mysql_error()); // on effectue la requête sur la bdd
			$data = mysql_fetch_array($req);

			if ($data[0] == 0) {
				$sql = 'INSERT INTO utilisateurs VALUES("", "'.mysql_escape_string($_POST['pseudo']).'", "'.mysql_escape_string(md5($_POST['mdp'])).'")'; // on insère un pseudo et un mot de passe dans la base ; on utilise md5 qui va hacher le mot de passe
				$req = mysql_query($sql) or die('Erreur SQL !'.$sql.'<br />'.mysql_error()); // 

				session_start();
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
			echo '<br />',$erreur;
			}
		?>
    </body>
</html>