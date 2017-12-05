<?php

require_once __DIR__ . '/../../vendor/autoload.php';

use Santa\Day02\DayTwo;

if (count($argv) < 2) {
    echo "usage: php $argv[0] filename\n";
    die();
}

$key = new DayTwo(DayTwo::DOOR);
$handle = fopen($argv[1], 'r');

while (($line = fgets($handle)) !== false) {
    $input[] = $line;
}
fclose($handle);

echo $key->getCode($input)."\n";

echo $key->setType(DayTwo::BATHROOM)->getCode($input)."\n";