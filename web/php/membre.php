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
</head>

<body>
Bienvenue <?php echo htmlentities(trim($_SESSION['pseudo'])); ?> !<br />
<a href="creation_perso.php">Création du personnage</a> <br /> 
<a href="accueil.php">Retour à l'accueil</a>
</body>
</html>