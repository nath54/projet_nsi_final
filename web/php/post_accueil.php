<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Bienvenue sur Maths Quest !</title>
    </head>
    <body>
    
        <?php
    if (isset($_POST['mdp']) AND $_POST['mdp'] == 'mdp')
    // On laisse le joueur se connecter au jeu, si son mot de passe est bon
    {
        header('Location jeu.php');
    }
    else // Sinon on ne laisse pas le joueur se connecter
    {
        header('Location: accueil.php');
        echo '<p> Mot de passe incorrect </p>';
    }
    ?>
    
        
    </body>
</html>