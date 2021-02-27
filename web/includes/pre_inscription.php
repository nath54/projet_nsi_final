
<?php

include_once "../includes/init.php";

$email = $_POST["email"];
$code = gen_key(6);

$to      = $email;
$subject = "Code de vérification d'email";
$message = 'Votre code de vérification est : '.$code;

mail($to, $subject, $message);
?>
