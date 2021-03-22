<?php
// on teste si le visiteur a soumis le formulaire de connexion
if (isset($_POST['connexion']) && $_POST['connexion'] == 'Connexion') {
	if ((isset($_POST['login']) && !empty($_POST['login'])) && (isset($_POST['pass']) && !empty($_POST['pass']))) {

	$base = mysql_connect ('serveur', 'login', 'password');
	mysql_select_db ('nom_base', $base);

	// on teste si une entrée de la base contient ce couple login / pass
	$sql = 'SELECT count(*) FROM membre WHERE login="'.mysql_escape_string($_POST['login']).'" AND pass_md5="'.mysql_escape_string(md5($_POST['pass'])).'"';
	$req = mysql_query($sql) or die('Erreur SQL !<br />'.$sql.'<br />'.mysql_error());
	$data = mysql_fetch_array($req);

	mysql_free_result($req);
	mysql_close();

	// si on obtient une réponse, alors l'utilisateur est un membre
	if ($data[0] == 1) {
		session_start();
		$_SESSION['login'] = $_POST['login'];
		header('Location: membre.php');
		exit();
	}
	// si on ne trouve aucune réponse, le visiteur s'est trompé soit dans son login, soit dans son mot de passe
	elseif ($data[0] == 0) {
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
        <meta charset="utf-8">
        <title> Accueil </title>
        <link href="style_co.css" rel = "stylesheet"> 
    </head>
    <body>
        <form method="POST" action = ""> 

            <section class="login">
                <div class="titre">Maths Quest</div>
                <form action="#" method="post">
                    <div class="bouton">Nom d'utilisateur</div>
                    <input type="text" required title="Username" placeholder="Username" data-icon="U"> </br>
                    </br>
                    <div class="bouton">Mot de passe</div>
                    <input type="password" required title="Password" placeholder="Password" data-icon="x">
                    <div class="oubli">
                        <div class="col"><a href="#" title="Retrouver mot de passe">Forgot Password ?</a></div>
                    </div>
                    <a href="#" class="envoyer">Submit</a>
                </form>
            </section>
        </form>

    </body>
</html>