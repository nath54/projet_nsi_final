<?php
session_start();
if (!isset($_SESSION['pseudo'])) {
	header ('Location: accueil.php');
	exit();
}
?>

<html>
<head>
<title>Espace membre</title>
<link href="../css/style_inscription.css" rel="stylesheet" />
</head>

<body>
	<section class="mem">
		<div class="titre">Bienvenue <?php echo htmlentities(trim($_SESSION['pseudo'])); ?> !</div><br /><br/><br/>  
			<a href="creation_perso.php" class="bouton">Création du personnage</a> 
				<br/> <br/> <br/> <br/> <br/> <br/>	<br/> <br/>
			<a href="accueil.php" class="bouton2">Retour à l'accueil</a>
		</div>
</body>
</html>