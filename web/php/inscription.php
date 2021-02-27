<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Inscription</title>
        <link href="../css/style.css" rel="stylesheet" />
    </head>
    <body>
        <div class="container">
            <form id="form" action="../includes/inscription.php" method="POST">
                <!-- Titre -->
                <div>
                    <h1>Inscription :</h1>
                </div>
                <!-- Pseudo -->
                <div>
                    <label>Pseudo / : </label>
                    <input type="text" name="pseudo" id="pseudo" />
                </div>
                <!-- Email -->
                <div>
                    <label>Email / : </label>
                    <input type="email" name="email" id="email" />
                </div>
                <!-- Mot de Passe -->
                <div>
                    <label>Password : </label>
                    <input type="secret" name="password" id="password" />
                </div>
                <!-- Mot de Passe (Confirmation) -->
                <div>
                    <label>Password (confirm) : </label>
                    <input type="secret" name="password_confirm" id="password_confirm" />
                </div>
                <!-- Bouton -->
                <div>
                    <!-- On doit mettre un <a> car si on met un bouton,
                    le formulaire va être envoyé avant que l'on puisse le tester-->
                    <a class="bouton_form" onclick="test_form();">Ok</a>
                </div>
            </form>
        </div>
    </body>
</html>
<!-- On laisse le script ici, car c'est un petit script qui ne sera utilisé qu'ici -->
<script>

// Fonction qui va tester le formulaire de connection
// ATTENTION ! Ceci ne va pas empecher les hackers de mettre n'importe quoi !
// Il faudra aussi faire des tests dans les fichiers php !
// Ce sera surtout utile à l'utilisateur lambda qui peut se tromper
function test_form(){
    var pseudo = document.getElementById("pseudo").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var password_confirm = document.getElementById("password_confirm").value;
    //
    if(pseudo.length < 2){
        alert("Erreur ! Le pseudo est trop petit, il faut qu'il aie au minimum 2 caractères !");
        return ;
    }
    else if(pseudo.length > 16){
        alert("Erreur ! Le pseudo est trop long, il faut qu'il aie au maximum 16 caractères !");
        return ;
    }
    if(password.length < 8){
        alert("Erreur ! Le mot de passe est trop petit, il faut qu'il aie au minimum 8 caractères !");
        return ;
    }
    else if(password.length > 32){
        alert("Erreur ! Le mot de passe est trop long, il faut qu'il aie au maximum 32 caractères !");
        return ;
    }
    if(password!=password_confirm){
        alert("Erreur ! Les mots de passe sont différents !");
        return ;
    }
    // On pourra aussi renvoyer d'autres tests
    // Les tests se sont déroulés sans problèmes, on peut envoyer
    document.getElementById("form").submit();
}

</script>