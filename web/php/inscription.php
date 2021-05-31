<?php

include_once("../../includes/init.php");
include_once("../../includes/bdd.php");
$db = load_db("../../includes/config.json");

// on teste si le joueur a soumis le formulaire
// Si les variables n'existent pas, on le signale
if (empty($_POST['pseudo']) OR empty($_POST['mdp']) OR empty($_POST['mdp_confirm']) OR empty($_POST['sexe']) OR empty($_POST['classe']))
{
	$erreur = 'Une des variables est vide.';
}

// On vérifie que le sexe et la classe du joueur correspondent aux valeurs prédéfinies
elseif( ! in_array($_POST['sexe'], ['Homme','Femme','Autre'])){
	$erreur = 'Ce sexe n\'est pas valide.';
}
elseif( ! in_array($_POST['classe'], ['chevalier','chasseur','sorcier'])){
	$erreur = 'Ce sexe n\'est pas valide.';
}

// Sinon, on teste le mot de passe et la confirmation du mot de passe
elseif($_POST['mdp'] != $_POST['mdp_confirm']){
	$erreur = "Les 2 mots de passe sont différents.";
}

// Si tout se passe bien...
else {
	// on recherche si ce pseudo est déjà utilisé par un joueur

	$sql = 'SELECT count(*) FROM utilisateurs WHERE pseudo=?';
	$data = requete_prep($db, $sql, array($_POST["pseudo"]));

	// On ajoute l'utilisateur à la base de données
	if ($data[0][0] == 0)
	{
		$sql = 'INSERT INTO utilisateurs (pseudo,mdp,sexe,classe,competence) VALUES(:pseudo, MD5(:mdp), :sexe, :classe, :comp)';
		$status = action_prep($db, $sql, $vars = array(":pseudo" => $_POST["pseudo"], ":mdp" => $_POST["mdp"], ":sexe" => $_POST["sexe"], ":classe" => $_POST["classe"], ":comp" => "{\"1\":1, \"2\":2, \"3\":3, \"4\":null}"),$debug);
		$_SESSION["player_id"] = $db->lastInsertId();

		// On l'envoie ensuite vers l'espace membre si l'inscription se déroule comme il faut
		// Il pourra choisir d'aller vers création perso ou de revenir à l'accueil
		if ($status){
			$_SESSION['pseudo'] = $_POST['pseudo'];
			header('Location: membre.php');
			exit();
		
		}
		else 
		{
			$erreur = 'Problème lors de l\'insertion dans la base de données';
		}

	}
		else
		{
			$db = null;
			$erreur = "Un membre possède déjà ce pseudo.";
		}
}

?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Inscription</title>
		<link href="../css/style_inscription.css" rel="stylesheet" />
    </head>

    <body>
		<section class="inscr">
			<div class="titre">Inscription à l'espace membre :</div><br />
			<section class="erreur">
			<?php echo $erreur ?>
			</section>
			<form action="inscription.php" method="post">

			<div class="bouton">
				<label for="pseudo"> Pseudo :</label> <input type="text" name="pseudo" value="<?php if (isset($_POST['pseudo'])) echo htmlentities(trim($_POST['pseudo'])); ?>"> </br>
				</br>
				<label for="mdp"> Mot de passe :</label> <input type="password" name="mdp" value="<?php if (isset($_POST['mdp'])) echo htmlentities(trim($_POST['mdp'])); ?>"> </br>
				</br>
				<label for="mdp_confirm"> Confirmation du mot de passe: </label> <input type="password" name="mdp_confirm" value=" <?php if (isset($_POST['mdp_confirm'])) echo htmlentities(trim($_POST['mdp_confirm'])); ?> "> </br>
				</br>
			</div>
				<!-- html entities convertit tous les caractères en entités HTML -->
			<div class="select">
				Sexe :
					<select name="sexe" size="1">
						<option>Homme</option>
						<option>Femme</option>
						<option>Autre</option>
					</select>
				</br></br>
				Classe :
					<select name="classe" size="1">
						<option>chevalier</option>
						<option>chasseur</option>
						<option>sorcier</option>
					</select>
				</br>
			</div>
			</br></br></br></br><input type="submit" class="sub" name="inscription" value="Inscription">

			</form>
		</section>

		<?php
			// TODO: Retirer pour la version finale
			if ($debug)
			{
				if (isset($erreur)) 
				{
					echo '<br />' . $erreur;
				}
			}
		?>
    </body>
</html>