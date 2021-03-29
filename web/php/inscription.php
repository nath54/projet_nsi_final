<?php
session_start();
$debug=true; // changer quand on mettra en ligne

// on teste si le joueur a soumis le formulaire
// TODO: $_POST['inscription'] jamais définie (et est-ce utile ?)
if (isset($_POST['inscription']) && $_POST['inscription'] == 'Inscription') {
	// Si les variables n'existent pas, on le signale
	if (empty($_POST['pseudo']) OR empty($_POST['mdp']) OR empty($_POST['mdp_confirm']) OR empty($_POST['sexe']) OR empty($_POST['classe']))
	{
		$erreur = 'Une des variables est vide.';
	}
	// Sinon, on teste le mot de passe et la confirmation du mot de passe
	elseif ($_POST['mdp'] != $_POST['mdp_confirm']) {
		$erreur = 'Les 2 mots de passe sont différents.';
	}
	// Si tout se passe bien...
	else {
		// on recherche si ce pseudo est déjà utilisé par un joueur

		include_once("../../includes/bdd.php");
		$db = load_db("../../includes/config.json");
		$sql = 'SELECT count(*) FROM utilisateurs WHERE pseudo=?';
		$data = requete_prep($db, $sql, array($_POST["pseudo"]));
		print_r($data);
		if ($data[0][0] == 0) {
			$sql = 'INSERT INTO utilisateurs (pseudo,mdp,sexe,classe) VALUES(?, MD5(?), ?, ?)';
			$status = action_prep($db, $sql, array($_POST["pseudo"], $_POST["mdp"], $_POST["sexe"], $_POST["classe"]),$debug);

			$db = null;

			if ($status){
				$_SESSION['pseudo'] = $_POST['pseudo'];
				header('Location: membre.php');
				exit();
			} else {
				$erreur = 'Problème lors de l\'insertion dans la base de données';
			}
		}
		else {
			$db = null;
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
			
			<form>
			Sexe :
				<select name="nom" size="1">
					<OPTION>Homme
					<OPTION>Femme
					<OPTION>Autre
				</select>
			</form>

			<form>
			Classe :
				<select name="nom" size="1">
					<OPTION>Chevalier
					<OPTION>Chasseur
					<OPTION>Sorcier
				</select>
			</form>

            <input type="submit" name="inscription" value="Inscription">

        </form>

		<?php
			// TODO: Retirer pour la version finale
			if (isset($erreur)) {
				echo '<br />' . $erreur;
			}
		?>
    </body>
</html>