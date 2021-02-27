
<?php

include_once "../includes/init.php";

if(!(isset($_SESSION["token"]) && isset($_SESSION["code_token"]) && isset($_POST[$_SESSION["code_token"]]) && $_SESSION["token"]==$_POST[$_SESSION["code_token"]])){
    disconnect(true);
}

$db = load_db();
$token = "";

if(isset($POST["pseudo"]) && isset($POST["email"]) && isset($POST["password"]) && isset($POST["password_confirm"]) ){
    $pseudo = $_POST["pseudo"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    $password_confirm = $_POST["password_confirm"];
    //
    //TODO : tests à faire
    // test de la taille du pseudo
    // test de la taille du password
    // test si les mots de passes sont différents
    // test du pseudo s'il existe déjà
    // test de l'email s'il existe déjà
    // Si Problème : 
    //   disconnect();
    //   $_SESSION["erreur_inscription"] = "Nom de l'erreur";
    //   header("Location: ../web/inscription.php");
    // Sinon :
    $action = "INSERT INTO comptes SET pseudo=:pseudo, email=:email, password_=MD5(:password_)";
    $vars = array(":pseudo"=>$pseudo,
                  ":email"=>$email,
                  ":password_"=>$password);
    if(action_prep($db, $actop, $vars)){
        $id_compte = $db->lastInsertId();
        $_SESSION["id_compte"] = $id_compte;
        $token = gen_key();
        $_SESSION["token"] = $token;
    }
    else{
        disconnect();
        $_SESSION["erreur_inscription"] = "Il y a eu une erreur, veuillez réessayer plus tard";
        header("Location: ../web/inscription.php");
    }

}
else if(!isset($_POST["pseudo"]) && isset($POST["email"]) && isset($_SESSION["id_compte"])){
    $email = $_POST["email"];
    $id_compte = $_SESSION["id_compte"];
    // On pourra éventuellement tester si le compte existe bien
    $action = "UPDATE comptes SET email=:email WHERE id=:id_compte";
    $vars = array(":email"=>$email,
                  ":id_compte"=>$id_compte);
    if(action_prep($db, $actop, $vars)){
        $token = gen_key();
        $_SESSION["token"] = $token;
    }
    else{
        disconnect();
        $_SESSION["erreur_inscription"] = "il y a eu une erreur, veuillez réessayer plus tard.";
        header("Location: ../web/inscription.php");
    }
}
else{
    disconnect();
    $_SESSION["erreur_inscription"] = "Il y a eu une erreur, veuillez réessayer plus tard.";
    header("../web/inscription.php");
}

$email = $_POST["email"];
$code = gen_key(6);
$_SESSION["code_email"] = $code;

// Il faudra trouver comment envoyer un mail depuis php
$to      = $email;
$subject = "Code de vérification d'email";
$message = 'Votre code de vérification est : '.$code;
mail($to, $subject, $message);


?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Vérification de l'addresse mail</title>
        <link href="../css/style.css" rel="stylesheet" />
    </head>
    <body>
        <div class="container">
            <form id="form" action="../includes/inscription.php" method="POST" token="<?php echo gen_key(); ?>">
                <?php
                for($x=0; $x<random_int(5,20); $x++){
                    echo '<input type="text" value="'.gen_key().'" name="'.gen_key().'" style="display:none" />';
                }
                ?>
                <!-- Titre -->
                <div>
                    <h1>Code de vérification de l'addresse mail :</h1>
                </div>
                <!-- Pseudo -->
                <div>
                    <label>Code : </label>
                    <input type="text" name="code" />
                </div>
                <!-- Bouton -->
                <div>
                    <!-- On doit mettre un <a> car si on met un bouton,
                    le formulaire va être envoyé avant que l'on puisse le tester-->
                    <a class="bouton_form" onclick="test_form();">Ok</a>
                </div>
                <?php
                for($x=0; $x<random_int(2,10); $x++){
                    echo '<input type="text" val!ue="'.gen_key().'" name="'.gen_key().'" style="display:none" />';
                }
                ?>
                <input type="text" value="<?php echo $token ?>" name="<?php $_SESSION["code_token"] ?>" style="display:none" />
                <?php
                for($x=0; $x<random_int(2,10); $x++){
                    echo '<input type="text" value="'.gen_key().'" name="'.gen_key().'" style="display:none" />';
                }
                ?>
            </form>
            
            <!-- Changer d'email -->
            <form id="form" action="../includes/pre_inscription.php" method="POST" token="<?php echo gen_key(); ?>">
                <?php
                for($x=0; $x<random_int(5,20); $x++){
                    echo '<input type="text" value="'.gen_key().'" name="'.gen_key().'" style="display:none" />';
                }
                ?>
                <!-- Titre -->
                <div>
                    <h1>Changement d'addresse mail :</h1>
                </div>
                <!-- Email -->
                <div>
                    <label>Email : </label>
                    <input type="email" name="email" />
                </div>
                <!-- Bouton -->
                <div>
                    <!-- On doit mettre un <a> car si on met un bouton,
                    le formulaire va être envoyé avant que l'on puisse le tester-->
                    <input type="submit" value="Change email" />
                </div>
                <?php
                for($x=0; $x<random_int(2,10); $x++){
                    echo '<input type="text" val!ue="'.gen_key().'" name="'.gen_key().'" style="display:none" />';
                }
                ?>
                <input type="text" value="<?php echo $token ?>" name="<?php $_SESSION["code_token"] ?>" style="display:none" />
                <?php
                for($x=0; $x<random_int(2,10); $x++){
                    echo '<input type="text" value="'.gen_key().'" name="'.gen_key().'" style="display:none" />';
                }
                ?>
            </form>
        </div>
    </body>
</html>