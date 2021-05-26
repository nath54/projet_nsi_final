<?php
$debug = true;
session_start();

if($debug){
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
}

/**
 * Crée une boîte de dialogue contenant `$texte`
 *
 * @param string $texte
 *      Texte devant être écrit dans la boîte de dialogue
 *
 * @return void
 *
 * @author Nathan
**/
function alert($texte){
    $texte = htmlspecialchars($texte);
    script("alert(\"$texte\");");
}

/**
 * Écrit `$texte` dans la console du navigateur
 *
 * @param string $texte
 *      Texte à écrire pour le debug
 *
 * @return void
 *
 * @author Nathan
**/
function clog($texte){
    $texte = htmlspecialchars($texte);
    script("console.log(\"$texte\");");
}


/**
 * Crée une balise script dans le code, contenant `$texte`.
 *
 * @param string $texte
 *      Instructions à exécuter.
 *
 * @return void
 *
 * @author Nathan
**/
function script($texte){
    echo "<script>$texte</script>";
}



function array_to_str($array){
    $txt = "{";
    $virg = false;
    foreach($array as $k=>$v){
        if($virg){
            $txt .= ", ";
        }
        else{
            $virg = true;
        }
        $txt .= "$k : $v";
    }
    $txt .= "}";
    return $txt;
}


/**
 * Generate a random string, using a cryptographically secure 
 * pseudorandom number generator (random_int)
 * 
 * For PHP 7, random_int is a PHP core function
 * For PHP 5.x, depends on https://github.com/paragonie/random_compat
 * 
 * @param int $length      How many characters do we want?
 * @param string $keyspace A string of all possible characters
 *                         to select from
 * @return string
 */
function random_str(
    $length,
    $keyspace = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
) {
    $str = '';
    $max = strlen($keyspace) - 1;
    if ($max < 1) {
        throw new Exception('$keyspace must be at least two characters long');
    }
    for ($i = 0; $i < $length; ++$i) {
        $str .= $keyspace[random_int(0, $max)];
    }
    return $str;
}


//

$images_corps = array(
    "tete"=> ["casque_chevalier.png", "chapeau_sorcier.png", "rien.png"],
    "cheveux"=> ["cheveux_coupe_1.png", "cheveux_coupe_2.png", "rien.png"],
    "barbe"=> ["barbe_1.png", "barbe_2.png", "rien.png"],
    "haut"=> ["t_shirt_bleu.png", "t_shirt_rouge.png", "tshirt_bleu.png", "rien.png"],
    "bas"=> ["pantalon_bleu.png", "pantalon_noir.png", "rien.png"],
    "pied"=> ["pied_noir.png", "pied_rouge.png", "rien.png"]
);

?>