<?php namespace AOC\D02;

class DayTwo
{
    protected $checkSum;

    public function __construct()
    {
        $this->reset();
        $this->debug = false;
    }

    public function SetDebugMode(bool $debug)
    {
        $this->debug = $debug;
    }

    public function reset()
    {
        $this->checkSum = 0;
    }

    public function getChecksum()
    {
        return $this->checkSum;
    }

    public function checkRow($row)
    {
        $values = explode(' ', $row);

        $max = PHP_INT_MIN;
        $min = PHP_INT_MAX;

        for ($i=0; $i < count($values); $i++) { 
            if ($max < $values[$i]) $max = $values[$i];
            if ($min > $values[$i]) $min = $values[$i];
        }

        $rowChecksum = $max - $min;
        $this->checkSum += $rowChecksum;
        if ($this->debug) echo "$max - $min = $rowChecksum\n";
        return $rowChecksum;
    }

    public function checkDivide($row)
    {
        $values = explode(' ', $row);
        $rowChecksum = null;

        for ($i=0; $i < count($values); $i++) { 
            for ($j=0; $j < count($values); $j++) { 
                if ($i === $j) continue;

                $a = $values[$i] / $values[$j];
                if (floor($a) == $a) $rowChecksum = $a;
            }
        }

        $this->checkSum += $rowChecksum;
        return $rowChecksum;
    }

    public function processSheet($sheet)
    {
        $this->reset();

        foreach ($sheet as $row) {
            $this->checkRow($row);
        }
    }

    public function processSheetDivision($sheet)
    {
        $this->reset();

        foreach ($sheet as $row) {
            $this->checkDivide($row);
        }
    }
}