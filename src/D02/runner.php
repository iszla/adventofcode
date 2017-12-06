<?php namespace AOC\D02;

require_once __DIR__ . '/../../vendor/autoload.php';
use AOC\D02\DayTwo;

$checksum = new DayTwo();

$handle = fopen($argv[1], 'r');
$sheet = [];

while (($line = fgets($handle)) !== false) {
    $sheet[] = trim($line);
}

$checksum->processSheet($sheet);
echo $checksum->getChecksum()."\n";

$checksum->processSheetDivision($sheet);
echo $checksum->getChecksum()."\n";
