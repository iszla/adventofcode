<?php

ini_set('memory_limit','2048M');

$passkey = "ckczppom";
$results = [];

// Step two million per run
for ($digit = 3000000; $digit < 5000000; $digit++) {;
    array_push($results, [md5($passkey.$digit), $digit]);
}

sort($results);

// Print top three to confirm if sort worked
print_r($results[0]);
print_r($results[1]);
print_r($results[2]);