<?php

require_once __DIR__ . '/../../vendor/autoload.php';

use Santa\Day03\DayThree;

if (count($argv) < 2) {
    echo "usage: php $argv[0] filename\n";
    die();
}

$check = new DayThree();
$handle = fopen($argv[1], 'r');

while (($line = fgets($handle)) !== false) {
    $tmp = explode(' ', preg_replace('!\s+!', ' ', trim($line)));
    $input[] = $tmp;
}
fclose($handle);

echo $check->checkForAmountOfValids($input);
