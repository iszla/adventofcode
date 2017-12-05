<?php

require_once __DIR__ . '/../../vendor/autoload.php';

use Santa\Day01\DayOne;

if (count($argv) < 2) {
    echo "usage: php $argv[0] filename\n";
    die();
}

$nav = new DayOne();
$input = fgets(fopen($argv[1], 'r'));


echo $nav->navigate($input)."\n";

echo $nav->navigateToFirstDouble($input)."\n";
