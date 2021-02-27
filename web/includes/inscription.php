<?php

include_once "../includes/init.php";

if(!(isset($_SESSION["token"]) && isset($_SESSION["code_token"]) && isset($_POST[$_SESSION["code_token"]]) && $_SESSION["token"]==$_POST[$_SESSION["code_token"]])){
    disconnect(true);
}

$db = load_db();
$token = "";

if(isset($_POST["code"]) && isset($_SESSION["code_email"]) && isset($_SESSION["id_compte"])){
    $action = "UPDATE comptes SET valid=1 WHERE id=:id_compte";
    $vars = array(":id_compte"=>$_SESSION["id_compte"]);
    if(action_prep($db, $action, $vars)){
        $key = gen_key();
        $_SESSION["key_connected"] = $key;
        $action = "UPDATE comptes SET key_connected=:key_connected WHERE id=:id_compte";
        $vars = array(":id_compte"=>$_SESSION["id_compte"],
                      ":key_connected"=>$key);
        header("../web/index.php");
    }
    else{
        disconnect();
        $_SESSION["erreur_inscription"] = "Il y a eu une erreur, veuillez réessayer plus tard.";
        header("../web/inscription.php");
    }
}
else{
    disconnect(true);
}

?>