<?php namespace AOC\D01;

require_once __DIR__ . '/../../vendor/autoload.php';

use AOC\D01\DayOne;

$t = new DayOne();
$input = fgets(fopen($argv[1], 'r'));

echo $t->sum($input)."\n";
echo $t->sum2($input)."\n";
